import unittest
import recipies.recipe1.fib as fib

class Testing(unittest.TestCase):
    
    def test_testing(self):
        self.assertEqual(1,1, "Of course it does!")

if __name__ == "__main__":
    unittest.main()
