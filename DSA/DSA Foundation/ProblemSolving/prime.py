number1 = int(input())

# Edge cases
if number1 <= 1:  # 1 and negative numbers are not prime
    print("Nay")
elif number1 == 2:  # 2 is the only even prime number
    print("Yay")
else:
    returnvalue = "Yay"
    counter = 0
    for y in range(2, int(number1**0.5) + 1):
        if number1 % y == 0:
            counter += 1
            returnvalue = "Nay"
            if counter > 2:
                break
    print(returnvalue)