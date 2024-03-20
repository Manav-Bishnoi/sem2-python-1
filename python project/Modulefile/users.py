def if_user_exists(name):
    a=False

    with open("user_file.txt","r") as fobj:
        for i in fobj:
            b=i.split(";")
            if b[0]==name:
                a=True
        return a
def new_user():
        with open("user_file.txt","a") as fobj:
            while True:

                user_name=input("enter new user name")
                checkk=if_user_exists(user_name)
                if checkk==True:
                     print("user already exists")
                     continue
                user_password=input("enter new user password")
                user_password_confirm=input("confirm new user password")
                try:
                    if (user_password==user_password_confirm):
                        fobj.write(user_name)
                        fobj.write(";")
                        fobj.write(user_password)
                        fobj.write("\n")
                        print("user created")
                        break
                    else:
                         raise Exception("both passwords are diffrent")
                except:
                     print("both passwords should be same")

def find_user():
                user_name=input("enter user name")
                user_password=input("enter user password")
                user_password=user_password+"\n"
                a=False

                with open("user_file.txt","r") as fobj:
                    for i in fobj:
                        b=i.split(";")
                        if b[0]==user_name and b[1]==user_password:
                            a=True
                            return(user_name)
                if a==(False):
                      print("user or password is wrong")
