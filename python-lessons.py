number = int(input())
a_word = str(input())
a_number = int(input())
while number > 1:
    acont = 0
    bcont = 0
    b_word = str(input())
    b_number = int(input())
    for i in str(a_number):
        acont += int(i)
    for ii in str(b_number):
        bcont += int(ii)
    if bcont >= acont:
        a_word = b_word
        a_number = b_number
    number -= 1
print(a_word)