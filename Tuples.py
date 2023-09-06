
# task 1

def isValidStudent(my_tuple):
    if type(my_tuple) == tuple:
        if len(my_tuple) == 5:
            if type(my_tuple[0]) == str and type(my_tuple[1]) == str:
                if type(my_tuple[2]) == int and type(my_tuple[3]) == int and type(my_tuple[4]) == int:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_studentlist(my_list):
    if type(my_list) == list:
        for entry in my_list:
            if isValidStudent(my_list) == True:
                return True
            else:
                return False
    else:
        return False




# task 2

def help_fix(my_tuple):
    new = []
    if isValidStudent(my_tuple) == False:
        if type(my_tuple) == tuple:
            for elem in my_tuple:
                new.append(elem)
            for elem in my_tuple:
                if len(new) < 5:
                    new.append(0)

            #print(new)
            if not type(new[0]) == str:
                new[0] = "car"
            if not type(new[1]) == str:
                new[1] = "wash"

            if not type(new[2]) == int:
                new.pop(2)
                new.append(0)
            if not type(new[3]) == int:
                new.pop(3)
                new.append(0)
            if not type(new[4]) == int:
                new.pop(4)
                new.append(0)
            return tuple(new)
        else:
            print("not a tuple")
            return 0
    else:
        print("there is nothing wrong")
        return my_tuple



def fix_studentlist(my_list):
    biglist = []
    if not type(my_list) == list:
        print("not a list")

    for entry in my_list:
        if type(entry) != tuple:
            my_list.remove(entry)
        fixed_entry = help_fix(entry)
        if isValidStudent(fixed_entry) == True:
            biglist.append(fixed_entry)
    return biglist



tupple = ("mint", "charge", "33")
tupling = ("flower", "string", 99, 13, 11)
biglist = [("hi", "mouse", 1, "5", 14), ("wow", "3", "13", 7, 19), ("tree", 111111, 8, 29, 43)]
print(isValidStudent(tupling))
print(is_valid_studentlist(biglist))
print(help_fix(tupple))
print(fix_studentlist(biglist))
# assert(is_valid_studentlist(fix_studentlist(studentGrades)) == True)
# no grades here