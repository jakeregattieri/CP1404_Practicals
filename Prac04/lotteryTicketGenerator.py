import random


def main():
    quick_picks = int(input("how many quick picks? "))
    for numbers in range(quick_picks):
        lottery_numbers = []
        for number in range(6):
            random_number = random.randint(1,45)
            while random_number in lottery_numbers:
                random_number = random.randint(1, 45)
            lottery_numbers.append(random_number)
        lottery_numbers.sort()
        for number in lottery_numbers:
            print("{:<4}".format(number), end='')
        print()


main()