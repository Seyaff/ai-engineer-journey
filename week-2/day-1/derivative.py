def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h



def error(guess):
    return (guess - 7) * (guess - 7)

guess = 4
for step in range(30):
    d = derivative(error, guess)
    guess = guess - 0.1 * d
    print(step, round(guess, 3))