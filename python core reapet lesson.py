#For-loop

"""""

ism = ['Max', 'Jack', 'Jamal']

for x in ism:
    print(f'Hello, {x}')
print(f'Kod {len(ism)} marta takrorlandi')

for y in range(9, 100, 2):
    print(f'{y}ning kubi {y**3}')

ism = []
for x in range(1, 6):
    a = input('Beshta kino: ')
    ism.append(a)
print(ism)

ismlar = []
a = int(input('nechta odam bilan uchrashdiz: '))
for x in range(1, a+1):
    b = input(f'{x}-odam: ')
    ismlar.append(b)
print(f'Siz uchrashgan odamlar:{ismlar}')

"""

#IF/ELSE

"""""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for x in cars:
    if 'gm' == x:
         print(x.upper())
    elif 'gm' != x:
        print(x.title())

a = input('Username: ')
if a.lower() == 'admin':
    print("Xush kelibsiz admin, list tekshirilsinmi?")
else:
    print(f"Xush kelibsiz, {a}")


a = int(input('Birinchi son: '))
b = int(input('Ikkinchi son: '))
if a==b:
    print('Sonlar teng')
else:
    print('Sonlar teng emas')


a = int(input('Son kiriting: '))
if a >= 0:
    print(f'Bu sonning kvadrati {a**2} ga teng')
else:
    print(f'musbat son kiritng!')

"""

#Dictionary

"""""

Men = {
    'ism':'Mirjalol',
    'familiya':'Xudoyberdiyev',
    't_sana':'1-iyul 2005-yil',
}

print(f"Mening ism-familiyam {Men['ism']} {Men['familiya']}, {Men['t_sana']}da tug'ilganman")


sevimli_taomlar = {
        'Dadam':'Osh',
        'Onam':"Manti",
        'Ukam':"Somsa"
    }
print(f'Dadamning sevimli toami {sevimli_taomlar['Dadam'].lower()}, onamniki esa {sevimli_taomlar['Onam'].lower()} va ukamniki esa {sevimli_taomlar['Ukam'].lower()}')



Dictionary = {
    'apple':'olma',
    'ramdom':'rtasodifiy',
    'pen':'ruchka',
    'bag':'sumka',
    'reaserch':'tadqiqot'
}

a = input("Birorta inglizcha so'z kiriting: ")
b = Dictionary.get(a)
if a.lower() in Dictionary:
    print(f'{a.lower()} = {b}')
else:
    print("Bu so'z mavjud emas!")


car0 = {
    'model':'Bmw m4',
    'yili':'2024',
    'narxi':'$78000',
    'km':10000
}

car1 = {
    'model': 'Porsche Cayyenne',
    'yili': '2021',
    'narxi': '$64000',
    'km': 40000
}

ccar2 = {
    'model': 'Mercedes S class',
    'yili': '2023',
    'narxi': '$92000',
    'km': 43000
}

cars = [car0, car1, ccar2]
for car in cars:
    print(f"Model: {car['model']}, "
          f"Yili: {car['yili']}, "
          f"Narxi: {car['narxi']}, "
          f"Km: {car['km']} ")

"""

#Funksiya


"""""
def yosh_hisoblash(yosh):
    print(f"Siz {2025-yosh}-yilda tug'ilgansiz")


yosh_hisoblash(18)


def hisoblash(son):
    print(f"Kvadrati: {son**2}, kubi: {son**3}ga teng")

hisoblash(12)
hisoblash(3)
hisoblash(-4)


def hisob(son):
    if son % 2 == 0:
        print(f'juft son')
    else:
        print(f'toq son')


hisob(3)
hisob(6)


def ismlar(ism):
    for x in ism:
        print(x)

ismlar(["Ali", 'Murod', 'Jasur'])

def numbers(*number):
    for x in number:
     print(x * 5)


numbers(2, 3, 4)

"""
#Object/Classes

"""

class Student:
    def __init__(self, name, sure_name, birthyear):
        self.name = name
        self.sure_name = sure_name
        self.birthyear = birthyear
    def information(self):
        print(f'Name: {self.name}, Sure_name: {self.sure_name}, Birthyear: {self.birthyear}')


student1 = Student('Jack', 'Black', 2005)
student2 = Student('Micheal', "Barret", 2000)

student2.information()
student1.information()

"""