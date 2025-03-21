def print_hanoi(starting_pillar, arrival_pillar):
    print(f"Déplacer un disque du pilier {str(starting_pillar)} vers le pilier {str(arrival_pillar)}")

def hanoi(n: int) -> int:
    if n == 0:
        return 0
    print_hanoi(1, 2)
    return hanoi(n-1)

if __name__ == "__main__":
    hanoi(3)