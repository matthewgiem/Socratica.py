import datetime

class User:
    pass

user1 = User()
user1.first_name = 'Matt'
user1.last_name = 'Giem'

print(user1.last_name) # 'Giem'

first_name = 'Author'
last_name = 'Clarke'

print(user1.first_name, user1.last_name)
# "Matt Giem"

print(first_name, last_name)
# "Author Clarke"


user2 = User()
user2.first_name = 'Frank'
user2.last_name = 'Poole'

class User:
    '''A member of FriendFace. For now we are
    only storing their name and birthday
    But soon we sill stroe an uncomfortable
    amount of user information.'''
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # YYYMMDD

        # extract first and last name
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
         yyyy = int(self.birthday[0:4)]
         mm = int(self.birthday[4:6])
         dd = int(self.birthday[6:8])
         dob = datetime.date(yyyy, mm, dd)  # Date of birthday
         age_in_days = (today-dob).days
         age_in_years = age_in_days/365
         return age_in_years

user = User('Matthew Giem', '19850130')
