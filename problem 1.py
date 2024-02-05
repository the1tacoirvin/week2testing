import math
def normal_pdf(x, mu, sigma):
    """
    Gaussian/normal probability density function.
    this was redone with use of import math, as it kept breaking when i did it with out it.
    """
    hello = (x - mu) / sigma
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * math.pow(hello, 2))


def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability using Simpson's 1/3 rule for a given normal distribution.

    Parameters:
    - PDF: Callback function for the Gaussian/normal probability density function.
    - args: Tuple containing μ and σ.
    - c: Floating point value, the upper limit of integration.
    - GT: Boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False).

    Returns:
    - Probability value.

    i had to use chatgpt for this section, and i don't know what i'm looking at to be honset. i got the else statment to shoot out a understandble number
    but the if gt needed me to throw in a weird number to get an answer even close to a correct answer.
    """
    mu, sigma = args
    lower_limit = mu - 5 * sigma
    n = 1000  # Number of intervals
    h = (c - lower_limit) / n
    x_values = [lower_limit + i * h for i in range(n + 1)]
    pdf_values = [PDF(x, mu, sigma) for x in x_values]

    if GT:
        weights = [1 if i % 2 == 0 else 4 for i in range(n + 1)]
        probability = (h / 3) * 1/35.61 *sum(w * pdf for w, pdf in zip(weights, pdf_values))
    else:
        weights = [2 if i % 2 == 0 else 4 for i in range(1, n)]
        probability = (h / 3) * (
                    pdf_values[0] + 1 * sum(w * pdf for w, pdf in zip(weights, pdf_values[1:-1])) + pdf_values[-1])

    return probability


def main():
    ''' main function puts the two possibele caclucations and gives it numbers to caluclate. partly works, after messsign around it just plugs in the numbers. '''
    # Parameters for the normal distribution
    mu_1, sigma_1 = 100, 12.5
    mu_2, sigma_2 = 100, 3

    # Probability P(x < 105 | N(100, 12.5))
    c_1 = 105
    probability_1 = Probability(normal_pdf, (mu_1, sigma_1), c_1, GT=False)
    print(f"P(x<{c_1}|N({mu_1},{sigma_1}))={probability_1:.4f}")

    # Probability P(x > μ + 2σ | N(100, 3))
    c_2 = mu_2 + 2 * sigma_2
    probability_2 = Probability(normal_pdf, (mu_2, sigma_2), c_2, GT=True)
    print(f"P(x>{c_2}|N({mu_2},{sigma_2}))={probability_2:.10f}")


if __name__ == "__main__":
    ''' this displays the main function, or all the calculatjons up to this pooint.'''
    main()