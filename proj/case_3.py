import random


def finish():
    yield "This"
    yield "is"
    yield "the"
    yield "end..."


def calculate_next_number():
    memory = list(range(10))
    times = 1
    while memory:
        v = memory.pop(-1) * times
        times = (yield v) or 1
    yield finish()


gen = calculate_next_number()
print(next(gen))
for i in random.sample(range(100), 9):
    if i % 2 == 0:
        value = next(gen)
        print(value)
    else:
        print(gen.send(i))

print(" ".join(str(elem) for elem in gen))
