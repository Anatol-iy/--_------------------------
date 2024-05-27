items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за зменшенням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    
    # Створюємо DP таблицю
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Визначення обраних страв
    res = dp[n][budget]
    w = budget
    selected_items = []
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected_items.append(names[i - 1])
            res -= calories[i - 1]
            w -= costs[i - 1]
    
    return selected_items, dp[n][budget]

# Приклад використання:
budget = 100

# Жадібний алгоритм
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: обрані страви {greedy_result}, сумарна калорійність {greedy_calories}")

# Алгоритм динамічного програмування
dp_result, dp_calories = dynamic_programming(items, budget)
print(f"Динамічне програмування: обрані страви {dp_result}, сумарна калорійність {dp_calories}")
