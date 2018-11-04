class Account:
  """
  Class that generates new instances of account.
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
    save_account method saves account objects into account_list
    '''
    Account.account_list.append(self)

  def delete_account(self):

    '''
    delete_account method deletes a saved account from the account_list
    '''

    Account.account_list.remove(self) 

  @classmethod
  def display_accounts(cls):
    '''
     method that returns the contact list
    '''
    return cls.account_list