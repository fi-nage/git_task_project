import random

# Function to generate a random color in RGB format
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
while True:
    # Taking input from the user
    userInput = input("Please enter something: ")

    if userInput.lower() == 'exit':
        print("Exiting the program...")
        break

    # Printing the input provided by the user with random colors for each letter
    coloredOutput = ""
    for letter in userInput:
        r, g, b = randomColor()
        coloredOutput += f"\033[38;2;{r};{g};{b}m{letter}\033[0m"  # ANSI escape sequence for color
    print("You entered:", coloredOutput)
