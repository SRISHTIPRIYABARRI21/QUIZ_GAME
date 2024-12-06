print("Welcome to the my computer quiz!")

playing = input("Do you want to play? ")

text = "SrishtI is gReat! "
print(text.lower())

if  playing != "yes":
    quit()

print("okay! Let's play:)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
    
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit ":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stands for? ").lower()
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question correct")
print("You got " + str((score / 4) * 100) + " %.")

