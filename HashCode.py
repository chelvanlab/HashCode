class Main:
    def __init__(self):
        self.textfileread()
        self.makelside()

    def textfileread(self):
        global lines,copy
        with open('mp3.txt') as f:
            lines = f.readlines()

        copy = lines

    def makelside(self):
        status = False
        c=p=0

        for i in lines:
            if status == True and i[0] == "V":
                copy[p+1] = i
                status = False

            if i[0] == "V":
                status = True
                del copy[c]
                p = c

            c+=1

        for i in copy:
            print(i)


Main()