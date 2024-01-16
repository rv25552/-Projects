print("Welcome To Quiz:")
answer=input("Are You Ready To Dive Into The World Of Quiz:Yes/No :")
if answer=="N0" or "no" or "No":
    print("Thank You(|-)")
        
score=0
questions=5
if answer=="yes":
    answer=input("What is The Capital of India:")
    if answer=="delhi" or "Delhi":
        score=score+1
        print("Correct Answer")
    else:
        print("Wrong Answer")
    answer=input("What is The Full Form of WWW:")
    if answer=="World Wide Web "or "word wide web":
        score=score+1
        print("Correct Answer")
    else:
        print("Wrong Answer")
    answer=input("What is The Financial of India:")
    if answer=="Mumbai" or "mumbai":
        score=score+1
        print("Correct Answer")
    else:
        print("Wrong Answer")
    answer=input("Opposite of Good:")
    if answer=="Bad" or "bad":
        score=score+1
        print("Correct Answer")
    else:
        print("Wrong Answer")
    answer=input("What is The Capital of Maharashtra:")
    if answer=="Mumbai" or "mumbai":
        score=score+1
        print("Correct Answer")
    else:
        print("Wrong Answer")
print("Thank You")      
print("Your Correct Answer is ",score)
print("Play Again!")
