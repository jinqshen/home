def is_palindrome(n):
    a = abs(n)
    c = 0
    while a > 0:
        p = a % 10
        a = int(a / 10)
        c = c * 10 + p
    if n > 0:
        return c == n
    else:
        return c == -n

out = filter(is_palindrome, range(-200, 0))
print(list(out))
