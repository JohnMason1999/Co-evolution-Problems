#shows that under no evolutionary pressure our mutation drifts towards half of maximum fitness
#maximum fitness is (vectors * scalar_length)/2

import PopulationTools as poptools
import statistics

mutation_rate = 0.05
vectors = 1
population_size = 25
scalar_length = 100
generations = 600

unfit_population = poptools.gen_population(population_size,vectors,scalar_length)
fit_population = poptools.gen_fittest_population(population_size,vectors,scalar_length)
for x in range(generations):
    unfit_population = poptools.mutate_population(unfit_population,mutation_rate)
    fit_population = poptools.mutate_population(fit_population,mutation_rate)

 #shows average fitness of the populations
print("unfit population average: "+str((statistics.mean(poptools.obj_score_pop(unfit_population)))))
print("fit population average: "+str((statistics.mean(poptools.obj_score_pop(fit_population)))))
