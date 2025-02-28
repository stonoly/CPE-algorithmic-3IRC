def recursive_increase(n: int) -> None:
    if n == 1:
        print(n)
    else:
        recursive_increase(n-1)
        print(n)

def recursive_decrease(n: int) -> None:
    if n == 1:
        print(n)
    else:
        print(n)
        recursive_decrease(n - 1)
    




if __name__ == "__main__":
    recursive_increase(8)
    print("------")
    recursive_decrease(8)