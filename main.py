
print('hello world')


def ex1(name: str, surname: str) -> str:
    str = name[0] + "." + surname
    return str


print(ex1("j", "kowalski"))


def ex2(name: str, surname: str) -> str:
    result: str = name[0].upper()
    result += "."
    result += surname[0].upper()
    result += surname[1:].lower()
    return result


print(ex2("jan", "kowalski"))


def ex3(first: int, second: int, age: int ) -> int:
    return first*100+second-age


print(ex3(20,21, 21))


def ex4(name: str, surname: str, foo):
    return foo(name, surname)


print(ex4("jae", "kowalski", ex2))

