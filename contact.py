class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = []

    def __init__(self,first_name,last_name,number,email):


        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
