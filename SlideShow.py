
class SlidShow:
    def __init__(self):
        self.textfileread()
        self.makelside()

    def textfileread(self):
        global lines
        with open('mp1.txt') as f:
            lines = f.readlines()

        for i in lines:
            print(i[0])


    def makelside(self):
        status = False
        c = 0
        p = 0

        f = open("mp.txt","w")

        for i in lines:

            if status == True and i[0] == "v":
                f.write(i)
                status = False

            if i[0] == "v":
                status = True
                p = c

            c += 1

        f.close()




main = SlidShow()



