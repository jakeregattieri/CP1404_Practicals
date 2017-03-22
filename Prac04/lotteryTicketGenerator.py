import random


def main():
    quick_picks = int(input("how many quick picks? "))
    for numbers in range(quick_picks):
        lottery_numbers = []
        for number in range(6):
            random_number = random.randint(1,45)
            if random_number in lottery_numbers:
                print(random_number)
                lottery_numbers.pop()
            lottery_numbers.append(random_number)
            lottery_numbers.sort()
        new_lottery_numbers = [str(number) for number in lottery_numbers]
        new_lottery_numbers = ' '.join(new_lottery_numbers)
        print("{}".format(new_lottery_numbers))


main()
