class Character:
    def __init__(self,fname,lname,occupation):
        self.fname = fname
        self.lname = lname
        self.occupation = occupation

class Player:
    def __init__(self): #dunder => double underscores
        self.fname = ""
        self.lname = ""
        self.number = ""

if __name__ == '__main__':
    p1=Character("Reiden","Ei","lancer")
    p2=Character("mona","","mage")
    print(p2.occupation)
    print(p1.fname)
    print(p1.occupation)


    p1a=Player()
    p1a.fname = "Jirachot"
    p1a.lname = "Saonram"
    p1a.number = "023"
    p2a=Player()
    p2a.fname = "Somchi"
    p2a.lname = "Goboy"
    p2a.number = "011"
    print(p1a.fname)
    print(p2a.number)

    
