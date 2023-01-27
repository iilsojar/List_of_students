import txt_creator


print("Список студентов") 

def main_menu(): 
    print("\nГлавное меню\n") 
    print("1. Показать все записи") 
    print("2. Добавить новую запись") 
    print("3. Искать запись") 
    print("4. Удалить запись")
    print("5. Выход") 

    choice = input("Выберите пункт меню: ") 


    if choice == "1": 
        myfile = open('List_of_students.txt', "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print("нет такой записи") 
        else: 
            print(filecontents) 
        myfile.close 

        enter = input("нажмите enter для продолжения ") 

        main_menu() 
    elif choice == "2": 
        newdata() 
        enter = input("нажмите enter для продолжения ") 

        main_menu() 
    elif choice == "3": 
        searchdata() 
        enter = input("нажмите enter для продолжения ") 

        main_menu() 
    elif choice == "4": 
        deletedata() 
        enter = input("нажмите enter для продолжения ") 

        main_menu() 
    elif choice == "5": 
        print("закончить работу") 
    else: 
        print( "выберите пункт в меню!\n") 
        enter = input( "нажмите enter для продолжения ") 
        main_menu() 
 
     
def searchdata(): 
    searchname = input("введите имя для поиска: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open('List_of_students.txt', "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print("запрашиваемые данные:", end = " ") 
            print(line) 
            found = True 
            break 
    if found == False: 
        print("таких данных нет") 
 
def input_firstname(): 
    first = input("имя ученика: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
def input_lastname(): 
    last = input("фамилия ученика: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
def newdata(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    number_class = input("номер класса ученика: ") 
    age = input("возраст ученика: ") 
    comments = input("комментарий: ") 
    details =("[" + firstname + " " + lastname + ", " + number_class + ", " + comments +  "]\n") 
    myfile = open('List_of_students.txt', "a") 
    myfile.write(details) 
    print("добавленные данные:\n " + details) 

def deletedata():
    with open('List_of_students.txt', "r") as file:
        lines = file.readlines()
        del lines[0]
        with open('List_of_students.txt', "w") as file:
            file.writelines(lines)
            print("удалено") 


main_menu() 
