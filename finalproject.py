#finalproject.py
#Take a personality test, get synopsis of your results and a new music artist to listen to based off results

import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import sys

def main():

    #infile = open("clientID.txt", "r") #read client credentials needed to access spotipy 
    cid = "36541021a8a24ba78d0880ce4aa827fc"
    secret = "944ba6ae30d74da286e0f7890b51cd8c"

    # #Introduce the program
    # print("For each set of words, type the corresponding letter to the word that you feel the most association to.\n")
    # time.sleep(2.0)
    # print("\nFor example, if the words given was: \n A. Bold \n B. Sympathetic \n C. Quiet \n D. Perfectionist \nAnd I related the most to 'Spontaneous' I would type in 'B'. ")
    # time.sleep(3.0)
    # print("\nAt the end of this quiz, you will recieve a new music artist to listen to based off your personality!")
    # time.sleep(2.0)
    # print("Let's begin!")
    # time.sleep(2.0)

    # #Have all variables start at 0, being able to add as user answers questions
    # a = 0
    # b = 0
    # c = 0
    # d = 0
   
    # #Ask questions 
    # answer1 = input("\nA. Likes Authority \nB. Enthusiastic \nC. Sensitive Feelings \nD. Likes Instructions \n Please type in A, B, C or D:  ")
    # while answer1.lower() != "a" and answer1.lower() != "b" and answer1.lower() != "c" and answer1.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer1 = input("A. Likes Authority \nB. Enthusiastic \nC. Sensitive Feelings \nD. Likes Instructions \n Please type in A, B, C or D:  ")
    # if answer1.lower() == "a":
    #     a += 1
    # elif answer1.lower() == "b":
    #     b += 1
    # elif answer1.lower() == "c":
    #     c += 1
    # elif answer1.lower() == "d":
    #     d += 1

    # answer2 = input("\nA. Takes Charge \nB. Takes Risks \nC. Loyal \nD. Accurate \n Please type in A, B, C or D:  ")
    # while answer2.lower() != "a" and answer2.lower() != "b" and answer2.lower() != "c" and answer2.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer2 = input("A. Takes Charge \nB. Takes Risks \nC. Loyal \nD. Accurate \n Please type in A, B, C or D:  ")
    # if answer2.lower() == "a":
    #     a += 1
    # elif answer2.lower() == "b":
    #     b += 1
    # elif answer2.lower() == "c":
    #     c += 1
    # elif answer2.lower() == "d":
    #     d += 1
    
    # answer3 = input("\nA. Determined \nB. Visionary \nC. Calm \nD. Consistent \n Please type in A, B, C or D:  ")
    # while answer3.lower() != "a" and answer3.lower() != "b" and answer3.lower() != "c" and answer3.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer3 = input("A. Determined \nB. Visionary \nC. Calm \nD. Consistent \n Please type in A, B, C or D:  ")
    # if answer3.lower() == "a":
    #     a += 1
    # elif answer3.lower() == "b":
    #     b += 1
    # elif answer3.lower() == "c":
    #     c += 1
    # elif answer3.lower() == "d":
    #     d += 1

    # answer4 = input("\nA. Problem Solver \nB. Enjoys Popularity \nC. Gives In To Others \nD. Factual \n Please type in A, B, C or D:  ")
    # while answer4.lower() != "a" and answer4.lower() != "b" and answer4.lower() != "c" and answer4.lower()!= "d":
    #     print("Sorry I don't understand that response.")
    #     answer4 = input("A. Problem Solver \nB. Enjoys Popularity \nC. Gives In To Others \nD. Factual \n Please type in A, B, C or D:  ")
    # if answer4.lower() == "a":
    #     a += 1
    # elif answer4.lower() == "b":
    #     b += 1
    # elif answer4.lower() == "c":
    #     c += 1
    # elif answer4.lower() == "d":
    #     d += 1

    # answer5 = input("\nA. Competitive \nB. Promoter \nC. Dislikes Change \nD. Practical \n Please type in A, B, C or D:  ")
    # while answer5.lower() != "a" and answer5.lower() != "b" and answer5.lower() != "c" and answer5.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer5 = input("A. Competitive \nB. Promoter \nC. Dislikes Change \nD. Practical \n Please type in A, B, C or D:  ")
    # if answer5.lower() == "a":
    #     a += 1
    # elif answer5.lower() == "b":
    #     b += 1
    # elif answer5.lower() == "c":
    #     c += 1
    # elif answer5.lower() == "d":
    #     d += 1
    
    # answer6 = input("\nA. Productive \nB. Fun-Loving \nC. Avoids Confrontation \nD. Conscientious \n Please type in A, B, C or D:  ")
    # while answer6.lower() != "a" and answer6.lower() != "b" and answer6.lower() != "c" and answer6.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer6 = input("A. Productive \nB. Fun-Loving \nC. Avoids Confrontation \nD. Conscientious \n Please type in A, B, C or D:  ")
    # if answer6.lower() == "a":
    #     a += 1
    # elif answer6.lower() == "b":
    #     b += 1
    # elif answer6.lower() == "c":
    #     c += 1
    # elif answer6.lower() == "d":
    #     d += 1

    # answer7 = input("\nA. Bold \nB. Likes Variety \nC. Sympathetic \nD. Perfectionist \n Please type in A, B, C or D:  ")
    # while answer7.lower() != "a" and answer7.lower() != "b" and answer7.lower() != "c" and answer7.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer7 = input("A. Bold \nB. Likes Variety \nC. Sympathetic \nD. Perfectionist \n Please type in A, B, C or D:  ")
    # if answer7.lower() == "a":
    #     a += 1
    # elif answer7.lower() == "b":
    #     b += 1
    # elif answer7.lower() == "c":
    #     c += 1
    # elif answer7.lower() == "d":
    #     d += 1

    # answer8 = input("\nA. Decision Maker \nB. Spontaneous \nC. Nurturing \nD. Detail-Oriented \n Please type in A, B, C or D:  ")
    # while answer8.lower() != "a" and answer8.lower() != "b" and answer8.lower() != "c" and answer8.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer8 = input("A. Decision Maker \nB. Spontaneous \nC. Nurturing \nD. Detail-Oriented \n Please type in A, B, C or D:  ")
    # if answer8.lower() == "a":
    #     a += 1
    # elif answer8.lower() == "b":
    #     b += 1
    # elif answer8.lower() == "c":
    #     c += 1
    # elif answer8.lower() == "d":
    #     d += 1

    # answer9 = input("\nA. Persistent \nB. Inspirational \nC. Peacemaker \nD. Analytical \n Please type in A, B, C or D:  ")
    # while answer9.lower() != "a" and answer9.lower() != "b" and answer9.lower()!= "c" and answer9.lower() != "d":
    #     print("Sorry I don't understand that response.")
    #     answer9 = input("A. Persistent \nB. Inspirational \nC. Peacemaker \nD. Analytical  \n Please type in A, B, C or D:  ")
    # if answer9.lower() == "a":
    #     a += 1
    # elif answer9.lower() == "b":
    #     b += 1
    # elif answer9.lower() == "c":
    #     c += 1
    # elif answer9.lower() == "d":
    #     d += 1
    
    # #Print Results
    # time.sleep(2.0)
    # print("\nTime for results!")
    # time.sleep(2.0)
    # if (a > (b and c and d)):
    #     print("\nYou selected 'A' the most! \nYou are a natural born leader. You may be a boss at work, super decisive and love to solve problems! You may be very confident and self-reliant, leading you to take charge when no one else will.")
    #     time.sleep(2.0)
    #     print("Some of your natural strengths may include: Achievement driven, Gets results, Independent, Risk-taker, Takes initiative, and persistent!")
    #     time.sleep(2.0)
    #     print("\nSomeone who shares this personality type is Freddie Mercury band Queen! That's pretty badass.")
    #     time.sleep(1.0)
    #     print("\nHere are Queen's top tracks from Spotify: ")
    #     #SPOTIPY FOR QUEEN

    # elif (b > (a and c and d)):
    #     print("\nYou selected 'B' the most! \nYou are like an excitable, fun-seeking, cheerleader! You might be great at motivating others. You may also succeed in an enviornment where you can talk. You can be very loving and encouraging, paired with a desire to be the center of attention.")
    #     time.sleep(2.0)
    #     print("Some of your strengths may include: Enthusiastic, Optimistic, Emotional and Passionate, and Personal!")
    #     time.sleep(2.0)
    #     print("\nSomeone who shares this personality type is P!nk.")
    #     time.sleep(1.0)
    #     print("\nHere is P!nk's top tracks from Spotify: ")
    #     #SPOTIPY FOR P!NK

    # elif (c > (a and b and d)):
    #     print("\nYou selected 'C' the most!\nYou are more than likely a people pleaser. Which isn't a bad thing! You're incredibly loyal to those you enjoy. You might be a great listener, empathetic, and a wonderful encourager!")
    #     time.sleep(2.0)
    #     print("Some of your strengths may include: Patient, Easy-going, Stable, Team player, and Reliable.")
    #     time.sleep(2.0)
    #     print("\nSomeone who shares this personality type is Ella Fitzgerald.")
    #     time.sleep(1.0)
    #     print("\nHere is Ella Fitzgerald's top tracks from Spotify: ")
    #     #SPOTIPY FOR ELLA 

    # elif (d > (a and b and c)):
    #     print("\nYou selected 'D' the most!\nYou are a rule-follower. You have a strong need to do things the correct way. You probably read the instruction manuals.")
    #     time.sleep(2.0)
    #     print("Some of your strengths may include: Accurate, Analytical, Orderly, High standards.")
    #     time.sleep(2.0)
    #     print("\nSomeone who shares this personality type is George Strait.")
    #     time.sleep(1.0)
    #     print("\nHere is George Straight's top tracks from Spotify: ")
    #     #SPOTIPY FOR GEORGE
    
    surfaces_url = 'https://open.spotify.com/artist/4ETSs924pXMzjIeD6E9b4u'

    #spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    spotify = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = '', client_secret = '', redirect_uri = '', user = ''))

    results = spotify.artist_albums(surfaces_url, album_type='album')
    albums = results['items']

    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])
   

if __name__ == "__main__":
    main()