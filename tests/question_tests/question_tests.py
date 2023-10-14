#write function tests here, don't add input('') statements here!
import unittest

from src.question_b.question_b import is_prime
from src.question_c.question_c import get_random_number

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_miles_per_hour


class Test_Config(unittest.TestCase):
#test case for question A
    def test_question_a_config(self):
        self.assertEqual(get_miles_per_hour(32,60), 19.883872)
#test case for question B
    def test_question_b_config(self):
        self.assertEqual(is_prime(4),False)
        self.assertEqual(is_prime(5),True)
        self.assertEqual(is_prime(11),True)
#test case for question C
    def test_question_c_config(self): 
        x = get_random_number()
        y = x >= 1 and x <= 5
        self.assertEqual(y,True)
#test case for question D