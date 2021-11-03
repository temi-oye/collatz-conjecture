import matplotlib.pyplot as plt


def get_collatz_step(n, step=1):
    if (n == 1):
        return step
    if (n % 2 == 0):
        return get_collatz_step(n / 2, step + 1)
    if (n % 2 != 0):
        return get_collatz_step(n * 3 + 1, step + 1)


def collatz(num):
    x_axis = []
    y_axis = []

    for i in range(1, num + 1):
        x_axis.append(i)
        y_axis.append(get_collatz_step(i))

    fig, ax = plt.subplots()
    ax.bar(x_axis, y_axis)
    plt.title("Collatz Conjecture")
    plt.xlabel("The number")
    plt.ylabel("The steps taken to reach 1")
    plt.show()


collatz()
