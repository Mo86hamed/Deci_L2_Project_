
# -- coding: utf-8 --





import pyttsx3
import time
import random
import turtle
# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to set the voice type
def set_voice():
    # Get available voices
        voices = engine.getProperty('voices')
    
    # Print available voices for user to choose
        for index, voice in enumerate(voices):
                print(f"{index + 1}. Voice ID: {voice.id}, Name: {voice.name}")

    # Prompt user to choose voice type
        print("\n")
        print("\n")
        print("\n")
        type_choice = input("What type of voice do you want? Enter the number: \n")

    # Set the selected voice based on user input
        try:
                choice_index = int(type_choice) - 1
                if 0 <= choice_index < len(voices):
                        engine.setProperty('voice', voices[choice_index].id)
                        print(f"Selected voice: {voices[choice_index].name}")
                else:
                        print("Invalid choice. Using default voice.")
        except ValueError:
                print("Invalid input. Using default voice.")


# Function to speak the provided text
def speak(text):
        engine.say(text)
        engine.runAndWait()


# Set the voice once
set_voice()

# Example usage
def story():
        print(""" 
                            ▀██                                     
        ▄▄▄ ▄▄▄ ▄▄▄   ▄▄▄▄   ██    ▄▄▄▄    ▄▄▄   ▄▄ ▄▄ ▄▄     ▄▄▄▄  
         ██  ██  █  ▄█▄▄▄██  ██  ▄█   ▀▀ ▄█  ▀█▄  ██ ██ ██  ▄█▄▄▄██ 
          ███ ███   ██       ██  ██      ██   ██  ██ ██ ██  ██      
           █   █     ▀█▄▄▄▀ ▄██▄  ▀█▄▄▄▀  ▀█▄▄█▀ ▄██ ██ ██▄  ▀█▄▄▄▀ """)

        name_list = ["Khalid", "Mohamed", "Ahmed", "Hamza", "Ali", "Zyad"]
        random_name = random.choice(name_list)
        print(f"Your total score is: [{score}]")
        speak(f"Your total score is: [{score}]")
        time.sleep(1)
        print(f"Your name is {random_name}")
        speak(f"Your name is {random_name}")
        time.sleep(1)
        print("You are in Dubai")
        speak("You are in Dubai")
        time.sleep(1)
        print("You are planning to travel with your family to Saudi Arabia.")
        speak("You are planning to travel with your family to Saudi Arabia.")
        time.sleep(1)
        print("You suggested that you will travel by ship")
        speak("You suggested that you will travel by ship")
        time.sleep(1)
        print("And it starts to move")
        speak("And it starts to move")
        time.sleep(1)
        print("But the ship was defective and no one knew that it was defective")
        speak("But the ship was defective and no one knew that it was defective")
        time.sleep(1)
        print("In the middle of the sea, while everyone is asleep.")
        speak("In the middle of the sea, while everyone is asleep.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("The ship's crew announces that it has discovered a breach in the ship")
        speak("The ship's crew announces that it has discovered a breach in the ship")
        time.sleep(1)
        print("Panic and fear filled the place and the ship's crew tried to calm the situation")
        speak("Panic and fear filled the place and the ship's crew tried to calm the situation")
        time.sleep(1)
        print("The crew started to solve the problem")
        speak("The crew started to solve the problem")
        time.sleep(1)
        print("The passengers started to feel calm")
        speak("The passengers started to feel calm")
        time.sleep(1)
        print("After a period of time, you and the passengers started to sleep")
        speak("After a period of time, you and the passengers started to sleep")
        time.sleep(1)
        print("You woke up terrified")
        speak("You woke up terrified")
        time.sleep(1)
        print("You hear screaming from the rooms around you")
        speak("You hear screaming from the rooms around you")
        time.sleep(1)
        print("Wait....what")
        speak("Wait....what")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("The ship is sinking")
        speak("The ship is sinking")
        time.sleep(2)

        # After the ship sinking
        time.sleep(2)
        print("After a lot of effort and risk, you were able to leave the room")
        speak("After a lot of effort and risk, you were able to leave the room")
        time.sleep(2)
        print("You are thinking ")
        speak("You are thinking ")
        time.sleep(1)
        print(f"What would you do {random_name}")
        speak(f"What would you do {random_name}")
        time.sleep(1)
        print("What would you do")
        speak("What would you do")
        time.sleep(1)
        print("Then you found an idea and you have 3 choices")
        speak("Then you found an idea and you have 3 choices")
        time.sleep(2)
        print("1--You will help yourself")
        print("2--You will try to help your family")
        print("3--You will try to help the largest number of passengers")
        speak("You know what would you do")

# Choosing the story event
def choice_story():
        while True:
                choice = input("Enter your choice [1, 2, or 3]: ")
                speak("Enter your choice [1, 2, or 3]:\n ")
                if choice in ["1", "2", "3"]:
                        return choice
                else:
                        print("Invalid choice, please try again.")
                        speak("Invalid choice, please try again.")

# Choices in the story
def choices1(score, turns):
                        global choice
                        choice = choice_story()
                        turns += 0
                        if choice == '1':
                                score += 20
                                time.sleep(2)
                                print("After thinking")
                                speak("After thinking")
                                time.sleep(1)
                                print("You chose that you will help yourself")
                                speak("You chose that you will help yourself")
                                time.sleep(1.5)
                                print("You found the lifeboat 🚤🚤")
                                speak("You found the lifeboat 🚤🚤")
                                time.sleep(1)
                                print("After doing your best, you managed to survive")
                                speak("After doing your best, you managed to survive")
                                time.sleep(1.5)
                                print("After a period of time, you fainted")
                                speak("After a period of time, you fainted")
                                time.sleep(1)
                                print("It's the morning")
                                speak("It's the morning")
                                time.sleep(1)
                                print("The sun is rising and you woke up from your sleep because of the sun")
                                speak("The sun is rising and you woke up from your sleep because of the sun")
                                time.sleep(2)
                                print("Your total score is: [20]")
                                speak("Your total score is: [20]")
                                time.sleep(1)
                                print("You started exploring the lifeboat")
                                speak("You started exploring the lifeboat")
                                time.sleep(1)
                                print("You found that you have enough food, water, and soft drinks enough for one person for two weeks.")
                                speak("You found that you have enough food, water, and soft drinks enough for one person for two weeks.")
                                time.sleep(2)
                                print("You are stuck in the middle of the sea")
                                speak("You are stuck in the middle of the sea")
                                time.sleep(1)
                                print("You don't know what you would do if the food runs out")
                                speak("You don't know what you would do if the food runs out")
                                time.sleep(2)
                                print("Day after day, food and water began to run out")
                                speak("Day after day, food and water began to run out")
                                time.sleep(1.5)
                                print("Two weeks have passed")
                                speak("Two weeks have passed")
                                time.sleep(1)
                                print("Food and water are completely gone")
                                speak("Food and water are completely gone")
                                time.sleep(1)
                                print("After thinking a lot")
                                speak("After thinking a lot")
                                time.sleep(1)
                                print("You start to look around you!")
                                speak("You start to look around you!")
                                time.sleep(1)
                                print("You found a fishing rod and net")
                                speak("You found a fishing rod and net")
                                time.sleep(1)
                                print("All day you are trying to catch fish.")
                                speak("All day you are trying to catch fish.")
                                time.sleep(1)
                                print("At the last moment and before giving up, you finally catch a fish")
                                speak("At the last moment and before giving up, you finally catch a fish")
                                time.sleep(2)
                                print("You cooked it and started to eat happily")
                                speak("You cooked it and started to eat happily")
                                time.sleep(1)
                                print("You fell asleep")
                                speak("You fell asleep")
                                time.sleep(1)
                                print("You woke up thirsty")
                                speak("You woke up thirsty")
                                time.sleep(1)
                                print("But you remembered that at the beginning of the day you had found tools to desalinate seawater")
                                speak("But you remembered that at the beginning of the day you had found tools to desalinate seawater")
                                time.sleep(2)
                                print("The next day, you look for a ship or somebody who might help you!")
                                speak("The next day, you look for a ship or somebody who might help you!")
                                time.sleep(2)
                                score += 40
                                print("You found a ship.!! 🚢⚓")
                                speak("You found a ship.!! 🚢⚓")
                                time.sleep(1)
                                print("You are shouting [helooooo... hellooooo]")
                                speak("You are shouting [helooooo... hellooooo]")
                                time.sleep(1)
                                print("Shouting [ can anybody hear me.. Hellooooo!!]")
                                speak("Shouting [ can anybody hear me.. Hellooooo!!]")
                                time.sleep(1)
                                print("You remembered that you have found a flare gun!!")
                                speak("You remembered that you have found a flare gun!!")
                                time.sleep(1)
                                print("But remember you have just 3 bullets")
                                speak("But remember you have just 3 bullets")
                                time.sleep(1)
                                print("Reloading..!!")
                                speak("Reloading..!!")
                                time.sleep(1)
                                print("Reloading..!!")
                                speak("Reloading..!!")
                                
                                time.sleep(1)
                                print("Fireee!!")
                                speak("Fireee!!")
                                time.sleep(1)
                                print("Reloading!.!")
                                speak("Reloading!.!")
                                time.sleep(1)
                                print("Fire!..!")
                                speak("Fire!..!")
                                time.sleep(1)
                                print("Wait, you have used 2 bullets from 3")
                                speak("Wait, you have used 2 bullets from 3")
                                time.sleep(1)
                                print("You have just one bullet")
                                speak("You have just one bullet")
                                time.sleep(1)
                                print("Thinking what would you do")
                                speak("Thinking what would you do")
                                time.sleep(1)
                                print("You have just 2 choices")
                                speak("You have just 2 choices")
                                time.sleep(1)

                                last_bullet = input("""Either the first choice 1: you won't shoot the last bullet
                        Or
                        the second choice 2: you will try your last chance and shoot it\n""")

                                if last_bullet == "1":
                                        time.sleep(2)
                                        print("For your bad luck, the ship has gone without you")
                                        speak("For your bad luck, the ship has gone without you")
                                        time.sleep(1.5)
                                        print("Soon....and after a month")
                                        speak("Soon....and after a month")
                                        time.sleep(1)
                                        print("For your good luck, another ship passed by you")
                                        speak("For your good luck, another ship passed by you")
                                        time.sleep(1)
                                        print("You took the chance, reloaded your bullet, and finally the ship's crew saw you and helped you 🚢⚓👨‍✈")
                                        speak("You took the chance, reloaded your bullet, and finally the ship's crew saw you and helped you ")
                                        time.sleep(2)
                                        score += 40
                                        print("Congratulations, you win! 🎉🎉")
                                        speak("Congratulations, you win! ")
                                        time.sleep(1)
                                        print(f"Your score is: [{score}]")
                                        speak(f"Your score is: [{score}]")

                                elif last_bullet == "2":
                                        time.sleep(2)
                                        print("You have shot it")
                                        speak("You have shot it")
                                        time.sleep(1)
                                        print("But no one hears you, no one sees you")
                                        speak("But no one hears you, no one sees you")
                                        time.sleep(1)
                                        print("Now you are alone in the middle of the sea, only darkness and cold")
                                        speak("Now you are alone in the middle of the sea, only darkness and cold")
                                        time.sleep(1)
                                        print("The lifeboat has gone farther and farther into the ocean")
                                        speak("The lifeboat has gone farther and farther into the ocean")
                                        time.sleep(1)
                                        print("You don't know what you would do")
                                        speak("You don't know what you would do")
                                        time.sleep(2)
                                        print("You don't know what to be afraid of: the dark, the cold, loneliness, ocean monsters, madness, or... or what")
                                        speak("You don't know what to be afraid of: the dark, the cold, loneliness, ocean monsters, madness, or... or what")
                                        time.sleep(2)
                                        print("Now you lost everything and you don't have anything to lose")
                                        speak("Now you lost everything and you don't have anything to lose")
                                        time.sleep(1)
                                        print("Finally, you died")
                                        speak("Finally, you died")
                                        time.sleep(1)
                                        score -= 40
                                        print("Sorry, you lose 😭😭")
                                        speak("Sorry, you lose ")
                                        time.sleep(1)
                                        print(f"Your score is: [{score}]")
                                        speak(f"Your score is: [{score}]")


        # Run the story













#here you try to help your family





                # choice = choice_story()
                
                        elif choice == "2":
                                                        print("after thinking")
                                                        speak("after thinking")
                                                        time.sleep(1)
                                                        print("you chose that you will help your family ")
                                                        speak("you chose that you will help your family ")
                                                        time.sleep(1)
                                                        print("you found the lifeboat⛵🚤")
                                                        speak("you found the lifeboat")
                                                        time.sleep(1)
                                                        print("After doing your best, you and your family managed to survive")
                                                        speak("After doing your best, you and your family managed to survive")
                                                        time.sleep(1)
                                                        print("after period of time")
                                                        speak("after period of time")
                                                        time.sleep(1)
                                                        print("you and your family fainted")
                                                        speak("you and your family fainted")
                                                        time.sleep(1)
                                                        print("it's the morning")
                                                        speak("it's the morning")
                                                        time.sleep(1)
                                                        print("the sun is rising and You and your family woke up from your sleep, cause of the sun")
                                                        speak("the sun is rising and You and your family woke up from your sleep, cause of the sun")
                                                        time.sleep(1)
                                                        print("your score is [40] ")
                                                        speak("your score is [40] ")
                                                        time.sleep(1)
                                                        print("You started exploring the lifeboat")
                                                        speak("You started exploring the lifeboat")
                                                        time.sleep(1)
                                                        print("you found that you have enough food, water and soft drinks Enough for you and your family for 5 days.")
                                                        speak("you found that you have enough food, water and soft drinks Enough for you and your family for 5 days.")
                                                        time.sleep(1)
                                                        print("You are stuck in the middle of the sea")
                                                        speak("You are stuck in the middle of the sea")
                                                        time.sleep(1)
                                                        print("you don't know what would you do if the The food is over")
                                                        speak("you don't know what would you do if the The food is over")
                                                        time.sleep(1)
                                                        print("Day after day, food and water began to run out")
                                                        speak("Day after day, food and water began to run out")
                                                        time.sleep(1)
                                                        print("5 days have passed")
                                                        speak("5 days have passed")
                                                        time.sleep(1)
                                                        print("Food and water are completely gone")
                                                        speak("Food and water are completely gone")
                                                        time.sleep(1)
                                                        print("after thinking a lot")
                                                        speak("after thinking a lot")
                                                        time.sleep(1)
                                                        print("you start to give a look around you!")
                                                        speak("you start to give a look around you!")
                                                        time.sleep(1)
                                                        print("you found Fishing rod and net")
                                                        speak("you found Fishing rod and net")
                                                        time.sleep(1)
                                                        print("all the day you and your family are trying to catch fish.")
                                                        speak("all the day you and your family are trying to catch fish.")
                                                        time.sleep(2)
                                                        print("you and your family made a great job,,you cached a lot of fish")
                                                        speak("you and your family made a great job,,you cached a lot of fish")
                                                        time.sleep(2)
                                                        print("you cooked it and you start to eat the fish with your family happily")
                                                        speak("you cooked it and you start to eat the fish with your family happily")
                                                        time.sleep(2)
                                                        print("you felt asleep")
                                                        speak("you felt asleep")
                                                        time.sleep(1)
                                                        print("you waked up cause of thirsty")
                                                        speak("you waked up cause of thirsty")
                                                        time.sleep(1)
                                                        print("you found your brother desalinate sea water")
                                                        speak("you found your brother desalinate sea water")
                                                        time.sleep(1)
                                                        print("you saw your brother is awake ")
                                                        speak("you saw your brother is awake ")
                                                        time.sleep(1)
                                                        print("you felt proud of your brother")
                                                        speak("you felt proud of your brother")
                                                        score += 40

                                                        time.sleep(1)
                                                        
                                                        print("soon.....a big shark attacked you")
                                                        speak("soon.....a big shark attacked you")
                                                        time.sleep(1)
                                                        print("no one expected that")
                                                        speak("no one expected that")
                                                        time.sleep(1)
                                                        print("and it bite your ship")
                                                        speak("and it bite your ship")
                                                        time.sleep(1)
                                                        print("all of you were feel fear")
                                                        speak("all of you were feel fear")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        predestination = input("you have two choices : 1 - don't help your family and wait till it go 2 - you will attack it and try to help you family\n")
                                                        predestination = speak("you have two choices : 1 - don't help your family and wait till it go 2 - you will attack it and try to help you family")
                                                        if predestination == "1":
                                                                time.sleep(2)
                                                                print("you choose that you won't help your family")
                                                                speak("you choose that you won't help your family")
                                                                time.sleep(1)
                                                                print("the shark keep attacking you")
                                                                speak("the shark keep attacking you")
                                                                time.sleep(1)
                                                                print("the shark disappointed and went away from you")
                                                                speak("the shark disappointed and went away from you")
                                                                time.sleep(1)
                                                                print("but 80 % of your boat is damaged")
                                                                speak("but 80 % of your boat is damaged")
                                                                time.sleep(1)
                                                                print("and your boat started to sink")
                                                                speak("and your boat started to sink")
                                                                time.sleep(1)
                                                                print("soon....One after another began to die")
                                                                speak("soon....One after another began to die")
                                                                time.sleep(1)
                                                                print("in the end , all of are died")
                                                                speak("in the end , all of are died")
                                                                time.sleep(1)
                                                                score -= 40
                                                                
                                                                print("sorry , you lose😭😭")
                                                                speak("sorry , you lose")
                                                                print(f"your score is : [{score}]")
                                                                speak(f"your score is : [{score}]")
                                                                


                                                        elif predestination == "2":
                                                                time.sleep(2)
                                                                print("you choose you will attack it and try to help you family")
                                                                speak("you choose you will attack it and try to help you family")
                                                                time.sleep(1)
                                                                print("you are fighting it .... fight and fight")
                                                                speak("you are fighting it .... fight and fight")
                                                                time.sleep(1)
                                                                print("until you have killed it")
                                                                speak("until you have killed it")
                                                                time.sleep(1)
                                                                print("all of your family are proud of you")
                                                                speak("all of your family are proud of you")
                                                                time.sleep(1)
                                                                print("you have damaged a lot") 
                                                                speak("you have damaged a lot") 
                                                                
                                                                time.sleep(1)
                                                                print("the next day and you are give a look for a ship or somebody who might help you!")
                                                                speak("the next day and you are give a look for a ship or somebody who might help you!")
                                                                time.sleep(2)
                                                                print("you found a ship.!! ")
                                                                speak("you found a ship.!! ")
                                                                time.sleep(1)
                                                                print("you are shouting [hellooooo... hellooooo]")
                                                                speak("you are shouting [hellooooo... hellooooo]")
                                                                time.sleep(1)
                                                                print("shouting [ can any body hear me.. Hellooooo!!]")
                                                                speak("shouting [ can any body hear me.. Hellooooo!!]")
                                                                time.sleep(1)
                                                                print("you remembered that you have found a flare gun!!")
                                                                speak("you remembered that you have found a flare gun!!")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print("reloading..!!")
                                                                speak("reloading..!!")
                                                                time.sleep(2)
                                                                print(".")
                                                                time.sleep(2)
                                                                print(".")
                                                                time.sleep(2)
                                                                print(".")
                                                                time.sleep(2)
                                                                print("fireee!!")
                                                                speak("fireee!!")
                                                                time.sleep(1)
                                                                print("the ship's crew saw you and they started to help you🚢🚢🚢")
                                                                speak("the ship's crew saw you and they started to help you🚢🚢🚢")
                                                                time.sleep(1)
                                                                score += 50
                                                                time.sleep(2)
                                                                print("Congratulations!!! You win🎉🎉🎊")
                                                                speak("Congratulations!!! You win")
                                                                time.sleep(2)
                                                        print(f"your score is : [{score}]")
                                                        speak(f"your score is : [{score}]")





#here you try to help the largest number of passengers




                
                
                # choice = choice_story()


                        elif choice == "3":
                                                        time.sleep(2)
                                                        print("after thinking")
                                                        speak("after thinking")
                                                        time.sleep(1)
                                                        print("you chose that You will try to help The largest number of passengers ")
                                                        speak("you chose that You will try to help The largest number of passengers ")
                                                        time.sleep(1)
                                                        print("you found the lifeboat⛵🚤")
                                                        speak("you found the lifeboat")
                                                        time.sleep(1)
                                                        print("After doing your best, you and other passengers managed to survive")
                                                        speak("After doing your best, you and other passengers managed to survive")
                                                        time.sleep(1)
                                                        print("after period of time")
                                                        speak("after period of time")
                                                        time.sleep(1)
                                                        print("you fainted")
                                                        speak("you fainted")
                                                        time.sleep(1)
                                                        print("it's the morning")
                                                        speak("it's the morning")
                                                        time.sleep(1)
                                                        print("the sun is rising and You woke up from your sleep, cause of the sun")
                                                        speak("the sun is rising and You woke up from your sleep, cause of the sun")
                                                        time.sleep(2)
                                                        print("your_total_score_is : [30] ")
                                                        speak("your_total_score_is : [30] ")
                                                        time.sleep(1)
                                                        print("You started exploring the lifeboat")
                                                        speak("You started exploring the lifeboat")
                                                        time.sleep(1)
                                                        print("you found that you have enough food, water and soft drinks Enough for you and your family for 2 days.")
                                                        speak("you found that you have enough food, water and soft drinks Enough for you and your family for 2 days.")
                                                        time.sleep(2)
                                                        print("You are stuck in the middle of the sea")
                                                        speak("You are stuck in the middle of the sea")
                                                        time.sleep(1)
                                                        print("you don't know what would you do if the The food is over")
                                                        speak("you don't know what would you do if the The food is over")
                                                        time.sleep(2)
                                                        print("Day after day, food and water began to run out")
                                                        speak("Day after day, food and water began to run out")
                                                        time.sleep(2)
                                                        print("2 days have passed")
                                                        speak("2 days have passed")
                                                        score += 70
                                                        time.sleep(1)
                                                        print("Food and water are completely gone")
                                                        speak("Food and water are completely gone")
                                                        time.sleep(1)
                                                        print("after thinking a lot")
                                                        speak("after thinking a lot")
                                                        time.sleep(1)
                                                        print("you start to give a look around you!")
                                                        speak("you start to give a look around you!")
                                                        time.sleep(1)
                                                        print("you found Fishing rod and net")
                                                        speak("you found Fishing rod and net")
                                                        time.sleep(1)
                                                        print("all the day you and other passengers are trying to catch fish.")
                                                        speak("all the day you and other passengers are trying to catch fish.")
                                                        time.sleep(2)
                                                        print("you and other passengers made a great job,,you cached a lot of fish")
                                                        speak("you and other passengers made a great job,,you cached a lot of fish")
                                                        time.sleep(2)
                                                        print("you cooked it and you start to eat the fish with your family happily")
                                                        speak("you cooked it and you start to eat the fish with your family happily")
                                                        time.sleep(2)
                                                        print("you felt asleep")
                                                        speak("you felt asleep")
                                                        time.sleep(1)
                                                        print("you waked up cause of thirsty")
                                                        speak("you waked up cause of thirsty")
                                                        time.sleep(1)
                                                        print("you found some one desalinate sea water")
                                                        speak("you found some one desalinate sea water")
                                                        time.sleep(1)
                                                        print("you and some passengers gave a look around you")
                                                        speak("you and some passengers gave a look around you")
                                                        time.sleep(2)
                                                        print("wait you see a land near to you")
                                                        speak("wait you see a land near to you")
                                                        time.sleep(1)
                                                        print("every one is happy , and start to move to this land")
                                                        speak("every one is happy , and start to move to this land")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print(".")
                                                        time.sleep(1)
                                                        print("it was very beautiful land")
                                                        speak("it was very beautiful land")
                                                        time.sleep(1)
                                                        print("some one said : WOW")
                                                        speak("some one said : WOW")
                                                        time.sleep(1)
                                                        print("but some one of you sees a monster")
                                                        speak("but some one of you sees a monster")
                                                        time.sleep(1)
                                                        print("every one feel fear ")
                                                        speak("every one feel fear ")
                                                        time.sleep(1)
                                                        monster = input("""you have two choice: 1 - you and the other men won't do anything 
                                                                        or
                                                                        2 - you will try with the other men to kill this monster""")
                                                        if monster == "1":
                                                                time.sleep(2)
                                                                print("all of were feel fear")
                                                                speak("all of were feel fear")
                                                                time.sleep(1)
                                                                print("the monster start to attack you")
                                                                speak("the monster start to attack you")
                                                                time.sleep(1)
                                                                print("some of you try to fight it but all of them died")
                                                                speak("some of you try to fight it but all of them died")
                                                                time.sleep(1)
                                                                print("some of you try to escape")
                                                                speak("some of you try to escape")
                                                                time.sleep(1)
                                                                print("but a lot of you died ")
                                                                speak("but a lot of you died ")
                                                                time.sleep(1)
                                                                print("and some of you escaped")
                                                                speak("and some of you escaped")
                                                                time.sleep(1)
                                                                
                                                                score -= 70
                                                                time.sleep(1)
                                                                print("sorry , you lose😭😭")
                                                                speak("sorry , you lose")
                                                                time.sleep(1)
                                                                print(f"your score is : [{score}]")
                                                                speak(f"your score is : [{score}]")
                                                                

                                                        elif monster == "2":
                                                                time.sleep(2)
                                                                print("you and the other men start to attack at the same time")
                                                                speak("you and the other men start to attack at the same time")
                                                                time.sleep(2)
                                                                print("some of died just 1 or 2")
                                                                speak("some of died just 1 or 2")
                                                                time.sleep(1)
                                                                print("but finally you killed it")
                                                                speak("but finally you killed it")
                                                                time.sleep(1)
                                                                
                                                                print("you and other men made a great effort to kill the monster")
                                                                speak("you and other men made a great effort to kill the monster")
                                                                time.sleep(1)
                                                                
                                                                print("then all of you started to make houses and plant fruits")
                                                                speak("then all of you started to make houses and plant fruits")
                                                                time.sleep(1)
                                                                print("soon.......you think why you don't write on the beach big 'S.O.S' word ")
                                                                speak("soon.......you think why you don't write on the beach big 'S.O.S' word ")
                                                                time.sleep(2)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                
                                                                time.sleep(1)
                                                                print("after a year an airplane was flying across the land")
                                                                speak("after a year an airplane was flying across the land")
                                                                time.sleep(1.5)
                                                                print("for your luck they saw you")
                                                                speak("for your luck they saw you")
                                                                time.sleep(1)
                                                                print("soon you  saw the helicopter came to help you")
                                                                speak("soon you  saw the helicopter came to help you")
                                                                
                                                                score += 80
                                                                time.sleep(1)
                                                                print(".")
                                                                time.sleep(1)
                                                                print(".")
                                                                
                                                                time.sleep(1)
                                                                
                                                                
                                                                print("congratulation , you win🎇🧨🎉🎊🎁🎀")
                                                                speak("congratulation , you win")
                                                                time.sleep(2)
                                                        print(f"your score is : [{score}]")
                                                        speak(f"your score is : [{score}]")
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                        else:
                                                        time.sleep(1)
                                                        print("you didn't choose any option , enter the true syntax😡😡")
                                                        speak("you didn't choose any option , enter the true syntax")
                                                        # choices1(score,turns)
                                                        choice_story()
                                                                
                                
                                                        
                                # turns += 1
                                        # Print current score and turns
                        print(f"Score: {score}, Turns: {turns}\n")
                        speak(f"Score: {score}, Turns: {turns}\n")

                                                        # Check if game over conditions are met
                        if score >= 150:  # Game ends if score reaches 100
                                                print("Game Over! You won!")
                                                speak("Game Over! You won!")
                                                

                        # elif score < 150:
                        #                 print("Game Over! You didn't reach the goal this time.")
                        #                 speak("Game Over! You didn't reach the goal this time.")
                                
                                



#do you want to play again



                        return score , turns

score,turns = 0,0
# set_voice()
story()
# choices1()
# score, turns = choices1(score, turns)
import turtle

# Set up your screen
screen = turtle.Screen()
screen.title("Thank You for Playing ❤")
screen.bgcolor("white")
screen.setup(width=800, height=600)  

# turtle draw text
text_turtle = turtle.Turtle()
text_turtle.color("black")
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(0, 200)  
text_turtle.write("Thank you for playing ❤", align="center", font=("Arial", 24, "normal"))

# another turtle
heart_turtle = turtle.Turtle()
heart_turtle.color("red")
heart_turtle.pensize(3)
heart_turtle.penup()
heart_turtle.goto(0, -150)  
heart_turtle.pendown()


def draw_heart(t):
        t.begin_fill()
        t.left(140)
        t.forward(224)
        for _ in range(200):
                t.right(1)
                t.forward(2)
        t.left(120)
        for _ in range(200):
                t.right(1)
                t.forward(2)
        t.forward(224)
        t.end_fill()

# Draw the heart
draw_heart(heart_turtle)


heart_turtle.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()

def repeat():
        score = 0
        turns = 0

        while True:
                score, turns = choices1(score, turns)
        


                restart = input("Do you want to restart? 1. Yes 2. No:🙂🙂 \n")
                if restart.lower() in ["yes","no", "1", "2"]:
                        break
                else:
                        print("please enter only 1 or 2😡😡")

        if restart.lower() == "yes" or  restart.lower() == "1":
                print("Restarting game")
                # speak()
                # speak()
                story()
                
                choice_story()
                choices1(0,0)
                repeat()

                
        elif restart.lower() == "2" or  restart.lower() == "2":
                # else:
                print("Exiting game")
                return
                
                
                
                
# speak(next)
story()
# choice_story()

choices1(0,0)



repeat()




