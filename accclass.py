class Account:
  """
  Class that generates new instances of contacts.
  """

  account_list = [] # Empty contact list

  def __init__(self,first_name,last_name,phone_number,email):

    # docstring removed for simplicity
      
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email


  def save_accclass(self):

    '''
    save_contact method saves contact objects into contact_list
    '''
    Account.account_list.append(self)