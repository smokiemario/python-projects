
name = input('What is your name, please?')

print("Hello " + name)

old = input('How old are you?')

print("You said you are " + old)

oldfriend = input('How old is your friend?')

print("Your friend is " + oldfriend)

totalage = int(old) + int(oldfriend)

print(totalage)

totaldays = (365.242 * totalage)

print("your total days alive is " + str(totaldays))
