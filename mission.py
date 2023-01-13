# 01

import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)

if secret == guess:
    print("just right")

else:
    if secret > guess:
        print("too low")

    else:
        print("too high")