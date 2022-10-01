import pyshorteners
import pyperclip
link = input("Enter the link : ")
shortener = pyshorteners.Shortener()
s = shortener.tinyurl.short(link)
# this will automatically copy the short link
pyperclip.copy(s)
print("\n-----------------------------------------------\n")
print("Short link : "+ s +"\n")
print(" ‎ ‎ ‎ ‎ Short link Copied to clipboard! ‎ ‎ ‎ ‎ ")
print("\n-----------------------------------------------")
