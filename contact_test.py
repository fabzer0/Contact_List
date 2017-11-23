import unittest #importing unittest module
from contact import Contact # importing the contact class

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
    '''
    Set up method to run before each test classes.
    '''
    # create contact object
    self.new_contact = Contact("James", "Muriuki", "0703341751", "james@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email,"james@gmail.com")



if __name__ == '_main_':
    unittest.main()
