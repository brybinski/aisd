from typing import Callable
from typing import Tuple

print('hello world')


# noinspection SpellCheckingInspection
def ex1(name: str, surname: str) -> str:
    stri = name[0] + "." + surname
    return stri


print(ex1("j", "kowalski"))


def ex2(name: str, surname: str) -> str:
    result: str = name[0].upper()
    result += "."
    result += surname[0].upper()
    result += surname[1:].lower()
    return result


print(ex2("jan", "kowalski"))


def ex3(first: int, second: int, age: int) -> int:
    return first * 100 + second - age


print(ex3(20, 21, 21))


def ex4(name: str, surname: str, foo: Callable) -> str:
    return foo(name, surname)


print(ex4("jae", "kowalski", ex2))


# noinspection SpellCheckingInspection
def ex5(divident: int, dividor: int):
    if divident >= 0 and dividor > 0:
        return divident / dividor


print(ex5(8, 2))

# ex6
#
# a: int = 0;
# lst: List[int] = []
#
# while a < 100:
#     tmp: int = 0
#     tmp = int(input("Add a number: "))
#     a += tmp
#     lst.append(tmp)
#
#
# # ex7
#
#
# def listtotuple(lst: List) -> Tuple:
#     tup: Tuple = tuple(lst)
#
#     return tup
#
#
# # ex8
# print(listtotuple(lst))


# ex9
def week(day: int) -> str:
    tup: Tuple = ('niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota')
    return tup[abs(day % 7)]


print(week(7))


# ex10

def palindrome(text: str) -> bool:
    tmp: str = text.lower()

    if tmp == tmp[::-1]:
        return True
    return False


print(palindrome("kajak"))
