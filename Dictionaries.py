
# task 1

test_students = [['David', 1234], ['Melanie', 4567], ['Apricat', 1111], ['Cleocatra', 2222], ['Melanie', 4567]]

def list_2_set(my_list):
    new = []
    for entry in my_list:
        entry = tuple(entry)
        if entry in new:
            continue
        else:
            new.append(entry)
    return set(new)

print(list_2_set(test_students))
#test_set = set(test_students)
#print(test_set)

td = dict(test_students)
print(td, 'with keys', td.keys(), 'and values', td.values())

# keys = student ID
# student entry = value
# [key, value]
# [1234, David]

def list_2_dict(my_list):
    students = {}
    for student in my_list:
        key = student[1]
        if student[1] in students.keys():
            pass
        else:
            students[key] = student[0]

    return students

print(list_2_dict(test_students))

rem_dupe = [1, 2, 2, 2, 2, 1, 2]
rem_set = set(rem_dupe)
print(rem_dupe)
print(rem_set)

# task 2
count_num = [1, 2, 3, 2, 4, 5, 2, 3, 2, 5]

# counter to determine how many times one iterator has been seen
# how to check if it was already counted?
# output number as key and counter as value
def repeat_count(num_list):
    num_dict = {}
    for elem in num_list:
        key = elem
        if key in num_dict.keys():
            pass
        else:
            num_dict[key] = num_list.count(elem)
    return num_dict

print(repeat_count(count_num))


# task 3

# question:
# print all letters of a tuple of lists except for vowels
# exclude spaces
# output should be one long word of consonants

my_sent = (["my boyfriend"], ["is the"], ["coolest"])

# possible solution
def no_vowels(my_tuple):
    # initialize new list to rid of split data types
    vowelless = []
    # identify unwanted letters
    vowels = ("a", "e", "i", "o", "u", " ")
    for entry in my_tuple: # ["my boyfriend"]
        for word in entry: # "my boyfriend"
            for letter in word: # m
                if letter in vowels: # "a", "e", "i", "o", "u", " "
                    continue
                else:
                    # add consonants to new list as separate strings
                    vowelless.append(letter)
    # returns list without spacing, creates giant word
    return "".join(vowelless)

print(no_vowels(my_sent))

