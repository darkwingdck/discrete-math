def request_program():
    print('Select program:\n1. Number to bit scale')
    program_num = int(input('>> '))
    return program_num

def bit_scale():
    number = int(input('Number: '))
    res = ''
    while number > 0:
        res = str(number % 2) + res
        number //= 2
    print('Number in bit scale: ' + res)

def main():
    program_num = request_program()
    if program_num == 1:
        bit_scale()

if __name__ == '__main__':
    main()