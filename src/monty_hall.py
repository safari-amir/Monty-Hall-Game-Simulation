import random


doors = ['car'] + ['goat'] + ['goat']
def monty_hall_game(switch_doors, n):
    true_choice = 0
    for _ in range(n):
        random.shuffle(doors)
        initial_choice = random.choice(doors)
        if switch_doors:
            if initial_choice == 'goat':
                true_choice += 1
        else:
            if initial_choice == 'car':
                true_choice += 1

    probability_of_succese = true_choice / n


    return probability_of_succese


if __name__ == '__main__':
    n = 100
    monty_hall_game(True, n)