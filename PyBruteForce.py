import random
import pyautogui
import string


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNORQRSTUVWXYZ0123456789@#"

# chars = string.printable
chars_list = list(chars)


password = pyautogui.password("Enter password you wanna brute force : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print(str(guess_password))

    if(guess_password == list(password)):
        print("The password is : "+ "".join(guess_password))
        break