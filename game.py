from random import choice



print()
print("~~|CHOOSE YOUR GAME|~~")



def main():
    try:

        print()
        game = input("(Dice/Coin/Guess): ").strip().lower()
        if game == "dice":
            dice()
        elif game == "coin":
            coin()
        elif game == "guess":
            guess()
        elif game == "exit":
            print("Come back soon!")
            print()
        else:
            main()
    except EOFError:
        print()
        print("Come back Soon")

def dice():
    try:
        dice_roll = choice([1,2,3,4,5,6])
        print()
        print("~|WELCOME TO DICE|~")
        print()
        dice = input("Roll? (Y/N): ").strip().lower()

        if dice == "y":
            print(dice_roll)
            while True:
                dice_roll = choice([1,2,3,4,5,6])
                print()
                dice = input("Roll Again? (Y/N): ").strip().lower()
                if dice == "y":
                    print(dice_roll)
                elif dice == "n":
                    return main()
                else:
                    continue
        elif dice == "n":
            main()
    except EOFError:
        print()
        print("Come back Soon")

def coin():
    try:
        coin_flip = choice(['Heads', 'Tails'])
        print()
        print("~|WELCOME TO COINFLIP|~")
        print()
        coin = input("Flip Coin? (Y/N): ").strip().lower()

        if coin == "y":
            print(coin_flip)
            while True:
                coin_flip = choice(['Heads', 'Tails'])
                print()
                coin = input("Flip Again? (Y/N): ").strip().lower()
                if coin == "y":
                    print(coin_flip)
                elif coin == "n":
                    return main()
                else:
                    continue
        elif coin == "n":
            main()
    except EOFError:
        print()
        print("Come back Soon")


def guess():
    try:
        print()
        print("~|WELCOME TO GUESSING GAME|~")
        while True:
            guess = choice([1,2,3,4,5])
            print()
            try:
                num = int(input("Guess number from 1-5: "))

                if num > 5 or num < 1:
                    raise ValueError

                if num == guess:
                    print("CORRECT!!!")
                elif num != guess:
                    print("INCORRECT")
                    print(f"Answer was {guess}")
                    print()
                    again = input("Try again? (Y/N): ").strip().lower()
                    if again == "y":
                        continue
                    if again == "n":
                        return main()
            except ValueError:
                print("Only numbers between 1-5")
                continue
            else:
                continue
    except EOFError:
        print()
        print("Come back Soon")


main()
