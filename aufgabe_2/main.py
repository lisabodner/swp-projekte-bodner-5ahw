import random
import matplotlib.pyplot as plt
from collections import Counter

def draw_six_lotto_nums():
    lotto_nums = []
    for i in range(1, 46):
        lotto_nums.append(i)

    lotto_results = []
    for i in range(0, 6):
        rnd_num = random.randint(0, 44-i)
        lotto_results.append(lotto_nums[rnd_num])
        value = lotto_nums[rnd_num]
        new_value = lotto_nums[44-i]
        lotto_nums[44-i] = value
        lotto_nums[rnd_num] = new_value
    return lotto_results

if __name__ == '__main__':
    counts = Counter()
    for i in range(0, 1000000):
        draw = draw_six_lotto_nums()
        counts.update(draw)

    numbers = list(range(1, 46))
    frequencies = [counts[num] for num in numbers]

    plt.figure(figsize=(14, 6))
    plt.bar(numbers, frequencies, color='skyblue', edgecolor='black')

    plt.title(f'distribution after 1000000 draws')
    plt.xlabel('number')
    plt.ylabel('count')
    plt.xticks(numbers)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()