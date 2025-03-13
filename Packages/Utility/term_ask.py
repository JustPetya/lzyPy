class TermAsk:
    def __init__(self, message: str):
        self.message = message

    def add_option(self, option: str, callback: callable, char: bool = False) -> None: 
        """Adds an option to the parser
        
        Parameters
        ----------
        option: str, required
            The option that is displayed and checked for on the input.

        callback: callable, required
            The callback that is invoked when the option was selected.

        char: bool, optional
            Enables if the first character is also a valid answer. (Use only if unique)
        """
        self.options[option] = {
            "callback": callback,
            "char": char
        }

    def compose(self) -> None:
        """
        Composes the string for the user input
        """
        options = []
        for name, option in self.options.items():
            if option["char"]:
                t = f"[{name[0]}]{name[1:]}"
            else:
                t = name

            options.append(t)

        self.output = f"{self.message} ({"/".join(options)}) "
    
    @staticmethod
    def test_output() -> bool:
        obj: TermAsk = TermAsk("Yes?").add_option("Yes", lambda: None).add_option("No", lambda: None, char=True).compose()
        
        if obj.output == "Yes? (Yes/[N]o) ":
            return True
        else:
            return False
        
    def question(self, ask_again: bool = False) -> None:
        """
        Asks the question in the terminal and calls the callbacks.

        Parameters
        ----------
        ask_again: bool, optional
            Asks again if no valid answer was given
        """
        user_input = input(self.output).lower()

        for name, option in self.options.items():
            if name.lower() == user_input:
                option["callback"]()
                break
            
            if option["char"]:
                if name[1:].lower() == user_input:
                    option["callback"]()
                    break

        print("No valid option was selected!")

        if ask_again:
            self.question(True)

if __name__=="__main__":
    print("Not able to run by itself at this point!")
