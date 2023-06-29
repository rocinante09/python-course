import unittest
import testing_exercise as main

'''
this fille needs to start with 'test'
'''

class TestMain(unittest.TestCase):
    def setUp(self):
        pass


    def test_check_guess(self):
        guess = 2
        answer = 2
        result = main.check_guess(guess, answer)
        self.assertTrue(result)

    def test_check_guess_wrong(self):
        guess = 2
        answer = 3
        result = main.check_guess(guess, answer)
        self.assertFalse(result)

    def test_check_guess_out_of_range(self):
        guess = 11
        answer = 3
        result = main.check_guess(guess, answer)
        self.assertFalse(result)


    def test_check_guess2(self):
        guess = 'asdf'
        answer = 2
        result = main.check_guess(guess, answer)
        self.assertFalse(result)

    def test_check_guess3(self):
        guess = 2
        answer = 'asdf'
        result = main.check_guess(guess, answer)
        self.assertFalse(result)


    def test_check_range1(self):
        test_param = 2
        result = main.is_range_correct(2, 1, 10)
        self.assertTrue(result, True)

    def test_check_range2(self):
        result = main.is_range_correct('asas', 1, 10)
        self.assertTrue(isinstance(result,TypeError))

    def test_check_range3(self):
        result = main.is_range_correct(2, 'asas', 10)
        self.assertTrue(isinstance(result,TypeError))


    def test_check_range3(self):
        result = main.is_range_correct(2, 1, 'asas')
        self.assertTrue(isinstance(result,TypeError))


    def tearDown(self) -> None:
        pass



if __name__ == '__main__':
    unittest.main()