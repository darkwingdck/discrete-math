def request_program():
    print('Select program:\n1. Number to bit scale\n2. Set operations')
    program_num = int(input('>> '))
    return program_num

def bit_scale():
    number = int(input('Number: '))
    res = ''
    while number > 0:
        res = str(number % 2) + res
        number //= 2
    print('Number in bit scale: ' + res)

def set_operations():
    pass

def main():
    program_num = request_program()
    if program_num == 1:
        bit_scale()
    elif program_num == 2:
        set_operations()

if __name__ == '__main__':
    main()