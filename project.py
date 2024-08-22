print("enter a character")
c=input()
if c>="0" and c<="9":
    print(c," is a number")
elif c>="a" and c<="z":
    print(c, "is an alphabet")
elif c>="A" and c<="Z":
    print(c, "is an alphabet")
else:
    print("it is neither a number nor an alphabet")