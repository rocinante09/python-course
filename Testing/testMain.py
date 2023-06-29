import unittest
import main_class_to_test as main

'''
this fille needs to start with 'test'
'''


class TestMain(unittest.TestCase):
    def setUp(self):
        print('in setup')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdf'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result,TypeError))

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result,TypeError))

    def test_do_stuff4(self):
        test_param = 500000000.2435
        result = main.do_stuff(test_param)
        self.assertEqual(result, 500000005.2435 )

    def tearDown(self) -> None:
        print('clean up your shit')



if __name__ == '__main__':
    unittest.main()