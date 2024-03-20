from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")

def autodelete(x):
    txt = ".txt"
    filename = x + txt
    secondfile = x + "_date_passed" + txt
    del_line = None
    
    with open(filename, 'r') as fr:
        lines = fr.readlines()
    
    with open(filename, 'w') as fw:
        for line in lines:
            columns = line.strip().split(";")
            if columns[2] != d1:
                fw.write(line)
            else:
                del_line = line
                print("Deleted:", line)

    if del_line:
        with open(secondfile, 'a') as nfw:
            nfw.write(del_line)
