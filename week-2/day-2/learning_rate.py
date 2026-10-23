def derivative(f , x , h=0.0001):
    return (f(x+h) - f(x))/h



def error(guess) :
    return (guess - 7) * (guess -7)


guess = 4
lr = 0.1
steps = 0

while error(guess) > 0.0001 and steps < 1000:
    d = derivative(error, guess)
    guess = guess - lr * d
    steps += 1
    print(steps, round(guess, 4), round(error(guess), 6))
    
print(f"Done : {steps} , step guess = {round(guess , 4)}")
