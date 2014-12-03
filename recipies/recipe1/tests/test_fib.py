import unittest
import fib

class Testing(unittest.TestCase):
    
    def test_testing(self):
        self.assertEqual(1,1, "Of course it does!")

class Fib_(unittest.TestCase):

    def setUp(self):
        self.fib = fib.fib2

    def basecase_num_1(self):
        self.assertEqual(self.fib(1), 0, "fib num 1 is not correct")

    def basecase_num_2(self):
        self.assertEqual(self.fib(2), 1, "fib num 2 is not correct")

    def fib_num_10(self):
        self.assertEqual(self.fib(10), 34, "fib 10 is 33")

    def basecase_list_1(self):
        self.assertEqual(self.fib(1), [0], "fib list with one item is not correct")

    def basecase_list_2(self):
        self.assertEqual(self.fib(2), [0,1], "fib list 2 with two items is not correct")

    def fib_list_10(self):
        self.assertEqual(self.fib(10), [0,1,1,2,3,5,8,13,21,34],
        "Fib list ten is not correct")

class Fib1_testing(Fib_):
    def setUp(self):
        self.fib = fib.fib1

    def test_basecase_1(self):
        self.basecase_list_1()

    def test_basecase_2(self):
        self.basecase_list_2()

    def test_fib_list_10(self):
        self.fib_list_10()

class Fib2_testing(Fib_):
    def setUp(self):
        self.fib = fib.fib2

    def test_basecase_1(self):
        self.basecase_num_1()

    def test_basecase_2(self):
        self.basecase_num_2()

    def test_fib_num_10(self):
        self.fib_num_10()

class Fib_yield_list(Fib1_testing):
    def setUp(self):
        self.fib = fib.fib_list

class Fib_yield_num(Fib2_testing):
    def setUp(self):
        self.fib = fib.nth_fib_num

if __name__ == "__main__":
    unittest.main()
