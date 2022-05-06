def request_program():
    print('Select program:\n1. Number to bit scale\n2. Set operations')
    program_num = int(input('>> '))
    return program_num


def bit_scale(array):
    ans = []
    for i in range(1, max(array) + 1):
        ans.append(1 if i in array else 0)
    return ans


class Operation:
    def choose_operation(self):
        print("\tSelect operation:\n\t1. Union\n\t2. Intersection\n\t3. Сomplementation\n\t4. Difference")
        operation_num = int(input("\t>> "))
        array1 = [int(i) for i in input("\tEnter first set\n\t>>").split()]
        array2 = [int(i) for i in input("\tEnter second set\n\t>>").split()]
        bit_array1 = bit_scale(array1)
        bit_array2 = bit_scale(array2)
        if len(bit_array1) < len(bit_array2):
            bit_array1.extend([0] * (len(bit_array2) - len(bit_array1)))
        elif len(bit_array1) > len(bit_array2):
            bit_array2.extend([0] * (len(bit_array1) - len(bit_array2)))
        if operation_num == 1:
            return self.union(bit_array1, bit_array2)
        elif operation_num == 2:
            return self.intersection(bit_array1, bit_array2)

    @staticmethod
    def union(bit_array1, bit_array2):
        bit_ans = []
        ans = []
        for i in range(len(bit_array1)):
            bit_ans.append(bit_array1[i] or bit_array2[i])
        for i in range(len(bit_ans)):
            if bit_ans[i] == 1:
                ans.append(i+1)
        return ans

    @staticmethod
    def intersection(bit_array1, bit_array2):
        bit_ans = []
        ans = []
        for i in range(len(bit_array1)):
            bit_ans.append(bit_array1[i] and bit_array2[i])
        for i in range(len(bit_ans)):
            if bit_ans[i] == 1:
                ans.append(i+1)
        return ans


def set_operations():
    operation = Operation()
    return operation.choose_operation()


def main():
    program_num = request_program()
    if program_num == 1:
        array = [int(i) for i in input("Enter set\n>>").split()]
        print(bit_scale(array))
    elif program_num == 2:
        print(set_operations())


if __name__ == "__main__":
    main()
