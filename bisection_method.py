import math

# Define the function whose root we want to find
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6

# Find a valid interval [a, b] where f(a) and f(b) have opposite signs
def find_interval(a, b, step):
    while f(a) * f(b) >= 0:  # Ensure the function changes sign in the interval
        a += step
        b += step
    return a, b

# Bisection method with table output
def bisection_method_with_table(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial interval: f(a) and f(b) must have opposite signs.")
    
    print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<10}".format(
        "Iteration", "a", "b", "c", "f(a)", "f(b)", "f(c)", "Updated"
    ))
    print("-" * 95)
    
    for i in range(max_iter):
        c = (a + b) / 2  # Compute midpoint
        f_a, f_b, f_c = f(a), f(b), f(c)
        update_side = 'a' if f_a * f_c < 0 else 'b'

        # Print the iteration data
        print("{:<10} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<10}".format(
            i + 1, a, b, c, f_a, f_b, f_c, update_side
        ))

        if abs(f_c) < tol:  # Check if f(c) is close to zero
            print("\nRoot found: {:.6f} in {} iterations".format(c, i + 1))
            return c

        # Narrow down the interval
        if f_a * f_c < 0:
            b = c
        else:
            a = c

    raise ValueError("Max iterations reached without convergence.")

# Define initial values
initial_a = 1.0
initial_b = 2.0
step = 0.1

# Find a valid interval and compute the root with iteration tracking
a, b = find_interval(initial_a, initial_b, step)
root = bisection_method_with_table(a, b)
