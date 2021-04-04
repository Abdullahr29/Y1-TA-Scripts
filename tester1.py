def missing_char(stri, n):
    stri = list(stri)
    del stri[n]
    return stri


l = missing_char('hello123456', 1)
str1 = ''.join(l)
print(str1)
