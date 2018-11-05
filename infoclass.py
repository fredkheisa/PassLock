class Info :
  """
  Class that generates new instances of account.
  """

  sitepass_list = [] # Empty contact list

  def __init__(self,platform,password,):

    # docstring removed for simplicity
      
    self.platform = platform
    self.password = password


  def save_infoclass(self):

    '''
    save_account method saves account objects into account_list
    '''
    Info.sitepass_list.append(self)

  def delete_sitepass(self):

    '''
    delete_contact method deletes a saved contact from the contact_list
    '''

    Info.sitepass_list.remove(self)

    