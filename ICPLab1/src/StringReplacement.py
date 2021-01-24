# Taking input from the User
sentence = input("Enter the Sentence: ")
# By replace function
print("Output Sentence by replace function: ", sentence.replace("python", "pythons"))

# By looping over all the words that separated by space
resultantSentence = ""
for word in sentence.split(" "):
    if word == "python":
        resultantSentence = resultantSentence + " " + word + "s"
    else:
        resultantSentence = resultantSentence + " " + word

print("Output Sentence by iterating over the words in sentence: ", resultantSentence)
