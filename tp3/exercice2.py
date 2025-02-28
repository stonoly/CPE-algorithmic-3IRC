import time

def fibonacci1(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    
def fibonacci2(n: int, memory: list={}) -> int:
    if n in memory:
        return memory[n]
    
    if n == 0 or n == 1:
        return 1
    
    memory[n] = fibonacci2(n-1) + fibonacci2(n-2)
    return memory[n]

def fibonacci3(n, a=1, b=1):
    if n == 0:
        return a
    else:
        return fibonacci3(n-1, b, a+b)
    

if __name__ == "__main__":
    value = 5
    result3 = fibonacci3(value)
    result1 = fibonacci1(value)
    print('------')
    print(f'Résultat de Fibonacci1 de {value} = {result1}')
    print(f'Résultat de Fibonacci3 de {value} = {result3}')


    list_test = [5, 10, 20, 30, 40]

    print('---------------------')
    for i in range (len(list_test)):
        start = time.time()
        fibonacci1(list_test[i])
        stop = time.time()
        print(f'Time: Fibonacci1({str(list_test[i])})', stop - start) 

    print('---------------------')
    for i in range (len(list_test)):
        start = time.time()
        fibonacci2(list_test[i])
        stop = time.time()
        print(f'Time: Fibonacci2({str(list_test[i])})', stop - start) 

    print('---------------------')
    for i in range (len(list_test)):
        start = time.time()
        fibonacci3(list_test[i])
        stop = time.time()
        print(f'Time: Fibonacci3({str(list_test[i])})', stop - start)