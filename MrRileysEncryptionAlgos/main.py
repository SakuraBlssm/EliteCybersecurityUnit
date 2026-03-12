

# the dumbest one I could think of... remove all vowels
def rileySuperSecretEncrypt01(someWord):
    removals = "aeiouy"
    result = ""
    for eachLetter in someWord:
        if not eachLetter in removals:
            result += eachLetter
    return result


# substitute vowels and stuff
def rileySuperSecretEncrypt02(someWord):
    substitutions = {"a":"@", "e":"3", "i":"1", "o":"0", "b":"6", "g":"9", "s":"5", "t":"+"}
    result = ""
    for eachLetter in someWord:
        if eachLetter in substitutions:
            result += substitutions[eachLetter]
        else:
            result += eachLetter
    return result


# rotate vowels with recursion
def rileySuperSecretEncrypt03(someWord):
    if len(someWord) >= 16:
        return someWord
    substitutions = {"a":"ee", "e":"ii", "i":"oo", "o":"uu", "u":"aa", "r":"ss", "s":"tt", "t":"ss"}
    result = "*"
    for eachLetter in someWord:
        if eachLetter in substitutions:
            result += substitutions[eachLetter]
        else:
            result += eachLetter
    return rileySuperSecretEncrypt03(result) + "*"
    



def checkForCollisions(functionName):
    hasCollisions = False
    dictionaryOfHashes = {}
    with open("google-10000-english-no-swears.txt") as myFile:
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
    with open("google-10000-english-no-swears.txt") as myFile:
        for eachWord in myFile:
            # print(eachWord)
            encryptedWord = rileySuperSecretEncrypt01(eachWord.strip("\n"))
            print(encryptedWord)


# checkForCollisions(rileySuperSecretEncrypt01)

# checkForCollisions(rileySuperSecretEncrypt02)

# checkForCollisions(rileySuperSecretEncrypt03)

printEncryptedWords()