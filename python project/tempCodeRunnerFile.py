user=int(input("1. for add new user, 2. for finding user"))
if(user==1):
    users.new_user()
elif(user==2):
    username=users.enter_user()
    print(username)