result = []
for count in range(1, 31):
    if count % 3 == 0 and count % 5 == 0: 
        result.append("FizzBuzz")
    elif count % 5 == 0:
        result.append("Buzz")
    elif count % 3 == 0:
        result.append("Fuzz")
    else :
        result.append(count)
print(result)
