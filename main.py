
import random
import copy
import math
import graphs



# TODO
# add muations /
# make graphs
# finish the readme

# # # # # # DISPLAY FUNCTIONS # # # # # #

def max_in_generation_list(generations : list) -> list:
        return [generation_max_value(i) for i in generations]


def print_generation(generation : list) -> None:
    print(generation_string(generation))


def generation_string(generation: list) -> str:
    out = ""
    for bag in enumerate(generation):
        out += ("Bag " + str(bag[0]) + " current weight: " + str(bag_weight(bag[1])) +
                                       ", current value: " + str(bag_value(bag[1])) +
                                       ", bricks: " + str(bag_string(bag[1])) + "\n")
    return out


def bag_string(bag: list) -> str:
    out = ""
    first = True
    for brick in bag:
        if not first:
            out += "," + brick_string(brick)

        else:
            out = "{ " + brick_string(brick)
            first = False
    return out + " }"


def brick_string(brick: dict) -> str:
    return "[" + str(brick_weight(brick)) + "," + str(brick_value(brick)) + "]"


# # # # # # generation functions # # # # # #

def first_generation(brick_pool: list, max_weight: int = 20, generation_size: int = 8) -> list:
    if generation_size is 0:
        return []
    else:
        return [make_bag(brick_pool, max_weight)] + first_generation(brick_pool, max_weight, generation_size - 1)


def next_generation(last_generation: list, brick_pool, max_weight: int = 20, mutation_chance: int = -1)-> list:
    return mating_season(pair_list(breeding_pool(generation_sort(last_generation))),
                         max_weight, brick_pool, mutation_chance)


def mutate(child: list, brick_pool) -> list:
    if random.choice([True, False]):
        if len(child) is 0:
            return child
        if len(child) is 1:
            child.pop(0)
            return child
        if len(child) > 1:
            child.pop(random.randint(0, len(child) - 1))
    else:
        child.append(random.choice(list(brick_pool)))

    return child


def breeding_pool(sorted_generation: list) -> list:
    return sorted_generation[math.ceil(len(sorted_generation)/2):]


def pair_list(breeding_pool: list) -> list:

    if breeding_pool is []:
        return []
    if len(breeding_pool) is 1:
        return []
    if len(breeding_pool) is 2:
        return [breeding_pool]
    parent1 = breeding_pool.pop(random.randrange(0, len(breeding_pool) - 1))
    parent2 = breeding_pool.pop(random.randrange(0, len(breeding_pool) - 1))
    return [[parent1, parent2]] + pair_list(breeding_pool)


def mating_season(pairs: list, max_weight: int, brick_pool:list, mutation_chance: int) -> list:
    if not pairs:
        return []
    pair = pairs.pop(0)
    return breed(pair[0], pair[1], 4, max_weight, brick_pool, mutation_chance) + \
        mating_season(pairs, max_weight, brick_pool, mutation_chance)


def breed(parent1: list, parent2: list, children: int, max_weight: int, brick_pool: list, mutation_chance: int) -> list:
    genes = parent1 + parent2
    children_list = []
    j = 0
    while j < children:
            child = []
            for i in range(len(genes)):
                if random.choice([True, False]):
                    child.append(genes[i])

            if mutation_chance != -1 and random.randint(0, mutation_chance) == 0:
                child = mutate(child, brick_pool)
            if bag_weight(child) <= max_weight and child != []:
                children_list.append(child)
                j += 1

    return children_list


def generation_sort(generation: list)-> list:
    if not generation:
        return []
    if len(generation) is 1:
        return generation

    return sorted(generation, key=sort_criteria)


def sort_criteria(x):
    return bag_value(x)


# # # # # # statistical functions # # # # # #

def generation_average_weight(generation: list) -> float:
    return sum(map(bag_weight, generation))/len(generation)


def generation_max_weight(generation: list) -> int:
    return max(map(bag_weight, generation))


def generation_min_weight(generation: list) -> int:
    return min(map(bag_weight, generation))


def generation_average_value(generation: list) -> float:
    return sum(map(bag_value, generation))/len(generation)


def generation_max_value(generation: list) -> int:
    return max(map(bag_value, generation))


def generation_min_value(generation: list) -> int:
    return min(map(bag_value, generation))


# # # # # # bag functions # # # # # #

def make_bag(brick_pool: list, max_weight: int) -> list:
    brick_pool_copy = copy.deepcopy(brick_pool)
    return make_bag_recursive([], brick_pool_copy, max_weight)


def make_bag_recursive(accumulator: list, brick_pool: list, max_weight: int) -> list:
    if not brick_pool:
        return []

    brick = None
    try:
        brick = brick_pool.pop(random.randint(1, len(brick_pool)) - 1)
    except ValueError:
        brick = brick_pool.pop(0)

    if (bag_weight(accumulator) + brick_weight(brick)) > max_weight:
        return accumulator
    else:
        return make_bag_recursive(accumulator + [brick], brick_pool, max_weight)


def bag_weight(bag: list) -> int:
    if not bag:
        return 0
    else:
        return sum(list(map(brick_weight, bag)))


def bag_value(bag: list) -> int:
    if not bag:
        return 0
    else:
        return sum(list(map(brick_value, bag)))


# # # # # # brick functions # # # # # #

def brick_weight(brick: dict) -> int:
    return brick['weight']


def brick_value(brick: dict) -> int:
    return brick['value']


def main():

    graphs.bar_chart_on_mutation_effects()


if __name__ == '__main__':
    main()

