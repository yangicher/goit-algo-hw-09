import timeit

COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> dict:
    result = {}
    for coin in COINS:
        if amount <= 0:
            break
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount: int) -> dict:

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    last_coin = [None] * (amount + 1)

    for a in range(1, amount + 1):
        for coin in COINS:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                last_coin[a] = coin

    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

def write_conclusion(file, total, dyn_res, grd_res, dyn_time, greedy_time):
    # Write header and comparison
    file.write(f"\n\n# Comparison dynamic func and greedy func for {total} \n\n")
    
    # Write table header
    file.write("| Algorithm |     Result       | Time (seconds)|\n")
    file.write("|-----------|------------------|---------------|\n")
    
    # Write algorithm results
    file.write(f"|Dynamic func|{dyn_res}|{dyn_time:.6f}|\n")
    file.write(f"|Greedy func|{grd_res}|{greedy_time:.6f}|\n")
    
    # Compare execution times
    if dyn_time < greedy_time:
        file.write("\n# Dynamic faster than greedy \n")
        time_diff = greedy_time - dyn_time
        speedup = (greedy_time / dyn_time) if dyn_time > 0 else float('inf')
        file.write(f"Dynamic programming is faster by {time_diff:.6f} seconds\n")
        file.write(f"Speed-up factor: {speedup:.2f}x\n")
    else:
        file.write("\n# Greedy faster than dynamic \n")
        time_diff = dyn_time - greedy_time
        speedup = (dyn_time / greedy_time) if greedy_time > 0 else float('inf')
        file.write(f"Greedy algorithm is faster by {time_diff:.6f} seconds\n")
        file.write(f"Speed-up factor: {speedup:.2f}x\n")

    # Compare results
    file.write("\n## Conclusions\n")
    if dyn_res == grd_res:
        file.write("- Both algorithms found the same result\n")
    else:
        file.write("- Algorithms found different results\n")
        diff = abs(dyn_res - grd_res)
        file.write(f"- Difference in results: {diff}\n")
    
    # Write overall recommendation
    file.write("\n### Recommendation\n")
    if dyn_time < greedy_time and dyn_res.items() >= grd_res.items():
        file.write("Use dynamic programming approach (faster and better/equal result)")
    elif greedy_time < dyn_time and grd_res.items() >= dyn_res.items():
        file.write("Use greedy approach (faster and better/equal result)")
    else:
        file.write("Trade-off between speed and accuracy - choose based on requirements")        

with open("README.md", "w", encoding="utf-8") as file:
    total = 12
    write_conclusion(file, total, find_min_coins(total), find_coins_greedy(total), timeit.timeit(lambda: find_min_coins(total), number=1), timeit.timeit(lambda: find_coins_greedy(total), number=1))
    total = 123
    write_conclusion(file, total, find_min_coins(total), find_coins_greedy(total), timeit.timeit(lambda: find_min_coins(total), number=1), timeit.timeit(lambda: find_coins_greedy(total), number=1))
    total = 1023
    write_conclusion(file, total, find_min_coins(total), find_coins_greedy(total), timeit.timeit(lambda: find_min_coins(total), number=1), timeit.timeit(lambda: find_coins_greedy(total), number=1))
    total = 10123
    write_conclusion(file, total, find_min_coins(total), find_coins_greedy(total), timeit.timeit(lambda: find_min_coins(total), number=1), timeit.timeit(lambda: find_coins_greedy(total), number=1))
