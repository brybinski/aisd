import math


def numbers(n: int) -> None:
    if n == 0:
        print(0)
        return
    print(n)
    return numbers(n - 1)


def fib(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n - 1) + fib(n - 2)


def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    return number * power(number, n - 1)


def reverse(txt: str) -> str:
    if len(txt) == 0:
        return ""
    return txt[len(txt) - 1] + reverse(txt[0: len(txt) - 1])


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


def prime(n: int, div=-1) -> bool:
    if n <= 1:
        return False
    if div == 1 or n == 2:
        return True

    sqrt: float = math.sqrt(n)

    if div == -1:
        return prime(n, math.ceil(sqrt))

    if n % div == 0:
        return False

    return prime(n, div - 1)


def sum_odd(n: int) -> int:
    if n <= 0:
        return 0
    return n % 10 + sum_odd(int(n / 100))


def sum_even(n: int) -> int:
    return sum_odd(int(n / 10))


def n_sums(n: int, tmp=-1, lst=None) -> list[int]:
    if tmp == -1:
        lst = []
        return n_sums(n, power(10, n) - 1, lst)
    if tmp == power(10, n - 1):
        return lst

    if sum_even(tmp) == sum_odd(tmp):
        lst.append(tmp)

    return n_sums(n, tmp - 1, lst)


def remove_duplicates(txt: str) -> str:
    if txt[0] == txt[-1]:
        return txt[0]
    if txt[0] == txt[1]:
        return remove_duplicates(txt[1:])
    return txt[0] + remove_duplicates(txt[1:])


def n_catalan(n: int) -> int:
    combination: int = int(factorial(2 * n) / (pow(factorial(n), 2)))
    return int((1 / (n + 1)) * combination)


def gen_dyck(n: int, cache=None, i=0, n0=0, n1=0, result=None, count=None):
    if count is None:
        count = n_catalan(n)
    if result is None:
        result = []
    if cache is None:
        cache = [-2] * 2 * n
    if n > n0 > n1 and n > n1:

        # add 0
        cache[i] = 0
        i = i + 1
        n0 = n0 + 1
        gen_dyck(n, cache, i, n0, n1, result, count)
        n0 = n0 - 1
        i += -1

        # add 1
        cache[i] = 1
        i = i + 1
        n1 = n1 + 1
        gen_dyck(n, cache, i, n0, n1, result, count)

    elif (n > n0 == n1 < n) or (n0 < n and n1 == n):
        # add 0
        cache[i] = 0
        i = i + 1
        n0 = n0 + 1
        gen_dyck(n, cache, i, n0, n1, result, count)

    elif n == n0 > n1:
        # add 1
        cache[i] = 1
        i = i + 1
        n1 = n1 + 1
        gen_dyck(n, cache, i, n0, n1, result, count)

    elif n0 == n1 == n:
        res: str = ""
        for itr in cache:
            res += str(itr)
        result.append(res)

    if len(result) == count:
        return result

    return


def balanced_parentheses(n: int) -> str:
    tmp = gen_dyck(int(n/2))
    result: str = ""
    for i in tmp:
        result += str(i) + "\n"
    result = result.replace("0", "(")
    result = result.replace("1", ")")

    return result

n = 16
print(balanced_parentheses(n))
print(n_catalan(n/2))
