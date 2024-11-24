import random
op = ["parchment", "boulder", "shears"]
print("I challenge you to a duel!")
print("Of parchment, boulder, and shears!")
prs = input("Parchment, boulder, or shears?: ").lower() 
comp = random.choice(op)
print("Computer chose:", comp)
if comp == prs:
    print("A draw!")
elif (prs == "boulder" and comp == "shears") or \
     (prs == "shears" and comp == "parchment") or \
     (prs == "parchment" and comp == "boulder"):
    print("You win!")
else:
    print("Computer wins!")