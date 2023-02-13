import random
TARGET = str(input("Enter a target:"))

POPULATION_SIZE = 100

MUTATION_RATE = 0.1

def fitness(candidate):
    score = 0
    for i in range(len(candidate)):
        if candidate[i] == TARGET[i]:
            score += 1
    return score

def mutate(candidate):
    mutated = ""
    for i in range(len(candidate)):
        if random.uniform(0, 1) < MUTATION_RATE:
            mutated += chr(random.randint(32, 126))
        else:
            mutated += candidate[i]
    return mutated
population = [''.join([chr(random.randint(32, 126)) for j in range(len(TARGET))]) for i in range(POPULATION_SIZE)]

generation = 0
while True:
    scores = [fitness(candidate) for candidate in population]
    population = [population[i] for i in range(POPULATION_SIZE) if scores[i] == max(scores)]
    if TARGET in population:
        break
    new_population = []
    for i in range(POPULATION_SIZE):
        parent1 = population[random.randint(0, len(population) - 1)]
        parent2 = population[random.randint(0, len(population) - 1)]
        child = ""
        for j in range(len(parent1)):
            if random.uniform(0, 1) < 0.5:
                child += parent1[j]
            else:
                child += parent2[j]
        new_population.append(mutate(child))
    population = new_population
    generation += 1
    
print("Target:", TARGET)
print("Found: ", population[0])
print("Generations: ", generation)
