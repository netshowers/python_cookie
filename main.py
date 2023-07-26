# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# multiple.sequences.py
people = ['Nick', 'Rick', 'Roger', 'Syd', 'Peter']
ages = [23, 24, 23, 21, 27]
sexes = ['Male', 'Male', 'Female', 'Male', 'Male']
# for position in range(len(people)):
#     person = people[position]
#     age = ages[position]
#     sex = sexes[position]
#     print(person, age, sex)
# for person, age, sex in zip(people, ages, sexes):
#   print(person, age, sex)
# data = list(zip(people, ages, sexes))
# data.sort()
# print(data)
strs = ['fight', 'fish', 'finish', 'fix']
t = strs[0]
for s in strs:
    while not s.startswith(t):
        if len(t) == 0:
            print("")
        else:
            t = t[:-1]
print(t)


def tryconvert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


lst = ['3', '7', 'foo', 'A.B', '2.6', 'bar', '8.9']
newlst = [tryconvert(i) for i in lst]
print(newlst)
# for number in range(5):
#     print(number)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
