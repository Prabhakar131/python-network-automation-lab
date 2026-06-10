'''
Scenario 1 - Username Validity
- Strings and Conditions
- Check if empty
- check if atleast 5 characters long
- converted to lowercase before saving
'''



class UsernameValidity:
    def __init__(self,username):
        self.username = username 
       
    def check_empty(self,):
        if len(self.username) == 0:
            return True
        else:
            return False
    
    def check_length(self):
        if len(self.username) >= 5 :
            return True
        else:
            return False
    
    def check_spaces(self):
        if " " in self.username:
            return True
        else:
            return False
    
    def valid_username(self):
        if self.check_length() == True and self.check_spaces() == False and self.check_empty() == False:
            return True
        else:
            return False
    
    def save_username(self):
        if self.valid_username() == True:
            self.username = self.username.lower()
            return True
        else:
             return False

    def overall_checking(self):
        if self.save_username() == True:
            print("Username is valid and was saved successfully")
        else:
            print('Please check if username is not empty or longer than 5 characters or has no spaces and enter again')


def retrieve_user_input():
    username = input("Please enter the username: ")
    return username 

username = retrieve_user_input()
username_validity_check = UsernameValidity(username)
username_validity_check.overall_checking()