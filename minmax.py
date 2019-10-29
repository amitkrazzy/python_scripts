def minmax(digits):
    max = digits[0]
    min = digits[0]

    for d in digits:
        if d > max:
            max = d
        if d < min:
            min = d
    result = (min, max)

    return result

digits = input('Enter integers seperated by space: ')
digits = [int(i) for i in digits.split()] #conveting string into list of integers

print(minmax(digits))
