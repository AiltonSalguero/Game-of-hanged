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
   /|\  =========''']


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
       
if __name__ == "__main__":
    selectWork = WORK[ran()]

    # for target_list in expression_list:  
    print(len(selectWork))
    


