#shows that under no evolutionary pressure our mutation drifts towards half of maximum fitness

import PopulationTools as poptools
import statistics

mutation_rate = 0.05
vectors = 1
population_size = 50
scalar_length = 100
generations = 600

population = poptools.gen_population(population_size,vectors,scalar_length)
for x in range(generations):
    population = poptools.mutate_population(population,mutation_rate)
print(statistics.mean(poptools.obj_score_pop(population))) #shows average fitness of the population
