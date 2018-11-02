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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_accclass.first_name,"Fred")
        self.assertEqual(self.new_accclass.last_name,"Wamalwa")
        self.assertEqual(self.new_accclass.phone_number,"0702049058")
        self.assertEqual(self.new_accclass.email,"fredkheisa@gmail.com")

    def test_save_account(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_accclass.save_accclass() # saving the new account
        self.assertEqual(len(Account.account_list),1)
    

    def test_save_multiple_account(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_accclass.save_accclass()
        test_accclass = Account("Test","user","0712345678","test@user.com") # new account
        test_accclass.save_accclass()
        self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_accclass.save_accclass()
            test_accclass = Account("Test","user","0712345678","test@user.com") # new contact
            test_accclass.save_accclass()

            self.new_accclass.delete_account()# Deleting a contact object
            self.assertEqual(len(Account.account_list),1)


    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_accclass.save_accclass()
        test_accclass = Account("Test","user","0711223344","test@user.com") # new contact
        test_accclass.save_accclass()

        found_accclass = account.find_by_phone_number("0711223344")

        self.assertEqual(found_accclass.email,test_accclass.email)


if __name__ == '__main__':
    unittest.main()
