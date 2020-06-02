#!/usr/bin/env python

class Richard:
    def __init__(self,build,level):
        #Initiate Richard with input of skills
        self.build = build
        self.level = level
    
    def attack(self):
        return
        

class Character:
    def __init__(self,stats):
        #Initiate a character and their base stats
        self.base_stats(stats)
    
    def base_stats(self,stats):
        #Base stats for character
        self.ia = stats[0]
        self.id = stats[1]
        self.ih = stats[2]
        self.ca = stats[3]
        self.cd = stats[4]
        self.ch = stats[5]
        self.aa = stats[6]
        self.ad = stats[7]
        self.ah = stats[8]
        self.sa = stats[9]
        self.sd = stats[10]
        self.sh = stats[11]
        
    def civilization(self,civ):
        self.civ = civ

stats = [0,1,2,3,4,5,6,7,8,9,10,11]

kevin = Character(stats)
print(kevin.aa,kevin.sh)
        
