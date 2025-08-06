print("This program will help you decide if a character is an \
uppercase or lowercase character or is a Digit.")
char=input("Enter the character :... ")
if char>="A" and char<="Z":
          print(char,"is an Uppercase character.")
elif char>="a" and char<="z":
          print(char,"is a Lowercase character.")
elif char>="0" and char<="9":
          print(char,"is a Digit.")
else:
          print(char,"is a Special Character.")
