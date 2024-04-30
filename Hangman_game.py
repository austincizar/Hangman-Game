import random

# a list containing the words to be guessed
words = "ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole rat raven rhino shark sheep spider toad turkey turtle wolf wombat zebra"
words= words.split(" ")
rand_word = random.choice(words)
#print (rand_word) #for debugging

# to display the first and last letters of the random word 
hidden = ""
num = 0
for char in rand_word:
    
    if char == rand_word[0] and num == 0:
         num += 1
         hidden += char
    elif char == rand_word[len(rand_word)-1] and num == len(rand_word)-1:
        num += 1
        hidden += char
    else:
        num += 1
        hidden += "_"
hidden_list = list(hidden)
print (hidden_list)



# the Hangman game.
def game():
    i = 0
    f = 0
    tries = 0
      
    l = int(len(rand_word)-1)
    
    while tries < len(rand_word)+2: # While loop defining the maximum number of attempts.
        
        if i == 0 and f == 0:
            print (" ")
            print ("First attempt, You have ", (len(rand_word)+2), " tries remaining")
        guess = input("Guess any letter in the hidden word: ")
       
        if guess not in rand_word: # Condition for if the guess is not in the random word
            f += 1
            tries += 1
            print ("Wrong guess, You have ", (len(rand_word)+2)-tries, " tries remaining")
            print (" ")
        c = int(-1)     
        for char in rand_word:
            location = 0 #To record the first occurance of the letter guessed.
            c += 1
            if guess == char:
                if guess not in hidden_list: 
                    i += 1
                    tries += 1
                    hidden_list[c] = guess
                    print (hidden_list) 
                    print ("Correct, You have ", (len(rand_word)+2)-tries, " tries remaining")
                    print (" ")
                    break
                else:
                    c2 = c
                    if guess in hidden_list:
                        if location == 0 :
                            location == c2+1
                        if c == -1:
                            location = 1
                        for y in range(location , l): #Loop to check for more occurances from the last registered occurance
                            if guess == rand_word[y] and guess != hidden_list[y]:
                                i += 1
                                tries += 1
                                hidden_list[y] = guess 
                                print (hidden_list)
                                print ("Correct, You have ", (len(rand_word)+2)-tries, " tries remaining")
                                print (" ")
                                break
                            elif y == l-1:
                                print("There are no more ", guess, "'s in the hidden word.")
                                tries += 1
                                print ("You have ", (len(rand_word)+2)-tries, " tries remaining")
                                print (" ")
                    break    
                   
        if i <= len(rand_word)-1 and "_" not in hidden_list: #The win condition
            print ("You Win! The hidden word is: ", rand_word) 
            break
        if tries >= len(rand_word)+2: #The loss condition
            print ("You Lose! The hidden word is: ", rand_word)  
            break
 

game() 


        
    

  