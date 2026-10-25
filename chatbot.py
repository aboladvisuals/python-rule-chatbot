replies ={
    "hello": "Hi. I only answer the messages I was given.",
    "hi": "Hi. I only answer the messages I was given.",
    "help": "Try: hello, name, python, data, or quit.",
    "name": "I am a rule-based bot. I do not learn.",
    "python": "Python is the language this bot is written in.",
    "data": "Data work starts by checking the question before you trust the answer.",
}

while True:
    text= input("YOU: ").strip().lower()
    if text == "quit":
        print ("Bot: GoodBye.")
        break
    if text in replies:
        print("Bot:", replies[text])
    else:
        print("Bot: I dont know that, try help!")
