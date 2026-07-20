import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses +=1
    a= int(input("guess a number: "))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
    else:
        print("correct!")

print(f"you have guessed the number {n} correctly in {guesses} attempts")
