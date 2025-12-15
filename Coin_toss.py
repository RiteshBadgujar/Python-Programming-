import random

coin = random.choice(["Head", "Tail"])

guess = input("Guess Head or Tail: ")

if guess.capitalize() == coin:
    print("🎉 You Win!", coin)
else:
    print("❌ You Lose!", coin)
