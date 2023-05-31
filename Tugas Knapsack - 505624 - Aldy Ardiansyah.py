import numpy as np

def max_calories(fruits, totalMoney):
    n = len(fruits)
    maxStocks = np.array([min(fruit['stock'], totalMoney // fruit['price']) for fruit in fruits], dtype=int)
    calories = np.array([fruit['calories'] for fruit in fruits], dtype=int)
    prices = np.array([fruit['price'] for fruit in fruits], dtype=int)

    dp = np.zeros(totalMoney + 1, dtype=int)

    for i in range(n):
        maxStock = maxStocks[i]
        temp = dp.copy()
        for j in range(1, maxStock + 1):
            temp[prices[i] * j:] = np.maximum(temp[prices[i] * j:], dp[:-prices[i] * j] + j * calories[i])
        dp = temp

    return dp[totalMoney]

fruits = [
    {'name': 'apel', 'calories': 91, 'price': 2360, 'stock': 3},
    {'name': 'jeruk', 'calories': 71, 'price': 2120, 'stock': 3},
    {'name': 'pisang', 'calories': 105, 'price': 1890, 'stock': 5},
    {'name': 'kiwi', 'calories': 103, 'price': 3770, 'stock': 10},
    {'name': 'mangga', 'calories': 96, 'price': 2870, 'stock': 5}
]

totalMoney = 25000
result = max_calories(fruits, totalMoney)
print("Jumlah maksimal kalori yang bisa didapatkan oleh Pak Blangkon:", result)
