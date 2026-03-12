

# the dumbest one I could think of... remove all vowels
def rileySuperSecretEncrypt01(word):
    removals = "aeiouy"
    result = ""
    for eachLetter in word:
        if not eachLetter in removals:
            result += eachLetter
    return result


# substitute vowels and stuff
def rileySuperSecretEncrypt02(word):
    substitutions = {"a":"@", "e":"3", "i":"1", "o":"0", "b":"6", "g":"9", "s":"5", "t":"+"}
    result = ""
    for eachLetter in word:
        if eachLetter in substitutions:
            result += substitutions[eachLetter]
        else:
            result += eachLetter
    return result


# rotate vowels with recursion
def rileySuperSecretEncrypt03(word):
    if len(word) >= 64 or len(word) == 0:
        return word
    substitutions = {"a":"ei", "e":"io", "i":"ou", "o":"ua", "u":"ae", "r":"st", "s":"tr", "t":"rs"}
    result = word[-1]
    for eachLetter in word:
        if eachLetter in substitutions:
            result += substitutions[eachLetter]
        else:
            result += eachLetter
    return rileySuperSecretEncrypt03(result) + word[0]
    

# this is just for testing as more words get added to bigListOfWords.txt
def checkForDuplicatesInWordList():
    dictionaryOfWords = {}
    with open("bigListOfWords.txt") as myFile:
        for eachWord in myFile:
            if eachWord in dictionaryOfWords:
                # already in the dictionary?
                dictionaryOfWords[eachWord] += 1
                # print("OOPS " + eachWord + " is already in the dictionaryOfWords", end =" / ")
                # return
            else:
                # add to dictionaryOfHashes and set it to 1 appearance
                dictionaryOfWords[eachWord] = 1
    # print("no duplicates")
    with open("words.txt", "w") as f:
        for key in dictionaryOfWords:
            f.write(key)



# param functionName - the function that will be tested for collisions
# for example, checkForCollisions(rileySuperSecretEncrypt01)
def checkForCollisions(functionName):
    hasCollisions = False
    dictionaryOfHashes = {}
    with open("bigListOfWords.txt") as myFile:
        for eachWord in myFile:
            # get each encrypted version
            encryptedWord = functionName(eachWord.strip("\n"))
            if encryptedWord in dictionaryOfHashes:
                # already in the dictionary?
                dictionaryOfHashes[encryptedWord] += 1
                print("OOPS " + encryptedWord + " is already in the dictionaryOfHashes", end =" / ")
                hasCollisions = True
            else:
                # add to dictionaryOfHashes and set it to 1 appearance
                dictionaryOfHashes[encryptedWord] = 1
    if hasCollisions:
        #print(dictionaryOfHashes)
        print("\nFAIL: we have collisions")
    else:
        print("\nSUCCESS: no collisions")
                



def printEncryptedWords():
    with open("bigListOfWords.txt") as myFile:
        for eachWord in myFile:
            # print(eachWord)
            encryptedWord = rileySuperSecretEncrypt01(eachWord.strip("\n"))
            print(encryptedWord)



# checkForCollisions(functionName = rileySuperSecretEncrypt01)

# checkForCollisions(functionName = rileySuperSecretEncrypt02)

# checkForCollisions(functionName = rileySuperSecretEncrypt03)

# printEncryptedWords()

# print(rileySuperSecretEncrypt03("Hello World"))
print("Hello World")