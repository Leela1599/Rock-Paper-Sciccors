x = input("Choose Your Thing Player 1 : ")
y = input("Now Player 2 Turn : ")

if x == 'paper' and y == 'rock':
    print("Player 2 win")
elif x == 'paper' and y == 'scissors':
   print("Player 2 win")
elif x == 'rock' and y == 'scissors':
    print("Player 1 win")
elif x == 'rock' and y == 'paper':
    print("Player 1 win")
elif x == 'scissors' and y == 'rock':
    print("Player 2 win")
elif x == 'scissors' and y == 'paper':
    print("Player 1 win")
else:
    print("Error, both players cant choose the same thing")