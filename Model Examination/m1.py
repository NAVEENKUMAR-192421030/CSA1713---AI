def f(x):
    return -x * x + 6 * x

x = 0

while True:
    current = f(x)
    left = f(x - 1)
    right = f(x + 1)

    print("State:", x, "Value:", current)

    if left > current:
        x = x - 1
    elif right > current:
        x = x + 1
    else:
        break

print("Maximum Value:", f(x))
print("Final State:", x)
