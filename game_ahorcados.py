import random
WORK = ["hola", "juan", "carro", "carrera", "computadora"]
WORKEXIST = []
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
   /    |
        |
        =========''','''

    +---+
    |   |
    O   |
    |   |
   /|   |
        |
        =========''','''

    +---+
    |   |
    O   |
    |   |
   /|\  |
        |
        =========''','''

    +---+
    |   |
    O   |
    |   |
   /|\  |
    |   |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
   /|\  |
    |   |
   /    =========''', '''

    +---+
    |   |
    O   |
    |   |
   /|\  |
    |   |
   / \  =========''']

lifes = 0

def ran():
    num = random.randint(0,len(WORK)-1)
    exits = False
    # workNum.append(num)
    for x in WORKEXIST:
        if x == num:
            exits = True
        
    if exits:
        return False
    else: 
        WORKEXIST.append(num)
        return num

def newWork():
    selectWork = WORK[ran()]
    showBoxWork = "["
    line = "* --- " * len(selectWork)

    for i in selectWork:  
        showBoxWork += "'_', "

    showBoxWork += "]"
    line += "*"

    print(IMAGES[lifes])
    print("\n")
    print(showBoxWork)
    print(line)
    insertWork(selectWork)
   

def insertWork(selectWork):
     while True:
        inputText = input("Choose a letter: ")
        if len(inputText) < 2 and len(inputText) > 0:
            verific(inputText, selectWork)
            break
        else:
            print("The entry is incorrect. Please add only one letter.")

def verific(text, selectWork):
    global lifes
    while True:
        workPosition = []
        count = 0

        for i in selectWork:
            if(i == text):
                workPosition.append(count)
            count += 1

        if (lifes+1) >= (len(IMAGES)-1):
            print("GAME OVER")
            break
        elif len(workPosition) < 1:
           lifes += 1
           print(IMAGES[lifes])
           insertWork(selectWork)
           break
        else:
            print("sigue")
            break


def revealLetters(positions, char):
    print("paso")
    pass


if __name__ == "__main__":
    newWork()


