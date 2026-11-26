import matplotlib.pyplot as plt
import numpy as np


def exercise_02() -> None:
    sM_ax = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
    period = np.array(
        [0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09]
    )
    names = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        "Pluto",
    ]
    plt.scatter(period, sM_ax)
    plt.xscale("log")
    plt.xlabel("Period/years")
    plt.yscale("log")
    plt.ylabel("Semi-major axis/AU")
    for name, per, sm in zip(names, period, sM_ax):
        plt.annotate(name, (per + np.pow(10, np.log10(per)) * 0.1, sm))
    plt.show()


def exercise_07() -> None:
    fractal = "mandelbrot"
    # fractal = "burning ship"
    Nmax = 1024
    N = 256

    def get_mandelbrot(z, c):
        return z * z + c

    def get_burning_ship(z, c):
        return np.square(np.abs(np.real(z)) + 1j * np.abs(np.imag(z))) + c

    if "mandelbrot" in fractal.lower():
        next_iter = get_mandelbrot
        max_abs = 2
        xmin, xmax = -2.5, 1
        ymin, ymax = -1.5, 1.5
    elif "burning ship" in fractal.lower():
        next_iter = get_burning_ship
        max_abs = 4
        xmin, xmax = -3, 2
        ymin, ymax = -2, 1
    else:
        raise UserWarning("Choose either Mandelbrot or Burning Ship fractals")

    x = np.linspace(xmin, xmax, N)
    y = np.linspace(ymin, ymax, N)

    xv, _ = np.meshgrid(x, y, indexing="ij")
    c = xv + 1j * y

    z = np.zeros((N, N), dtype=np.complex128)
    mask = np.ones_like(z)
    counts = np.zeros_like(z, dtype=np.int64)

    iters = 0
    # while np.any(mask) or iters < Nmax:
    while iters < Nmax:
        z = next_iter(z, c)
        mask = np.where(np.abs(z) <= max_abs)
        counts[mask] += 1
        iters += 1

    counts = Nmax / counts
    counts[counts == np.inf] = Nmax
    _, ax = plt.subplots()
    ax.imshow(counts.T, aspect=(ymax - ymin) / (xmax - xmin))
    plt.show()


def exercise_09() -> None:
    print("Cough")


if __name__ == "__main__":
    exercise_02()
    exercise_07()
    exercise_09()
