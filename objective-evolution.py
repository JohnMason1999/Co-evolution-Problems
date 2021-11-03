#demonstration of how trivial evolution in our experiment is when we have access to objective scoring

import PopulationTools as poptools
import statistics

mutation_rate = 0.005
scalar_length = 100
vectors = 1
population_size = 25
generations = 600

population = poptools.gen_population(population_size,vectors,scalar_length)
for x in range(generations):
    new_population = poptools.mutate_population(population,mutation_rate)
    population = poptools.fitness_proportionate_selection(population+new_population,poptools.obj_score_pop,population_size)

print("maximum fitness: " + str(vectors*scalar_length))
print("average fitness: "+str(statistics.mean(poptools.obj_score_pop(population))))