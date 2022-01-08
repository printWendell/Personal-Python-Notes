import unittest
import randint

class Test_Randint(unittest.TestCase): 
    
    def test_input(self): 
        answer = 5
        guess = 5
        result = randint.run_guess(answer, guess)
        self.assertTrue(result)
    
    def test_input_wrong_guess(self): 
        answer = 5
        guess = 0
        result = randint.run_guess(answer, guess)
        self.assertFalse(result)
    
    def test_input_wrong_number(self): 
        result = randint.run_guess(5, 11)
        self.assertFalse(result)
    
    def test_input_string(self): 
        result = randint.run_guess(5, '11')
        self.assertFalse(result)
    
    def test_input_array(self): 
        result = randint.run_guess(5, [])
        self.assertFalse(result)


if __name__ == '__main__': 
    unittest.main()