import random


def estimate_pi(points):
    inside_circle = 0

    for _ in range(points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            inside_circle += 1

    return 4 * (inside_circle / points)


def get_pi():
    num_points = int(input("How many random points do you want to generate? "))
    pi_approximation = estimate_pi(num_points)

    print(f"Approximation of pi using {num_points} points is: {pi_approximation: .2f}")


get_pi()
