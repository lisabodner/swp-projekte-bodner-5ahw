import random

rnd_list = [random.randint(1, 100) for _ in range(6)]
list_rating = ["over 50" if p >= 50 else "under 50" for p in rnd_list]

print("list:", rnd_list)
print("rating:", list_rating)

rnd_temp = [random.randint(-5, 35) for _ in range(8)]
temp_set = {"warm" if t > 20 else "cold" for t in rnd_temp}

print("temp values:", rnd_temp)
print("temp rating:", temp_set)

products = ["phones", "laptops", "mouses", "cables", "ram"]
ergebnis_dict = {product: ("stock high enough" if random.randint(0, 20) >= 10 else "needs reordering") for product in products}

print("products:", ergebnis_dict)