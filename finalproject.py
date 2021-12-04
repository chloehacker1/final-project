#finalproject.py
#Take a personality test, get synopsis of your results and a new music artist to listen to based off results

import time #needed for sleep
from pygame import mixer #needed to play music

def main():

    #Introduce the program
    time.sleep(1.0)
    print("For each set of words, type the corresponding letter to the word that you feel the most association to.\n")
    time.sleep(3.0)
    print("\nFor example, if the words given was: \n A. Bold \n B. Sympathetic \n C. Quiet \n D. Perfectionist \nAnd I related the most to 'Spontaneous' I would type in 'B'. ")
    time.sleep(3.0)
    print("\nAt the end of this quiz, you will recieve a new music artist to listen to based off your personality!")
    time.sleep(2.0)
    print("Let's begin!")
    time.sleep(2.0)

    #Have all variables start at 0, being able to add as user answers questions
    a = 0
    b = 0
    c = 0
    d = 0
   
    #Ask questions 
    answer1 = input("\nA. Likes Authority \nB. Enthusiastic \nC. Sensitive Feelings \nD. Likes Instructions \n Please type in A, B, C or D:  ")
    while answer1.lower() != "a" and answer1.lower() != "b" and answer1.lower() != "c" and answer1.lower() != "d":
        print("Sorry I don't understand that response.")
        answer1 = input("A. Likes Authority \nB. Enthusiastic \nC. Sensitive Feelings \nD. Likes Instructions \n Please type in A, B, C or D:  ")
    if answer1.lower() == "a": #change total of choice as quiz continues
        a += 1
    elif answer1.lower() == "b":
        b += 1
    elif answer1.lower() == "c":
        c += 1
    elif answer1.lower() == "d":
        d += 1

    answer2 = input("\nA. Takes Charge \nB. Takes Risks \nC. Loyal \nD. Accurate \n Please type in A, B, C or D:  ")
    while answer2.lower() != "a" and answer2.lower() != "b" and answer2.lower() != "c" and answer2.lower() != "d":
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
    
    answer3 = input("\nA. Determined \nB. Visionary \nC. Calm \nD. Consistent \n Please type in A, B, C or D:  ")
    while answer3.lower() != "a" and answer3.lower() != "b" and answer3.lower() != "c" and answer3.lower() != "d":
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

    answer4 = input("\nA. Problem Solver \nB. Enjoys Popularity \nC. Gives In To Others \nD. Factual \n Please type in A, B, C or D:  ")
    while answer4.lower() != "a" and answer4.lower() != "b" and answer4.lower() != "c" and answer4.lower()!= "d":
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

    answer5 = input("\nA. Competitive \nB. Promoter \nC. Dislikes Change \nD. Practical \n Please type in A, B, C or D:  ")
    while answer5.lower() != "a" and answer5.lower() != "b" and answer5.lower() != "c" and answer5.lower() != "d":
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
    
    answer6 = input("\nA. Productive \nB. Fun-Loving \nC. Avoids Confrontation \nD. Conscientious \n Please type in A, B, C or D:  ")
    while answer6.lower() != "a" and answer6.lower() != "b" and answer6.lower() != "c" and answer6.lower() != "d":
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

    answer7 = input("\nA. Bold \nB. Likes Variety \nC. Sympathetic \nD. Perfectionist \n Please type in A, B, C or D:  ")
    while answer7.lower() != "a" and answer7.lower() != "b" and answer7.lower() != "c" and answer7.lower() != "d":
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

    answer8 = input("\nA. Decision Maker \nB. Spontaneous \nC. Nurturing \nD. Detail-Oriented \n Please type in A, B, C or D:  ")
    while answer8.lower() != "a" and answer8.lower() != "b" and answer8.lower() != "c" and answer8.lower() != "d":
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

    answer9 = input("\nA. Persistent \nB. Inspirational \nC. Peacemaker \nD. Analytical \n Please type in A, B, C or D:  ")
    while answer9.lower() != "a" and answer9.lower() != "b" and answer9.lower()!= "c" and answer9.lower() != "d":
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
    
    #Print Results
    time.sleep(2.0)
    print("\nTime for results!")
    time.sleep(2.0)

    if (a > (b and c and d)): #if choice a was selected the most
        print("\nYou selected 'A' the most! \nYou are a natural born leader. You may be a boss at work, super decisive and love to solve problems! \nYou may be very confident and self-reliant, leading you to take charge when no one else will.")
        time.sleep(2.0)
        print("Some of your natural strengths may include: Achievement driven, Gets results, Independent, Risk-taker, Takes initiative, and Persistent!")
        time.sleep(3.0)
        print("\nSomeone who shares this personality type is Freddie Mercury band Queen! That's pretty badass.")
        time.sleep(1.0)
        print("\nHere are Queen's top tracks from Spotify: ")
        time.sleep(1.0)

        #starting mixer
        mixer.init()    
        mixer.music.load("queen.mp3")
        mixer.music.set_volume(0.7)

        print("\n1. Another One Bites The Dust \n2. Bohemian Rhapsody \n3. Don't Stop Me Now \n4. Under Pressure \n5. We Will Rock You ")
        #play the top track
        mixer.music.play()

        #loop for ability to pause, resume, or exit the music
        while True:
            print("Press 'p' to pause the preview and 'r' to resume")
            print("Or press 'e' to exit")
            button = input("  ")
            
            if button == 'p':
        
                #pause the music
                mixer.music.pause()     
            elif button == 'r':
        
                #resume the music
                mixer.music.unpause()
            elif button == 'e':
        
                #stop the music
                mixer.music.stop()
                break

    elif (b > (a and c and d)): #if choice b was selected the most
        print("\nYou selected 'B' the most! \nYou are like an excitable, fun-seeking, cheerleader! You might be great at motivating others. \nYou may also succeed in an enviornment where you can talk. You can be very loving and encouraging, paired with a desire to be the center of attention.")
        time.sleep(2.0)
        print("Some of your strengths may include: Enthusiastic, Optimistic, Emotional and Passionate, and Personal!")
        time.sleep(3.0)
        print("\nSomeone who shares this personality type is Bob Dylan.")
        time.sleep(1.0)
        print("\nHere are Bob Dylan's top tracks from Spotify: ")
        time.sleep(1.0)

        #starting mixer
        mixer.init()    
        mixer.music.load("bobdylan.mp3")
        mixer.music.set_volume(0.7)

        print("\n1. Knockin' On Heavens's Door \n2. Like a Rolling Stone \n3. Blowin' in the Wind \n4. Hurricane \n5. The Times They Are A-Changing")
        #play the top track
        mixer.music.play()

        #loop for ability to pause, resume, or exit the music
        while True:
            print("Press 'p' to pause the preview and 'r' to resume")
            print("Or press 'e' to exit")
            button = input("  ")
            
            if button == 'p':
        
                #pause the music
                mixer.music.pause()     
            elif button == 'r':
        
                #resume the music
                mixer.music.unpause()
            elif button == 'e':
        
                #stop the music
                mixer.music.stop()
                break

    #Music

    elif (c > (a and b and d)):
        print("\nYou selected 'C' the most!\nYou are more than likely a people pleaser. Which isn't a bad thing! You're incredibly loyal to those you enjoy.\nYou might be a great listener, empathetic, and a wonderful encourager!")
        time.sleep(2.0)
        print("Some of your strengths may include: Patient, Easy-going, Stable, Team player, and Reliable.")
        time.sleep(3.0)
        print("\nSomeone who shares this personality type is Taylor Swift.")
        time.sleep(1.0)
        print("\nHere are Taylor Swift's top tracks from Spotify: ")
        time.sleep(1.0)

        #starting mixer
        mixer.init()    
        mixer.music.load("taylorswift.mp3")
        mixer.music.set_volume(0.7)

        print("\n1. All Too Well (10 Minute Version) (Taylor's Version) \n2. Red (Taylor's Version) \n3. Wildest Dreams (Taylors Version) \n4. All Too Well (Taylor's Version) \n5. Nothing New (feat. Phoebe Bridgers) (Taylor's Version)")
        
        #play the top track
        mixer.music.play()
    
        #loop for ability to pause, resume, or exit the music
        while True:
            print("Press 'p' to pause the preview and 'r' to resume")
            print("Or press 'e' to exit")
            button = input("  ")
            
            if button == 'p':
        
                #pause the music
                mixer.music.pause()     
            elif button == 'r':
        
                #resume the music
                mixer.music.unpause()
            elif button == 'e':
        
                #stop the music
                mixer.music.stop()
                break

    elif (d > (a and b and c)):
        print("\nYou selected 'D' the most!\nYou are a rule-follower. You have a strong need to do things the correct way. \nYou probably read the instruction manuals.")
        time.sleep(2.0)
        print("Some of your strengths may include: Accurate, Analytical, Orderly, High standards.")
        time.sleep(3.0)
        print("\nSomeone who shares this personality type is Alan Jackson.")
        time.sleep(1.0)
        print("\nHere is Alan Jackson's top tracks from Spotify: ")
        time.sleep(1.0)
        print("\n1. Chattahoochee \n2. Freight Train \n3. It's Five O'Clock Somewhere \n4. Little Betty \n5. Country Boy")
    #Music

    
    
if __name__ == "__main__":
    main()