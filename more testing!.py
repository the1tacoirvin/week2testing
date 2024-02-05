def Secant(fcn, x0, x1, maxiter, xtol):
    # Initial values
    x_previous = x0
    x_current = x1

    for i in range(maxiter):
        # Secant method iteration
        f_x_previous = fcn(x_previous)
        f_x_current = fcn(x_current)

        # Check for division by zero
        if f_x_current - f_x_previous == 0:
            print("Error: Division by zero")
            return None

        # Calculate the new estimate using the secant method formula
        x_new = x_current - f_x_current * (x_current - x_previous) / (f_x_current - f_x_previous)

        # Check for convergence
        if abs(x_new - x_current) < xtol:
            return x_new

        # Update values for the next iteration
        x_previous = x_current
        x_current = x_new

    # Return the final estimate if maxiter is reached
    return x_current

def main():
    # Test case
    result1 = Secant(lambda x: x**3 - 6*x**2 + 11*x - 6, 1, 2, maxiter=5, xtol=1e-4)
    print("Result 1:", result1)

if __name__ == "__main__":
    main()
