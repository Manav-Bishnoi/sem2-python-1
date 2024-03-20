from Modulefile import tasks, users,auto

user=int(input("1. for add new user, 2. for finding user"))
if(user==1):
    users.new_user()
elif(user==2):
    username=users.find_user()
    if username!=None:
        auto.autodelete(username)
        what_to_do=int(input("1. for add task, 2. for show tasks, 3. for task done, 4.show_done_tasks"))
        match what_to_do:
            case 1:
                tasks.add_task(username)
                tasks.show_tasks(username)
            case 2:
                tasks.show_tasks(username)
            case 3:
                tasks.show_tasks(username)
                tasks.delete_task(username)
            case 4:
                tasks.show_done_tasks(username)
