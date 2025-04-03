import math

# Define the function for problem A
def f(x):
    return math.exp(x) + 2**(-x) + 2 * math.cos(x) - 6

# Secant Method implementation with tabular output
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    print(f"{'Iter':<5} {'a (x0)':<12} {'b (x1)':<12} {'c (x2)':<12} {'f(a)':<12} {'f(b)':<12} {'f(c)':<12} {'Updated'}")
    print("-" * 90)

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Avoid division by zero
        if f_x1 - f_x0 == 0:
            print("Division by zero encountered in the secant method.")
            return None

        # Secant method formula
        x2 = x0 - f_x0 * (x0 - x1) / (f_x0 - f_x1)
        f_x2 = f(x2)

        # Check for convergence
        if abs(x2 - x1) < tol:
            print(f"{i+1:<5} {x0:<12.6f} {x1:<12.6f} {x2:<12.6f} {f_x0:<12.6f} {f_x1:<12.6f} {f_x2:<12.6f} {'-' * 7}")
            print(f"\nRoot found: {x2:.6f} (converged in {i+1} iterations)")
            return x2

        # Determine which value is replaced
        update = "b → a; " "c → b"

        # Print iteration details
        print(f"{i+1:<5} {x0:<12.6f} {x1:<12.6f} {x2:<12.6f} {f_x0:<12.6f} {f_x1:<12.6f} {f_x2:<12.6f} {update}")

        # Update guesses for the next iteration
        x0, x1 = x1, x2

    print("Secant method did not converge within the maximum number of iterations.")
    return None

# Get user input for initial guesses
try:
    x0 = float(input("Enter the first initial guess (a): "))
    x1 = float(input("Enter the second initial guess (b): "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

# Call the secant method
root = secant_method(f, x0, x1)

# Output the result
if root is not None:
    print(f"\nThe root of the equation is approximately: {root:.6f}")