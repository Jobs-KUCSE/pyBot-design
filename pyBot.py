#---Main----

print("\n\nSystem: you need---\n\t\t[1] Tutorial help")
print("\t\t[2] Programming help @@@ Under construction @@@")
print("\t\t[3] eBook")
print("\n\t\tEnter your choice -")

ch=input("You: ")

if int(ch) == 1 :
   print("\nSystem: Welcome to Tutorial help page\n\t\t Please search anything--")
   exec(open("pyBot-tutorials.py").read())
   
elif int(ch) == 2 :
   print("\nSystem: Welcome to Programming help page\n\t\t Please search anything--")
   
elif int(ch) == 3 :
   print("\nSystem: Welcome to Programming help page\n\t\t Please search anything--")
   exec(open("pyBot-ebooks.py").read())

else:
   print("-- Wrong input || Please try again --")
