import random as rnd

def objscore(a):
    #a is an array of scalars represented by binary strings
    score = 0
    for scalar in a:
        count = 0
        for bit in scalar:
            if bit=='1':
                count = count + 1
        score = score + count
    return score

def objScorePop(pop):
    return [objscore(a) for a in pop]

def subjscores(pop,opppop,samplesize):
    scores = []
    mutations = []
    for p in pop:
        tempscore = score2(p,samplepop(opppop,samplesize))
        scores.append(tempscore[0])
        mutations.append(tempscore[1])
    return scores,mutations

def score(individual,opponents):
    score = 0
    for opp in opponents:
        if objscore(individual) > objscore(opp):
            score += 1
    return score

def score2(individual,opponents):
    score=0
    difference=0
    mutationpoints = []
    for opp in opponents:
        curx=0
        for x in range(len(individual)):
            curdif = abs(objscore(individual[x])-objscore(opp[x]))
            if curdif > difference:
                difference=curdif
                curx=x
        mutationpoints.append(curx)
        if objscore(individual[curx]) > objscore(opp[curx]):
            score +=1
    return score,mutationpoints

def score3(individual,opponents):
    score=0
    for opp in opponents:
        if abs(individual[0]-opp[0])<abs(individual[1]-opp[1]):
            if objscore([individual[0]]) > objscore([opp[0]]):
                score +=1
        else:
            if objscore([individual[1]]) > objscore([opp[1]]):
                score +=1
    return score

def genIndividual(length,numOfVecs):
    return [length*'0' for x in range(numOfVecs)]

def genPop(count,length,numOfVecs):
    pop = [genIndividual(length,numOfVecs) for x in range(count)]
    return pop

def mutateIndividual(ind,rate,mutation):
    newInd = []
    for dimension in range(len(ind)):
        newDim = ""
        for char in ind[dimension]:
            if dimension in mutation:
                if rnd.random() <= rate:
                    if char=='1':
                        newDim = newDim+"0"
                    else:
                        newDim +="1"
                else:
                    newDim = newDim + char
            else:
                newDim = newDim+char
        newInd.append(newDim)
    return newInd

def mutatePop(pop,rate,mutations):
    newPop = [mutateIndividual(pop[i],rate,mutations[i]) for i in range(len(pop))]
    return newPop

def propselection(pop,opponents,size):
    totalscore = 0
    scores = []
    mutations = []
    for p in pop:
        tempscore = score2(p,samplepop(opponents,size))
        mutations.append(tempscore[1])
        scores.append(tempscore[0])
        totalscore += tempscore[0]
    if totalscore==0:
        return pop,scores,mutations
    else:
        randnum = rnd.random()*totalscore
        current=0
        newpop=[]
        for x in range(len(pop)):
            found=False
            for p in range(len(pop)):
                current+=scores[p]
                if current>randnum:
                    if found==False:
                        newpop.append(pop[p])
                        found=True   
            if found==False:
                newpop.append(pop[x])
        return newpop,scores,mutations

def samplepop(pop,size):
    sample = []
    newpop = pop.copy()
    for x in range(size):
        individual=rnd.choice(newpop)
        newpop.remove(individual)
        sample.append(individual)
    return sample
	
import pandas as pd

popsize = 25
indLength = 100
mutationRate = 0.005
dimensions = 1
samplesize = 15
generations = 600

pop1 = genPop(popsize,indLength,dimensions)
pop2 = genPop(popsize,indLength,dimensions)
objscores1 = objScorePop(pop1)
objscores2 = objScorePop(pop2)
subjscore1 = []
subjscore2 = []

for x in range(generations):
    #form new pop from existing using fitness proportianate selection
        #pick an individual popsize times, individuals chance of being picked is-
        #subjective fitness of individual/total subj fitness of population
    pop1tup = propselection(pop1,pop2,samplesize)
    pop2tup = propselection(pop2,pop1,samplesize)
    #evolve the population
    pop1 = mutatePop(pop1tup[0],mutationRate,pop1tup[2])
    pop2 = mutatePop(pop2tup[0],mutationRate,pop2tup[2])
    
    #add individuals objective score to a dataframe under the current generation
    objscores1.extend(objScorePop(pop1))
    subjscore1.append(sum(pop1tup[1]))
    objscores2.extend(objScorePop(pop2))
    subjscore2.append(sum(pop2tup[1]))
    #repeat
	
df1 = pd.DataFrame({'Objective Fitness':objscores1, 'Generations':[x//popsize for x in range(len(objscores1))]})
sdf1 = pd.DataFrame({'Subjective Fitness':subjscore1, 'Generations':[x for x in range(len(subjscore1))]})
df2 = pd.DataFrame({'Objective Fitness':objscores2, 'Generations':[x//popsize for x in range(len(objscores2))]})
sdf2 = pd.DataFrame({'Subjective Fitness':subjscore2, 'Generations':[x for x in range(len(subjscore2))]})

import matplotlib.pyplot as plt
plt.plot([x//popsize for x in range(len(objscores1))],objscores1,'k,')
plt.ylim(0,100)
plt.xlabel('Generations')
plt.ylabel('Objective Fitness')