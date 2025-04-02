import math

# Define the function for problem A
def f(x):
    return math.exp(x) + 2**(-x) + 2 * math.cos(x) - 6

# Secant Method implementation
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    
    # f: The function for which we are finding the root
    # x0, x1: Initial guesses
    # tol: Tolerance for stopping criteria
    # max_iter: Maximum number of iterations
    
    for i in range(max_iter):
        # Calculate the value of the function at the guesses
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Avoid division by zero
        if f_x1 - f_x0 == 0:
            print("Division by zero encountered in the secant method.")
            return None

        # Secant method formula
        x2 = x0 - f_x0 * (x0 - x1) / (f_x0 - f_x1)

        # Check for convergence
        if abs(x2 - x1) < tol:
            print(f"Root found: {x2} (converged in {i+1} iterations)")
            return x2

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
    print(f"The root of the equation is approximately: {root}")