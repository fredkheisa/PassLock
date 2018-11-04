
import unittest
from infoclass import Info 

class TestInfo(unittest.TestCase):
    """
    Test class that defines test cases for the platforms and passwords class behaviours.
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_infoclass = Info("facebook","these are fun times",) 

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Info.sitepass_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_infoclass.platform,"facebook")
        self.assertEqual(self.new_infoclass.password,"these are fun times")
    def test_save_pass(self):
        '''
        test_save_password test case to test if the password object is saved into
         the contact list
        '''
        self.new_infoclass.save_infoclass() # saving the new account
        self.assertEqual(len(Info.sitepass_list),1)

    def test_save_multiple_sitepass(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_infoclass.save_infoclass()
        test_infoclass = Info("platform","password") # new account
        test_infoclass.save_infoclass()
        self.assertEqual(len(Info.sitepass_list),2)


if __name__ == '__main__':
    unittest.main()