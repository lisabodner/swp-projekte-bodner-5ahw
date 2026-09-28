import random
if __name__ == '__main__':
    dataset = random.sample(range(1, 11), 10)
    datapoint = random.randint(0, 11)

    if datapoint == 0:
        print(f"datapoint is at min value: {datapoint}")
    elif datapoint in range(1, 9):
        print(f"datapoint is somewhere in between: {datapoint}")
    else:
        print(f"datapoint is at max value: {datapoint}")

    i = 1
    for num in dataset:
        print(f"{i}. random value: {num}")
        i+=1

    n = random.randint(1, 10)
    while n != 4:
        print(f" {n} is still not 4")
        n = random.randint(1, 10)

    for i in range(1, 11):
        n = random.randint(1, 11)
        if n == 5:
            break
        print(f"{i}. time its not 5 but {n} :'")

    for i in range(1, 10):
        n = random.randint(1, 11)
        if n != 7:
            pass
        else:
            print(f"{i}. number is 7")

    try:
        for i in range(1,12):
            print(f"{i}. datapoint: {dataset[i]}")
    except IndexError:
        print("out of bounds :(")

