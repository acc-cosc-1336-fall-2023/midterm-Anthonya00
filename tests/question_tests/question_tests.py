#write function tests here, don't add input('') statements here!
import unittest
from src.question_b.question_b import is_prime

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_miles_per_hour


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(get_miles_per_hour(32,60), 19.883872)

    def test_question_b_config(self):
        self.assertEqual(is_prime(4),False)
        self.assertEqual(is_prime(5),True)
        self.assertEqual(is_prime(11),True)

