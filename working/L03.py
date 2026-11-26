import matplotlib.pyplot as plt
import numpy as np


def exercise_02() -> None:
    print("Exercise 2:")
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
    print("Exercise 7:")
    fractal = "mandelbrot"
    fractal = "burning ship"
    Nmax = 512
    Nx = 1280
    Ny = 720

    def get_mandelbrot(z, c):
        return z * z + c

    def get_burning_ship(z, c):
        return np.square(np.abs(np.real(z)) + 1j * np.abs(np.imag(z))) + c

    if "mandelbrot" in fractal.lower():
        next_iter = get_mandelbrot
        max_abs = 2
        xmin, xmax = -2, 1
        ymin, ymax = -1.5, 1.5
    elif "burning ship" in fractal.lower():
        next_iter = get_burning_ship
        max_abs = 4
        # Full ship
        xmin, xmax = -2.6, 1.9
        ymin, ymax = -2.3, 1.9
        # Ship on lower left
        xmin, xmax = -1.815, -1.7
        ymin, ymax = -0.085, 0.012
    else:
        raise UserWarning("Choose either Mandelbrot or Burning Ship fractals")

    x = np.linspace(xmin, xmax, Nx)
    y = np.linspace(ymin, ymax, Ny)

    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    z = np.zeros_like(c)
    mask = np.ones(z.shape, dtype=bool)
    counts = np.zeros(z.shape, dtype=np.int64)

    for _ in range(Nmax):
        z[mask] = next_iter(z[mask], c[mask])
        mask &= np.abs(z) <= max_abs
        counts[mask] += 1
        if not mask.any():
            break

    counts[counts == 0] = 1
    vals = np.log(Nmax / counts)
    _, ax = plt.subplots()
    ax.imshow(
        vals.T,
        extent=(xmin, xmax, ymin, ymax),
        aspect="equal",
        origin="lower",
    )
    if "burning ship" in fractal.lower():
        ax.invert_yaxis()
    plt.show()


def exercise_09() -> None:
    print("Exercise 9:")
    print("Cough")


if __name__ == "__main__":
    exercise_02()
    exercise_07()
    exercise_09()
