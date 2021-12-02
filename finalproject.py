#finalproject.py
#Take a personality test, get synopsis of your results and a new music artist to listen to based off results
import time
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

def main():

    infile = open("clientID.txt", "r") #read client credentials needed to access spotipy 
    cid = infile.readline()
    secret = infile.readline()
    print(cid)
    print(secret)

    #Introduce the program
    # print("For each set of words, type the corresponding letter to the word that you feel the most association to.\n")
    # time.sleep(2.0)
    # print("\nFor example, if the words given was: \n A. Bold \n B. Sympathetic \n C. Quiet \n D. Perfectionist \nAnd I related the most to 'Spontaneous' I would type in 'B'. ")
    # time.sleep(3.0)
    # print("\nAt the end of this quiz, you will recieve a new music artist to listen to based off your personality!")
    # time.sleep(2.0)

    # #Have all variables start at 0, being able to add as user answers questions
    a = 0
    b = 0
    c = 0
    d = 0
   
    #Ask questions 
    answer1 = input("A. Likes Authority \nB. Enthusiastic \nC. Sensitive Feelings \nD. Likes Instructions \n Please type in A, B, C or D:  ")
    while answer1 != "a" and answer1 != "b" and answer1 != "c" and answer1 != "d":
        print("Sorry I don't understand that response.")
        answer1 = input("A. Likes Authority \nB. Enthusiastic \nC. Sensitive Feelings \nD. Likes Instructions \n Please type in A, B, C or D:  ")
    if answer1.lower() == "a":
        a += 1
    elif answer1.lower() == "b":
        b += 1
    elif answer1.lower() == "c":
        c += 1
    elif answer1.lower() == "d":
        d += 1

    answer2 = input("A. Takes Charge \nB. Takes Risks \nC. Loyal \nD. Accurate \n Please type in A, B, C or D:  ")
    while answer2 != "a" and answer2 != "b" and answer2 != "c" and answer2 != "d":
        print("Sorry I don't understand that response.")
        answer2 = input("A. Takes Charge \nB. Takes Risks \nC. Loyal \nD. Accurate \n Please type in A, B, C or D:  ")
    if answer2.lower() == "a":
        a += 1
    elif answer2.lower() == "b":
        b += 1
    elif answer2.lower() == "c":
        c += 1
    elif answer2.lower() == "d":
        d += 1
    
    answer3 = input("A. Determined \nB. Visionary \nC. Calm \nD. Consistent \n Please type in A, B, C or D:  ")
    while answer3 != "a" and answer3 != "b" and answer3 != "c" and answer3 != "d":
        print("Sorry I don't understand that response.")
        answer3 = input("A. Determined \nB. Visionary \nC. Calm \nD. Consistent \n Please type in A, B, C or D:  ")
    if answer3.lower() == "a":
        a += 1
    elif answer3.lower() == "b":
        b += 1
    elif answer3.lower() == "c":
        c += 1
    elif answer3.lower() == "d":
        d += 1

    answer4 = input("A. Problem Solver \nB. Enjoys Popularity \nC. Gives In To Others \nD. Factual \n Please type in A, B, C or D:  ")
    while answer4 != "a" and answer4 != "b" and answer4 != "c" and answer4 != "d":
        print("Sorry I don't understand that response.")
        answer4 = input("A. Problem Solver \nB. Enjoys Popularity \nC. Gives In To Others \nD. Factual \n Please type in A, B, C or D:  ")
    if answer4.lower() == "a":
        a += 1
    elif answer4.lower() == "b":
        b += 1
    elif answer4.lower() == "c":
        c += 1
    elif answer4.lower() == "d":
        d += 1

    answer5 = input("A. Competitive \nB. Promoter \nC. Dislikes Change \nD. Practical \n Please type in A, B, C or D:  ")
    while answer5 != "a" and answer5 != "b" and answer5 != "c" and answer5 != "d":
        print("Sorry I don't understand that response.")
        answer5 = input("A. Competitive \nB. Promoter \nC. Dislikes Change \nD. Practical \n Please type in A, B, C or D:  ")
    if answer5.lower() == "a":
        a += 1
    elif answer5.lower() == "b":
        b += 1
    elif answer5.lower() == "c":
        c += 1
    elif answer5.lower() == "d":
        d += 1
    
    answer6 = input("A. Productive \nB. Fun-Loving \nC. Avoids Confrontation \nD. Conscientious \n Please type in A, B, C or D:  ")
    while answer6 != "a" and answer6 != "b" and answer6 != "c" and answer6 != "d":
        print("Sorry I don't understand that response.")
        answer6 = input("A. Productive \nB. Fun-Loving \nC. Avoids Confrontation \nD. Conscientious \n Please type in A, B, C or D:  ")
    if answer6.lower() == "a":
        a += 1
    elif answer6.lower() == "b":
        b += 1
    elif answer6.lower() == "c":
        c += 1
    elif answer6.lower() == "d":
        d += 1

    answer7 = input("A. Bold \nB. Likes Variety \nC. Sympathetic \nD. Perfectionist \n Please type in A, B, C or D:  ")
    while answer7 != "a" and answer7 != "b" and answer7 != "c" and answer7 != "d":
        print("Sorry I don't understand that response.")
        answer7 = input("A. Bold \nB. Likes Variety \nC. Sympathetic \nD. Perfectionist \n Please type in A, B, C or D:  ")
    if answer7.lower() == "a":
        a += 1
    elif answer7.lower() == "b":
        b += 1
    elif answer7.lower() == "c":
        c += 1
    elif answer7.lower() == "d":
        d += 1

    answer8 = input("A. Decision Maker \nB. Spontaneous \nC. Nurturing \nD. Detail-Oriented \n Please type in A, B, C or D:  ")
    while answer8 != "a" and answer8 != "b" and answer8 != "c" and answer8 != "d":
        print("Sorry I don't understand that response.")
        answer8 = input("A. Decision Maker \nB. Spontaneous \nC. Nurturing \nD. Detail-Oriented \n Please type in A, B, C or D:  ")
    if answer8.lower() == "a":
        a += 1
    elif answer8.lower() == "b":
        b += 1
    elif answer8.lower() == "c":
        c += 1
    elif answer8.lower() == "d":
        d += 1

    answer9 = input("A. Persistent \nB. Inspirational \nC. Peacemaker \nD. Analytical \n Please type in A, B, C or D:  ")
    while answer9 != "a" and answer9 != "b" and answer9 != "c" and answer9 != "d":
        print("Sorry I don't understand that response.")
        answer9 = input("A. Persistent \nB. Inspirational \nC. Peacemaker \nD. Analytical  \n Please type in A, B, C or D:  ")
    if answer9.lower() == "a":
        a += 1
    elif answer9.lower() == "b":
        b += 1
    elif answer9.lower() == "c":
        c += 1
    elif answer9.lower() == "d":
        d += 1
    
    
    #Calculate results based off highest count of variables

    #Spotipy
    #try:
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    

    # client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

    #if len(sys.argv) > 1:
        #weezer = sys.argv[1]
    #else:
    weezer = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    response = sp.artist_top_tracks(weezer)

    for track in response['tracks']:
        print(track['name'])

    # except HTTPError as e:
    #     print(e)

    #Print results 



if __name__ == "__main__":
    main()