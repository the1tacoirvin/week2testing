import math


def Secant(fcn, x0, x1, maxiter=10, xtol=1*math.exp(-8)):
    # Initial values
    x_previous = x0
    x_current = x1

    for i in range(maxiter):
        # Secant method iteration
        f_x_previous = fcn(x_previous)
        f_x_current = fcn(x_current)

        # Check for division by zero
        if f_x_current - f_x_previous == 0:
            raise ValueError("Secant method: Division by zero")

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
    # Test cases
    result1 = Secant(lambda x: x**3 - 6*x**2 + 11*x - 6, 1, 2, maxiter=5, xtol=1*math.exp(-8))
    print("Result 1:", result1)

    result2 = Secant(lambda x: x**3 - 6*x**2 + 11*x - 6, 1, 2, maxiter=15, xtol=1e-8)
    print("Result 2:", result2)

    result3 = Secant(lambda x: x**3 - 6*x**2 + 11*x - 6, 1, 2, maxiter=3, xtol=1e-8)
    print("Result 3:", result3)

if __name__ == "__main__":
    main()
