
import unittest
import main


class MainTests(unittest.TestCase):

    def setUp(self):

        self.brick_pool = [
              {'weight': 2, 'value': 4},
              {'weight': 3, 'value': 6},
              {'weight': 4, 'value': 5},
              {'weight': 4, 'value': 8},
              {'weight': 6, 'value': 11},
              {'weight': 7, 'value': 12},
              {'weight': 9, 'value': 15},
              {'weight': 11, 'value': 18}]

    def test_bag_value(self):
        test_bag = [{'weight': 2, 'value': 4},
                    {'weight': 3, 'value': 6}]

        self.assertEquals(main.bag_value(test_bag),10)

    def test_bag_weight(self):
        test_bag = [{'weight': 2, 'value': 4},
                    {'weight': 3, 'value': 6}]

        self.assertEquals(main.bag_weight(test_bag), 5)

    def test_make_bag(self):
        test_pool = [{'weight': 2, 'value': 4},
                    {'weight': 3, 'value': 6}]

        test_bag = main.make_bag(test_pool, 2)

        if main.bag_weight(test_bag) is 2:
            self.assertEquals(main.bag_value(test_bag), 4)
        else:
            self.assertEquals(main.bag_value(test_bag), 0)

    def test_make_bag_empty_pool(self):

        test_bag =  main.make_bag([], 10)
        self.assertTrue(True)

    def test_first_generation(self):
        generation = main.first_generation(self.brick_pool, 20, 5)
        print(main.print_generation(generation))
        self.assertTrue(True)

    def test_generation_sort(self):
        print(main.print_generation(main.generation_sort(main.first_generation(self.brick_pool, 20, 5))))


    def test_breed(self):
        generation = main.first_generation(self.brick_pool, 20, 8)
        print(main.print_generation(generation))
        print("-----------")
        print(main.print_generation(main.breed(generation[0], generation[1], 8, 20, self.brick_pool, 2)))

    def test_pair_list(self):
        generation = main.first_generation(self.brick_pool, 20, 8)
        print(main.print_generation(generation))
        print("--------")
        pair_list = main.pair_list(generation)
        print(pair_list)

    def test_mating_season(self):
        generation = main.first_generation(self.brick_pool, 20, 8)
        pair_list = main.pair_list(
                    main.breeding_pool(
                        main.generation_sort(generation)))

        print(main.generation_string(generation))
        next_generation = main.mating_season(pair_list, 20, self.brick_pool, -1)
        print(main.generation_string(next_generation))

    def test_next_generation(self):
        gen = main.first_generation(self.brick_pool, 20, 8)
        for i in range(10):
            print(main.print_generation(gen))
            gen = main.next_generation(gen, self.brick_pool, 20, -1)

    def test_generation_csv_max_value(self):
        # if that's not 20 the whole thing breaks , investigate
        gen = main.first_generation(self.brick_pool, 20, 10)

        for i in range(100):
            gen = main.next_generation(gen, self.brick_pool, 20, 1)
            print(main.generation_max_value(gen), end=",")

        print()
        print(main.print_generation(gen))
