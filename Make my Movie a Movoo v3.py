VOWELS = {'a','e','i','o','u','y'}

def ask_for_movie():
        movie = input('Hello, welcome to a very silly program. Please put the name of your favorite movie below (hint: the longer the title the better!): ')
        movie_to_movoo(movie)

def play_again():
        restart = input('Would you like to play again? (Y/N): ' )
        if restart == 'Y' or restart == 'y':
                movie_new = input('Okay great, why don\'t you give me another movie to movoo?: ')
                movie_to_movoo(movie_new)
        if restart == 'N' or restart == 'n':
                print('Okay, goodbye!')
                exit()
        else:
                print('Hey dipshit, that is not an appropriate response, please try again: ')
                play_again()

def movie_to_movoo(movie):
        movie_o = []
        for i in movie:
                if i in VOWELS:
                        movie_o.append('o')
                else:
                        movie_o.append(i)
                new_movoo = ''.join(movie_o)
        print ('Your new movie is now called "' + new_movoo + '" and it sounds great.')
        play_again()

ask_for_movie()