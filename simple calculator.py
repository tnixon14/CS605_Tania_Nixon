print('~~~~~ Simple Calculator ~~~~~')
print('Select an operation:')
print('+: Addition')
print('-: Subtract')
print('*: Multiplication')
print('/: Division')

while True:
    #take operation input from user
    op = input("Enter operation: (+, - , * , /) ")

    #check if input is a valid operation
    if op in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("ERROR: INVALID INPUT! Please enter a number.")
            continue

        if op == '+':
            num_add = num1 + num2
            print('Result:', num1, '+', num2, '=', num_add)

        elif op == '-':
            num_sub = num1 - num2
            print('Result:',num1, '-', num2, '=', num_sub)

        elif op == '*':
            num_multi = num1 * num2
            print('Result:',num1, '*', num2, '=', num_multi)

        elif op == '/':
            if num2 != 0:
                num_div = num1 / num2
                print('Result:',num1, '/', num2, '=', num_div)
            elif num1 == 0 and num2 == 0:
                print('ERROR: Undefined')
                print('-' * 40)
            elif num1 != 0 and num2 == 0:
                print('ERROR: Zero as a divisor is not allowed.')
                print('-' * 40)

        #check if user wants another calculation, use "break" if no
        conti = input('Do you want to continue with another calculation? (YES/NO):').strip().upper()
        #strip() removes trailing or leading the string (aimed for unintentional spaces)
        #upper() turn entry into uppercase no or yes
        if conti == 'NO':
            break
    else:
        print('ERROR: INVALID INPUT! Please enter "YES" or "NO".')
