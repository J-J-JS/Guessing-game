import random

answer = random.randint(1, 100)
guess = int(input("Make your guess!\n"))
highscore = random.randint(1,15)
score = 0

while guess != answer:
 if guess > answer:
  print("your guess is lower then the answer!")
  guess = int(input("Make your guess!\n"))
  score = score + 1
 elif guess < answer:
  print("your guess is higher then the answer!")
  guess = int(input("Make your guess!\n"))
  score = score + 1
  

if guess == answer:
  score = score + 1
  print("the previous highscore was",highscore)
if score == 1:
  print("you got the answer!", answer, "in", score, "guess! wow that's impressive!")
elif score != 1:
  print("you got the answer!", answer, "in", score, "guesses!")