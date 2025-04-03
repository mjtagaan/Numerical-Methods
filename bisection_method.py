import math

# Define the function whose root we want to find
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6 # <<<<--- Modify this part

# Find a valid interval [a, b] where f(a) and f(b) have opposite signs
def find_interval(a, b, step):
    while f(a) * f(b) >= 0:  # Ensure the function changes sign in the interval
        a += step
        b += step
    return a, b

# Bisection method to find the root of f(x)
def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial interval: f(a) and f(b) must have opposite signs.")

    for i in range(max_iter):
        c = (a + b) / 2  # Compute midpoint

        if abs(f(c)) < tol:  # Check if f(c) is close to zero
            return c

        # Narrow down the interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("Max iterations reached without convergence.")

# Define initial values
initial_a = 1.0
initial_b = 2.0
step = 0.1

# Find a valid interval and compute the root
a, b = find_interval(initial_a, initial_b, step)
root = bisection_method(a, b)
print(f"Root: {root:.6f}")