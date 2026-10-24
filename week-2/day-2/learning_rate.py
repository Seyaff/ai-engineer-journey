def derivative(f , x , h=0.0001):
    return (f(x+h) - f(x))/h



def error(guess) :
    return (guess - 7) * (guess -7)


for lr in [0.01, 0.1, 0.3, 0.5, 0.9, 1.0, 1.1]:
    guess = 4
    steps = 0
    while error(guess) > 0.0001 and steps < 1000:
        d = derivative(error, guess)
        guess = guess - lr * d
        steps += 1
    print("lr =", lr, "| steps:", steps, "| final guess:", round(guess, 4))