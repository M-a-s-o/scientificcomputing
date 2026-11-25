import numpy as np


def exercise_01() -> None:
    print("Exercise 1, part A:")

    array = np.arange(1, 16, 1).reshape(3, 5).T
    array2 = array[1:4:2]
    print(array)
    print(array2)

    print("Exercise 1, part B:")
    dim = 4
    array2d = np.ones((dim, dim), dtype=int)
    print(array2d)
    array2d[1:-1, 1:-1] = 0
    print(array2d)


def exercise_06() -> None:
    print("\n\nExercise 6:")

    def get_point(file) -> tuple[float, float]:
        return (
            int(file.read(15)) / int("9" * 15),
            int(file.read(15)) / int("9" * 15),
        )

    rng = np.random.default_rng()
    with open(
        "1-100000000.txt"
    ) as file:  # from https://files.pilookup.com/pi/1-100000000.zip
        file.read(rng.integers(50, 100, dtype=int))

        samples = 100_000
        count_area = 0  # Count points within quarter circle
        sum = 0  # Estimate integral sqrt(1-x**2) dx over [0,1]
        for _ in range(samples):
            x, y = get_point(file)
            if x * x + y * y <= 1.0:
                count_area += 1
            sum += np.sqrt(1.0 - x * x) + np.sqrt(1.0 - y * y)

    print("pi            :", np.pi)
    print("Area method   :", count_area / samples * 4)
    print("MC integration:", sum / (2 * samples) * 4)


if __name__ == "__main__":
    exercise_01()
    exercise_06()
