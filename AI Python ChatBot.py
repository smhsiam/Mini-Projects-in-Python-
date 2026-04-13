#Rule Based AI Python ChatBot 

import datetime
import time

name= input("As-salamu alaykum, Enter your name : ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11: 
    print("Good Morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good Evening, ", name)
else:
    print("Good Night, ", name)



print("As-salamu alaykum! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "Hello": "Hi, welcome. How can I help you?",
    "How are you": "I am very fine. Thank you",
    "Who are you": "I am smart AI chatbot",
    "Motivate me": "Keep going. Every bug of your project makes you a better developer",
    "Happy": "Great to hear that",
    "What are functions": "Tell me about a Software Developers life?."
} 

# Method/Function to get response of ChatBot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I will learn this soon"    
    

# Take user input 


while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break