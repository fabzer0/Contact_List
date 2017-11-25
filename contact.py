import pyperclip

class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = []
    # Init method up here
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)


    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)


    def __init__(self,first_name,last_name,number,email):


        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
