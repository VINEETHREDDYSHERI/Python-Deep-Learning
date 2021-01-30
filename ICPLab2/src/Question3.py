# Function that will return Dictionary with words as key and wordCount as the value
def createWordCountDict():
    inputFile = open("wordCountInput.txt", "r")  # Opening the file in read mode
    currentLine = inputFile.readline().replace("\n", "")  # Removing newline when reading the line of a file
    wordCountDict = dict()
    while currentLine != "":  # iterating the loop until currentLine variable is empty
        for word in currentLine.split(" "):  # iterating over all the words in the currentLine variable
            if word in wordCountDict.keys():  # checking if word is already is present if so incrementing its value by 1
                wordCountDict[word] = wordCountDict[word] + 1
            else:
                wordCountDict[word] = 1  # adding the word and its value to dictionary
        currentLine = inputFile.readline()  # reading the next Line
    return wordCountDict


# Function that will write word and its wordCount to the wordCountOutput.txt File
def writeWordCountToFile(wordCountDict):
    outPutFile = open("wordCountOutput.txt", "w")  # Opening the file in write mode
    inputFile = open("wordCountInput.txt", "r")  # Opening the file in read mode
    currentLine = inputFile.readline().replace("\n", "")  # Removing newline when reading the line of a file
    while currentLine != "":  # iterating the loop until currentLine variable is empty
        for word in currentLine.split(" "):  # iterating over all the words in the currentLine variable
            if word in wordCountDict.keys():   # checking if word is present in dictionary
                wordData = str(word) + ": " + str(wordCountDict[word]) + "\n"
                outPutFile.write(wordData)  # writing the word and its count to the file in new line
                wordCountDict.pop(word)  # removing the word from the dictionary
        currentLine = inputFile.readline()  # reading the next Line


wordCount = createWordCountDict()  # Function returns wordCount of each word in Dictionary
writeWordCountToFile(wordCount)  # Function that writes the word and its wordCount to the wordCountOutput.txt File
