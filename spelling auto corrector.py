
from textblob import TextBlob
i="x"
while i=="x":
    words=input("Enter Any Words ")
    print("Wrong Words:",words)
    correct=TextBlob(words)
    print("Correct Words:",correct.correct())
    i=input("Press x to auto correct another word or Press Any Other Key for Exit:")


