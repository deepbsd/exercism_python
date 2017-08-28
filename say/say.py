#!/usr/bin/env python3

import subprocess

def say(num):
    up2_20 = { 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
            10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 
            18:'eighteen', 19:'nineteen', 20: 'twenty'}
    ten_100 = { 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety' }


    def millions(n1, n2): return n1+' million '+n2
    def billions(n1, n2): return n1+' billion '+n2
    def trillions(n1, n2): return n1+' trillion '+n2

    def lt20(num):
        return up2_20[num]

    def twtyto100(num):
        s1 = int(str(num)[0])
        s2 = int(str(num)[1:])
        if num in [20, 30, 40, 50, 60, 70, 80, 90]:
            return "{}".format(ten_100[s1])
        else:
            return "{}-{}".format(ten_100[s1], up2_20[s2])

    def hundreds(num):
        s1 = int(str(num)[0])
        s2 = int(str(num)[1:]) 
        if s2 <= 20:
            s2 = lt20(s2)
        elif s2 > 20:
            s2 = twtyto100(s2)
        if num in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            return "{} hundred".format(up2_20[s1])
        else:
            return "{} hundred and {}".format(up2_20[s1], s2)

    def thousands(num):
        s1 = int(str(num)[:-3])
        s2 = int(str(num)[-3:])
        #print(s1, ' ', s2)
        if num in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]:
            return "{} thousand".format(up2_20[s1])
        elif num >= 10000:
            s1 = callit(s1)
            if callit(s2) != 'zero':
                s2 = callit(s2)
            else:
                s2 = ''
            return "{} thousand {}".format(s1, s2).rstrip()
        else:
            s1 = callit(s1)
            s2 = callit (s2)
            return "{} thousand {}".format(s1, s2)


           


    def callit(num):
        if num <= 20:
            return up2_20[num]
        if (num > 20) and (num < 100):
            return twtyto100(num)
        if (num >= 100) and (num < 1000):
            return hundreds(num)
        if (num >= 1000) and (num < 1000000):
            return thousands(num)



    return callit(num)





if __name__ == "__main__":

    number = say(10234)

    print(number)

    subprocess.call(["say", "{}".format(number)])

