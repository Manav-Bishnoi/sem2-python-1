from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")

def add_task(x):
    txt=".txt"
    filename=(x+txt)
    with open(filename,"a") as fobj:
            task_to_be_done=input("enter the task here")
            fdate=input("date till task must be done")
            fobj.write(task_to_be_done)
            fobj.write(";")
            fobj.write(d1)
            fobj.write(";")
            fobj.write(fdate)
            fobj.write("\n")
    # y=input("Type 1 if you want to add another task")
    # if y==1:
    #     add_task(x)

def show_tasks(x):  
    txt=".txt"
    filename=x+txt
    with open(filename,'r') as fobj:
        count=1
        for i in fobj:
            a=i.split(";")
            print(count," \ntask= ",a[0], "\ninitial date= ", a[1], "\nfinal date= ", a[2])
            count=count+1

def delete_task(x):
    txt=".txt"
    filename=(x+txt)
    secondfile=(x+"done"+txt)
    a=int(input("which line to delete"))
    del_line=None
    #to learn and undestand
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        ptr = 1
        with open(filename, 'w') as fw:
            for line in lines:
                if ptr != a:
                    fw.write(line)
                else:
                    del_line=line
                ptr += 1
        with open(secondfile, 'a') as nfw:
            if del_line!=None:
                line.strip()
                nfw.write(line+";"+d1+"\n")
                print("Deleted")
            else:
                print("Task not found")

def show_done_tasks(x):
    txt=".txt"
    secondfile=(x+"done"+txt)
    with open(secondfile,'r') as fobj:
        count=1
        for i in fobj:
            a=i.split(";")
            print(count," \ntask= ",a[0], "\ninitial date= ", a[1], "\nfinal date= ", a[2], "\ntask done date= ", a[3])
            count=count+1