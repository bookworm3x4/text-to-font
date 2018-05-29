# converts text to font
# Emmett Wald
# 23 May 2018

# import font dictionary
from font1 import *

# prompt user for text input
def getInput():
    '''print("What is your message?")
    print("(Enter on multiple lines; use a blank line to finish.)")
    message = ''''''
    while addOn != '':
        addOn = input("> ")
        message += addOn'''
    text = input("What is your message? ").upper()
    return text

# convert font character strings into lists
def unpackFont():
    for character in font:
        rows = font[character].split("\n")
        rows = rows[1:]
        font[character] = rows
    return font

# convert message to font
def convertToFont(text):
    message = [""] * height
    for i in range(height):
        for character in text:
            try:
                message[i] += font[character][i]
            except:
                message[i] += font["missing"][i]
    return message

# print message
def printMsg(message):
    print()
    for line in message:
        print(line)

# main function
def main():
    text = getInput()
    font = unpackFont()
    message = convertToFont(text)
    printMsg(message)

main()
