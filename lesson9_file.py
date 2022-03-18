# Problem 1
"""
with open('/home/adiko/Рабочий стол/directories.txt', 'r') as all_files:
    print(all_files.read())
"""

# Problem 2
"""
with open('users.txt', 'a') as info_user:
    login = input('Text your login: ')
    password = input('Text your password: ')
    info_user.writelines(f'login: {login}\nPassword: {password}')
"""

# Problem 3
"""
with open('find_letter.txt', 'a') as find_w:
    find_w.writelines('The weather was very good!')

with open('find_letter.txt', 'r') as find_w:
    info = find_w.read()
    if 'w' in info:
        print("The letter w have in file")
    else:
        print("The letter w doesn't have in file")
"""

# Problem 4
"""
info_python = '''Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java'''

with open('python.txt', 'rw+') as file:
    file.write(info_python)


t_words = []
with open('python.txt', 'r') as file:
    info = file.read().split()
    for i in info:
        if 't' in i:
            t_words.append(i)
print(t_words)
"""

# Problem 1
"""
with open('database.txt', 'a') as f1:
    f1.write(f'''
Login: telephone@gmail.com
password: smart1234

Login: Computer@gmail.com
password: comp54321

Login: Iphone@gmail.com
password: iphone15

''')

with open('database.txt', 'r') as f2:
    infile = f2.read()
    while True:
        login = input('Your login: ')
        password = input('Your password: ')
        if login not in infile:
            while True:
                second_pass = input('Repeat password: ')
                if second_pass == password:
                    break
                else:
                    print('Пароль должен совпадать!')
            break
        else:
            print('Такой логин уже существует!\nПовторите ещё раз :)')
with open('database.txt', 'a') as f3:
    f3.write(f'Login: {login}\npassword: {password}')

"""

# Problem 2
"""
login = input('Your login >>> ')
password = input('Your password >>> ')
photo = input('Your photo >>> ').split('.')
way_photo = '/home/adiko/OWN/Python/ITCBOOTCAMP/lesson9_workfile/моргенштерн.png'
if photo[0] in way_photo and photo[1] in 'jpeg,jpg,png':
    with open('user_info.txt', 'a') as userfile:
        userfile.write(f'login: {login}\npassword: {password}\nphoto: {".".join(photo)}')
    print('Регистрация успешно!')
"""

# Problem 1
"""
need_change = input('Путь до картинки которую нужно изменить >>> ')
need_to_change = input('Путь до картинки НА которую нужно изменить >>> ')
first_way = '/home/adiko/OWN/Python/ITCBOOTCAMP/lesson9_workfile/моргенштерн.png'
second_way = '/home/adiko/Загрузки/iphone-13.png'
if need_change == first_way and need_to_change == second_way:
    first_way, second_way = second_way, first_way
else:
    print('Tакой картинке не существует')
"""

# Problem 2
month_pay = '''
January       18000
February      32641
March         28300
April         11200
May           21100
June          19000
July          8000
August        72000
September     12300
October       17000
November      25000
December      30000
'''

with open('month_money', 'w') as file1:
    file1.write(month_pay)

# Май, Июль, Сентябрь и Ноябрь

with open('month_money', 'r') as file2:
    info = file2.read().split('\n')
    for i in info:
        if 'May' in i:
            may = ''
            for j in i:
                if j.isdigit():
                    may += j
        elif 'July' in i:
            july = ''
            for j in i:
                if j.isdigit():
                    july += j
        elif 'September' in i:
            september = ''
            for j in i:
                if j.isdigit():
                    september += j

        elif 'November' in i:
            november = ''
            for j in i:
                if j.isdigit():
                    november += j
print(f'({may} + {may} + {may} + {may}) / 4 = {(int(may) + int(july) + int(september) + int(november)) / 4}')
