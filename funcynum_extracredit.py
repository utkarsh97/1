if __name__ == '__main__': #Extra Credit
    def horizontal_line(a, b, c):
        d = b + c
        e = format(str(a) * b, '>' + str(d))
        return e

    def vertical_line(a, b, c):
        d = c + 1
        e = ''
        for i in range(1, b + 1):
            if i == b:
                e = e + format(a, '>' + str(d))
            else:
                e = e + format(a, '>' + str(d)) + '\n'
        return e

    def vertical_lines(a, b, c, d, e):
        horizontal = ''
        vertical = ''
        for num in range(1, d + 1):
            horizontal = horizontal + a + ' ' * e 
        for i in range(1, b + 1):
            if i == b:
                vertical += ' ' * c + horizontal
            else:
                vertical += ' ' * c + horizontal + '\n'
        return vertical

    def print_zero(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_lines(a, 3, 0, 2, b - 2))
        print(horizontal_line(a, b, 0))

    def print_one(a, b):
        if b < 3:
            b = 3
        print(vertical_line(a, b, b - 1))

    def print_two(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, b - 1))
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, 0))
        print(horizontal_line(a, b, 0))

    def print_three(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, b - 1))
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, b - 1))
        print(horizontal_line(a, b, 0))

    def print_four(a, b):
        if b < 3:
            b = 3
        print(vertical_lines(a, 2, 0, 2, b - 2))
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 2, b - 1))
   
    def print_five(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, 0))
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, b - 1))
        print(horizontal_line(a, b, 0))
    
    def print_six(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 1, 0))
        print(horizontal_line(a, b, 0))
        print(vertical_lines(a, 1, 0, 2, b - 2))
        print(horizontal_line(a, b, 0))

    def print_seven(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 4, b - 1))

    def print_eight(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_lines(a, 1, 0, 2, b - 2))
        print(horizontal_line(a, b, 0))
        print(vertical_lines(a, 1, 0, 2, b - 2))
        print(horizontal_line(a, b, 0))

    def print_nine(a, b):
        if b < 3:
            b = 3
        print(horizontal_line(a, b, 0))
        print(vertical_lines(a, 1, 0, 2, b - 2))
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 2, b - 1))

    def print_plus(a, b):
        if b < 3:
            b = 3
        c = int((b+1)/2)
        print(vertical_line(a, 2, c - 1))
        print(horizontal_line(a, b, 0))
        print(vertical_line(a, 2, c - 1))

    def print_minus(a, b):
        if b < 3:
            b = 3
        print()
        print()
        print(horizontal_line(a, b, 0))
        print()
        print()
    
    def print_multiply(a, b): #Extra Credit
        if b < 5:
            b = 5
        c = int((b+1)/2)
        d = int((b - 3)/2)
        print(vertical_lines(a, 1, 0, 2, b - 2))
        print(vertical_lines(a, 1, d, 2, d))
        print(vertical_line(a, 1, c - 1))
        print(vertical_lines(a, 1, d, 2, d))
        print(vertical_lines(a, 1, 0, 2, b - 2))

    def check_answer(a, b, c, d):
        if d == '+':
            e = a + b
            if e == c:
                return "True"
            else:
                return "False"
        elif d == '-':
            e = a - b
            if e == c:
                return "True"
            else:
                return "False"
        elif d == '*' or d == 'x' or d == 'X': #Extra Credit
            e = a * b
            if e == c:
                return "True"
            else:
                return "False"
        else:
            return "Incorrect Operand"
