def fib(num):

    while True:

        try:

            if type(num) != int or num < 0:
                raise ValueError

            p = 0 # previous
            n = 1 # next
            
            if num == 0 or num == 1:
                return 'Este valor pertence à sequência Fibonacci!'

            while n < num:

                t = n
                n = p + n
                p = t

                if n == num:
                    return 'Este valor pertence à sequência Fibonacci!'
                elif n > num:
                    return 'Este valor não pertence à sequência Fibonacci!'

        except ValueError:
            return 'Insira um valor numérico maior ou igual a 0!'

test = fib(8)
print(test)
