import random as rnd

def obj_score(individual):
    #a is an array of scalars represented by binary strings
    count = 0
    for scalar in individual:
        for bit in scalar:
            if bit=='1':
                count = count + 1
    return count

def obj_score_pop(pop):   #returns a list of objective scores for a population
    return [obj_score(a) for a in pop]

def sample_pop_random(pop,size):
    sample = []
    newpop = pop.copy()
    for x in range(size):
        individual=rnd.choice(newpop)
        newpop.remove(individual)
        sample.append(individual)
    return sample

def sample_pop_best(pop,size): #UNFINISHED
    sample = []
    newpop = pop.copy()
    scores = obj_score_pop(pop)
    return None

def gen_individual(vectors,length):
    return [length*'0' for x in range(vectors)]

def gen_fittest_individual(vectors,length):
    return [length*'1' for x in range(vectors)]

def gen_population(size,vectors,length):
    return [gen_individual(vectors,length) for x in range(size)]

def gen_fittest_population(size,vectors,length):
    return [gen_fittest_individual(vectors,length) for x in range(size)]

def gen_random_individual(vectors,length): #each bit in this individual starts randomised, instead of starting as all 0's
    return ["".join([(rnd.choice("01")) for x in range(length)]) for y in range(vectors)]

def gen_random_population(size,vectors,length):
    return [gen_random_individual(vectors,length) for x in range (size)]

def mutate_population(population,mutation_rate):
    new_population = []
    for individual in population:
        new_population.append(mutate_individual(individual,mutation_rate))
    return new_population

def mutate_individual(individual,mutation_rate):
    new_individual = []
    for scalar in individual:
        new_individual.append(mutate_scalar(scalar,mutation_rate))
    return new_individual

def mutate_scalar(scalar,mutation_rate):
    new_scalar = []
    for char in scalar:
        if rnd.random() <= mutation_rate:
            if char == '0':
                new_scalar.append('1')
            else:
                new_scalar.append('0')
        else:
            new_scalar.append(char)
    return "".join(new_scalar)

#takes scores as argument so method can be used with subjective or objective scoring
def fitness_proportionate_selection(population,population_scores,size):
    new_population = []
    for x in range(size):
        selection = []
        selection_int = rnd.randint(0,sum(population_scores))
        current = 0
        for i in range(len(population)):
            current += population_scores[i]
            if current >= selection_int:
                selection = population[i]
        new_population.append(selection)
    return new_population