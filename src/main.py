from .prompt_pipeline import prompt_pipeline


intro_message = (
    "\nDobrý den. Jmenuji se Adéla a jsem chatbot ve společnosti Nestlé. "
    "Ráda vám poradím s hledáním práce v naší společnosti nebo s otázkami, "
    "které máte o společnosti Nestlé. S čím vám dnes můžu pomoct?"
)
goodbye_message = (
    "\nDěkujeme za chatování se společností Nestlé. V případě dalších otázek "
    "kontaktujte Nestlé na tel. č. 123 456 789. Nashledanou!"
)


def main():
    # main logic of the application

    # the bot introduces itself
    print(intro_message)

    # main loop
    # get user input
    while True:
        prompt = input("\nNapište vaši otázku nebo 'stop' na ukončení chatu: ")
        # stop the chat and say goodbye
        if prompt.lower() == "stop":
            print(goodbye_message)
            break
        # or get system response
        response = prompt_pipeline(prompt)
        print(f"\n{response}")


if __name__ == "__main__":
    main()

