import random

# print(f"{random.random()}")
# print(f"{random.randint(1,10)}")
# print(f"{random.randrange(1,102)}")
# print(f"{random.uniform(1,102):.4f}")

colors = ["red" , "green" , "blue" , "black" , "white"]

numbers = list(range(1,100))

random_list = random.choice(colors)
random_3 =random.choices(colors, k=3)
random_uniq = random.sample(colors, 3)


numbers = list(range(1,100))
print(numbers)
random.shuffle(numbers)
print("==========================")
print(numbers)