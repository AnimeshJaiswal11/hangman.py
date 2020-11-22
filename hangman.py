import random
movies = ["don","Baaghi","titanic"]
name = input("Enter your name: ")
print("Hello " + name + " Welcome to Hangman arena !!")
total_turns = 7
print("So let's get started")
print("Following are the rules of the game:")
print("You have to guess a movie name")
print("You will be given " + str(total_turns) + " chances to guess a movie")
print("If you have guessed a wrong character one turn will be deducted")
print("Okay....let's play")
print("Please type exit if you want to stop the game play")
q = "y"
while True:
    choosen = []
    random.shuffle(movies)
    movie = orgmovie = random.choice(movies).lower()
    if q == "y" or q == "yes":
        turns = total_turns
        for i in movie:
            if i != " ":
                movie = movie.replace(i,"-")
        print("Guess movie " + movie)
        while turns > 0:
            guess = input("Guess Character: ")
            guess = guess.lower()
            if guess == "exit":
                exit(0)
            if guess in orgmovie:
                for _ in range(0, len(movie)):
                    if orgmovie[_] == guess:
                        temp = list(movie)
                        temp[_] = guess
                        movie = "".join(temp)
            else:
                if guess in choosen:
                    print("Already choosen, try another one")
                    continue
                else:
                    turns -= 1
                    choosen.append(guess)
                    print("Wrong guess, try another one ")
                    print("turns remain: " + str(turns))
            print(movie)
            if movie == orgmovie:
                print("You Won!!")
                break
        if turns == 0:
            print("You Loose..")
            print("correct answer: " + orgmovie.upper())
            print("Better luck next time")
    if q != "y" or q != "yes":
        break

