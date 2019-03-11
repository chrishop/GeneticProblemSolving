import matplotlib.pyplot as plt
import main

brick_pool = [
        {'weight': 2, 'value': 4},
        {'weight': 3, 'value': 6},
        {'weight': 4, 'value': 5},
        {'weight': 4, 'value': 8},
        {'weight': 6, 'value': 11},
        {'weight': 7, 'value': 12},
        {'weight': 9, 'value': 15},
        {'weight': 11, 'value': 18}]


def make_max_value_graph():
    # A graph showing the max weight for each generation.
    # with a generation size of 10
    # and 50 generations
    generation_size = 10
    generations = 50

    raw_generations = [main.first_generation(brick_pool, 20, generation_size)]

    for i in range(generations - 1):
        raw_generations.append(main.next_generation(raw_generations[len(raw_generations) - 1], brick_pool, 50))

    x = [i for i in range(generations)]
    y = main.max_in_generation_list(raw_generations)

    print(x)
    print(y)

    plt.plot(x, y)
    plt.show()


def show_whole_generation_graph():
    # make generation list
    # iterate through to make a series
    generation_size = 8
    generations = 50

    raw_generations = [main.first_generation(brick_pool, 20, generation_size)]
    for i in range(generations - 1):
        raw_generations.append(main.next_generation(raw_generations[len(raw_generations) - 1], brick_pool, 50))

    print(len(raw_generations))
    print(len(raw_generations[0]))

    x = [i for i in range(generations - 1)]
    child_value_series = []
    child_value = []
    for j in range(8 - 1):
        for i in range(50 - 1):
            print(i, j)
            child_value.append(main.bag_value(raw_generations[i][j]))
        child_value_series.append(child_value)
        child_value = []


    print(child_value_series)

    # plot all 10 members of the population throughout the generations
    for child in child_value_series:
        plt.plot(x, child)

    plt.show()


def affects_of_small_generation_size():
    # small generation size and weight value causes
    # local minimum without mutation
    generation_size = 4
    generations = 50

    raw_generations = [main.first_generation(brick_pool, 10, generation_size)]

    for i in range(generations - 1):
        raw_generations.append(main.next_generation(raw_generations[len(raw_generations) - 1], brick_pool, 50, -1))

    raw_generations_mutation = [main.first_generation(brick_pool, 10, generation_size)]

    for i in range(generations - 1):
        raw_generations_mutation.append(
            main.next_generation(raw_generations_mutation[len(raw_generations_mutation) - 1], brick_pool, 50, 15))

    x = [i for i in range(generations)]
    y1 = main.max_in_generation_list(raw_generations)
    y2 = main.max_in_generation_list(raw_generations_mutation)

    plt.plot(x, y1, 'b')
    plt.plot(x, y2, 'r')

    plt.show()


def mutation_effect():
    generation_size = 10
    generations = 50

    raw_generations_no_mutation = [main.first_generation(brick_pool, 20, generation_size)]
    raw_generations_small = [main.first_generation(brick_pool, 20, generation_size)]
    raw_generations_medium = [main.first_generation(brick_pool, 20, generation_size)]
    raw_generations_large = [main.first_generation(brick_pool, 20, generation_size)]

    for i in range(generations - 1):
        raw_generations_no_mutation.append(
            main.next_generation(raw_generations_no_mutation[len(raw_generations_no_mutation) - 1], brick_pool, 50))

        raw_generations_small.append(
            main.next_generation(raw_generations_small[len(raw_generations_small) - 1], brick_pool, 50, 49))

        raw_generations_medium.append(
            main.next_generation(raw_generations_medium[len(raw_generations_medium) - 1], brick_pool, 50, 19))

        raw_generations_large.append(
            main.next_generation(raw_generations_large[len(raw_generations_large) - 1], brick_pool, 50, 2))

    x = [i for i in range(generations)]
    y1 = main.max_in_generation_list(raw_generations_no_mutation)
    y2 = main.max_in_generation_list(raw_generations_small)
    y3 = main.max_in_generation_list(raw_generations_medium)
    y4 = main.max_in_generation_list(raw_generations_large)

    plt.plot(x, y1, 'r')
    plt.plot(x, y2, 'g')
    plt.plot(x, y3, 'b')
    plt.plot(x, y4, 'c')
    plt.show()


def bar_chart_on_mutation_effects():
    generation_size = 10
    generations = 50

    x1_win = 0
    x2_win = 0
    x3_win = 0
    x4_win = 0

    for k in range(5000):
        print(k)
        raw_generations_no_mutation = [main.first_generation(brick_pool, 20, generation_size)]
        raw_generations_small = [main.first_generation(brick_pool, 20, generation_size)]
        raw_generations_medium = [main.first_generation(brick_pool, 20, generation_size)]
        raw_generations_large = [main.first_generation(brick_pool, 20, generation_size)]

        x1 = main.generation_max_value(raw_generations_no_mutation[0])
        x2 = main.generation_max_value(raw_generations_small[0])
        x3 = main.generation_max_value(raw_generations_medium[0])
        x4 = main.generation_max_value(raw_generations_large[0])

        for i in range(generations - 1):
            raw_generations_no_mutation += \
                [main.next_generation(
                    raw_generations_no_mutation[len(raw_generations_no_mutation) - 1], brick_pool, 50)]

            raw_generations_small += \
                [main.next_generation(raw_generations_small[len(raw_generations_small) - 1], brick_pool, 50, 7)]

            raw_generations_medium += \
                [main.next_generation(raw_generations_medium[len(raw_generations_medium) - 1], brick_pool, 50, 3)]

            raw_generations_large += \
                [main.next_generation(raw_generations_large[len(raw_generations_large) - 1], brick_pool, 50, 1)]

            x1 = max(x1, main.generation_max_value(raw_generations_no_mutation.pop(0)))
            x2 = max(x2, main.generation_max_value(raw_generations_small.pop(0)))
            x3 = max(x3, main.generation_max_value(raw_generations_medium.pop(0)))
            x4 = max(x4, main.generation_max_value(raw_generations_large.pop(0)))

        x1 = max(x1, main.generation_max_value(raw_generations_no_mutation.pop(0)))
        x2 = max(x2, main.generation_max_value(raw_generations_small.pop(0)))
        x3 = max(x3, main.generation_max_value(raw_generations_medium.pop(0)))
        x4 = max(x4, main.generation_max_value(raw_generations_large.pop(0)))

        if x1 == max(x1, x2, x3, x4):
            x1_win += 1
        elif x2 == max(x1, x2, x3, x4):
            x2_win += 1
        elif x3 == max(x1, x2, x3, x4):
            x3_win += 1
        else:
            x4_win += 1

    y = max(x1_win, x2_win, x3_win, x4_win)
    print(y, x1_win, x2_win, x3_win, x4_win)
    bar_chart = plt.bar([1, 2, 3, 4], [x1_win, x2_win, x3_win, x4_win],
                        0.8, tick_label=['no mutation', 'small_mutation', 'medium_mutation', 'large_mutation'])

    plt.show()


def bar_chart_on_mutation_effects_small_population():
    generation_size = 4
    generations = 50

    x1_win = 0
    x2_win = 0
    x3_win = 0
    x4_win = 0

    for k in range(1000):
        raw_generations_no_mutation = [main.first_generation(brick_pool, 10, generation_size)]
        raw_generations_small = [main.first_generation(brick_pool, 10, generation_size)]
        raw_generations_medium = [main.first_generation(brick_pool, 10, generation_size)]
        raw_generations_large = [main.first_generation(brick_pool, 10, generation_size)]

        for i in range(generations - 1):
            raw_generations_no_mutation.append(
                main.next_generation(raw_generations_no_mutation[len(raw_generations_no_mutation) - 1], brick_pool, 50))

            raw_generations_small.append(
                main.next_generation(raw_generations_small[len(raw_generations_small) - 1], brick_pool, 50, 49))

            raw_generations_medium.append(
                main.next_generation(raw_generations_medium[len(raw_generations_medium) - 1], brick_pool, 50, 19))

            raw_generations_large.append(
                main.next_generation(raw_generations_large[len(raw_generations_large) - 1], brick_pool, 50, 2))

        x1 = main.generation_max_value(raw_generations_no_mutation[len(raw_generations_no_mutation) - 1])
        x2 = main.generation_max_value(raw_generations_small[len(raw_generations_small) - 1])
        x3 = main.generation_max_value(raw_generations_medium[len(raw_generations_medium) - 1])
        x4 = main.generation_max_value(raw_generations_large[len(raw_generations_large) - 1])

        if x1 == max(x1, x2, x3, x4):
            x1_win += 1
        elif x2 == max(x1, x2, x3, x4):
            x2_win += 1
        elif x3 == max(x1, x2, x3, x4):
            x3_win += 1
        else:
            x4_win += 1

    y = max(x1_win, x2_win, x3_win, x4_win)
    print(y, x1_win, x2_win, x3_win, x4_win)
    bar_chart = plt.bar([1, 2, 3, 4], [x1_win, x2_win, x3_win, x4_win],
                        0.8, tick_label=['no mutation', 'small_mutation', 'medium_mutation', 'large_mutation'])

    plt.show()
