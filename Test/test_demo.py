
import unittest
import demo


class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calculate = demo.Calculate()


    def tearDown(self):
        print("This is a teardown method")
    
    @unittest.skipIf(True,"Skipping this test for some reason")
    def test_add(self):
        
        self.assertEqual(self.calculate.add(25,5),30)

    def test_sub(self):
        
        self.assertEqual(self.calculate.sub(50,25),25)

    def test_mul(self):
        
        self.assertEqual(self.calculate.mul(5,5),25)

    @unittest.skipIf(True,"Skipping this test for some reason")
    def test_div(self):
        self.assertEqual(self.calculate.div(40,5),8)

        with self.assertRaises(ValueError):
            self.calculate.div(10,0)


if __name__ == '__main__':
    unittest.main()




