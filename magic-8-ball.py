from random import randint
from my_libs import labelmaker

response_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
again = True

print("\n\n\n" + labelmaker.create_label(["Welcome to my 'Magic 8 ball™' program!", "", "Instructions:", "1. Type your question", "2. Press 'RETURN' on your keyboard", "3. Read the advice that the 'Magic 8 Ball™' gives you", "It's as easy as that!"], top_text="Magic 8 ball™"))

while again:
    input("\nQuestion: ")
    print("The all-knowing 'Magic 8 Ball™'s answer: " + response_list[randint(0, len(response_list)-1)] + "\n")

    want_again = input("Do you want to ask another question? (Y/N)\n").lower()
    if want_again == "y" or want_again == "yes":
        again = True
    else:
        again = False