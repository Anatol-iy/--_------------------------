import random

def simulate_dice_rolls(num_rolls):
    # Створюємо словник для підрахунку кожної можливої суми
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        # Кидаємо два кубики
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        # Визначаємо суму чисел на обох кубиках
        dice_sum = dice1 + dice2
        
        # Підраховуємо кількість випадків кожної суми
        sum_counts[dice_sum] += 1
    
    # Обчислюємо ймовірність кожної суми
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    
    return probabilities

# Теоретичні ймовірності для кожної суми
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Кількість спостережень
num_rolls_list = [100, 1000, 10000, 100000]

# Заголовок таблиці
print(f"{'Кількість спостережень':<25} {'Сума':<8} {'Імовірність (Монте-Карло, %)':>30} {'Імовірність (аналітичні розрахунки, %)':>40} {'Абсолютна похибка':>25} {'Різниця (%)':>20}")
print("-" * 155)

# Симуляція для кожної кількості спостережень
for num_rolls in num_rolls_list:
    probabilities = simulate_dice_rolls(num_rolls)
    for sum_value in range(2, 13):
        monte_carlo_probability = probabilities[sum_value] * 100
        theoretical_probability = theoretical_probabilities[sum_value] * 100
        absolute_error = abs(monte_carlo_probability - theoretical_probability)
        difference_percentage = (absolute_error / theoretical_probability) * 100
        print(f"{num_rolls:<25} {sum_value:<8} {monte_carlo_probability:>30.3f} {theoretical_probability:>40.2f} {absolute_error:>25.3f} {difference_percentage:>20.2f}")
    print("-" * 155)
