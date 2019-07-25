from stack import Stack

def decimal2binary(deci_num):
    s = Stack(100)

    while deci_num > 0:
        remainder = deci_num % 2
        s.push(remainder)
        deci_num = deci_num // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num
