def hanoi_helpers(disque, start, intermediate, final):
    if disque == 1:
        print(f"Déplacer un disque du pilier {str(start)} vers le pilier {str(final)}")
    else:
        hanoi_helpers(disque-1, start, final, intermediate)
        print(f"Déplacer un disque du pilier {str(start)} vers le pilier {str(final)}")
        hanoi_helpers(disque-1, intermediate, start, final)

def hanoi(n: int) -> int:
    hanoi_helpers(n, 1, 2, 3)

if __name__ == "__main__":
    hanoi(4)