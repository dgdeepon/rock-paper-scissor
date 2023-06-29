# This Python file uses the following encoding: utf-8
import random


run=True

while run:

    try:

        options=" 1.ROCK \n 2.PAPER \n 3.SCISSOR"
        userInput=int(input(options+"\n"+"Select your option : "))

        str=['ROCK','PAPER','SCISSOR'];

        computerScore=0
        playerScore=0

        while True :
            if  (userInput-1) > (len(str)-1):
                userInput=int(input(options+"\n"+"Invalid input, Please try again : "))
                continue
            else:
                computerInput=random.randint(0,2)
                if str[userInput-1] == "ROCK" and str[computerInput]== "PAPER" :
                    computerScore+=1
                    print( "Player: "+(str[userInput-1])+" & "+"Computer: "+(str[computerInput]))
                    print('Computer won this round 🎉')
                    print("Computer Score:{}\nPlayer Score:{}".format(computerScore,playerScore))
                elif str[userInput-1] == "SCISSOR" and str[computerInput] == "ROCK":
                    computerScore+=1    
                    print( "Player: "+(str[userInput-1])+" & "+"Computer: "+(str[computerInput]))
                    print('Computer won this round 🎉')
                    print("Computer Score:{}\nPlayer Score:{}".format(computerScore,playerScore))
                elif str[userInput-1] == "PAPER" and str[computerInput] == "SCISSOR":
                    computerScore+=1
                    print( "Player: "+(str[userInput-1])+" & "+"Computer: "+(str[computerInput]))
                    print('Computer won this round 🎉')
                    print("Computer Score:{}\nPlayer Score:{}".format(computerScore,playerScore))
                elif str[userInput-1] == str[computerInput] :
                    print("It's a tie 🤝")
                    print( "Player: "+(str[userInput-1])+" & "+"Computer: "+(str[computerInput]))
                    print("Computer Score:{}\nPlayer Score:{}".format(computerScore,playerScore))
                else :
                    playerScore+=1   
                    print( "Player: "+(str[userInput-1])+" & "+"Computer: "+(str[computerInput]))
                    print('You won this round 🎉')
                    print("Computer Score:{}\nPlayer Score:{}".format(computerScore,playerScore))
                try:    
                    playCheck=input("[1 - Continue / 0 - Exit]")
                    print(playCheck)
                    if playCheck == 1:
                        userInput=int(input(options+"\n"+"Select your option : "))
                        continue
                    else:
                        run=False
                        print("Thank you for playing 😎")
                        break
                except NameError:
                    print(NameError)
    except NameError:
        print(NameError)



