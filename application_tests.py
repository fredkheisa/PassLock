import unittest # Importing the unittest module
from accclass import Account # Importing the contact class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the Account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_accclass = Account("Fred","Wamalwa","0702049058","fredkheisa@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_accclass.first_name,"Fred")
        self.assertEqual(self.new_accclass.last_name,"Wamalwa")
        self.assertEqual(self.new_accclass.phone_number,"0702049058")
        self.assertEqual(self.new_accclass.email,"fredkheisa@gmail.com")


if __name__ == '__main__':
    unittest.main()
