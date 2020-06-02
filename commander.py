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
        self.attack_buffs([])
        self.defense_buffs([])
        self.health_buffs([])
        self.rally_buffs([])
        self.skill_buffs([])
        self.counter_buffs([])
    
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
        if civ == 'Rome':
            self.defense_buffs([5,0,0])
        if civ == 'Germany':
            self.attack_buffs([0,5,0])
        if civ == 'Britain':
            self.attack_buffs([0,0,5])
        if civ == 'France':
            self.health_buffs([3,3,3])
        if civ == 'Spain':
            self.defense_buffs([0,5,0])
        if civ == 'China':
            self.defense_buffs([3,3,3])
        if civ == 'Japan':
            self.attack_buffs([3,3,3])
        if civ == 'Korea':
            self.defense_buffs([0,0,5])
        if civ == 'Arabia':
            self.attack_buffs([0,5,0])
            self.rally_buffs(5)
        if civ == 'Ottoman':
            self.health_buffs([0,0,5])
            self.skill_buffs(5)
        if civ == 'Byzantium':
            self.health_buffs([0,5,0])
            
        self.civ = civ
        
    def attack_buffs(self,buffs):
        if buffs == []:
            self.buffs_ia = 0
            self.buffs_ca = 0
            self.buffs_aa = 0
        else:
            self.buffs_ia += buffs[0]
            self.buffs_ca += buffs[1]
            self.buffs_aa += buffs[2]
    
    def defense_buffs(self,buffs):
        if buffs == []:
            self.buffs_id = 0
            self.buffs_cd = 0
            self.buffs_ad = 0
        else:
            self.buffs_id += buffs[0]
            self.buffs_cd += buffs[1]
            self.buffs_ad += buffs[2]
    
    def health_buffs(self,buffs):
        if buffs == []:
            self.buffs_ih = 0
            self.buffs_ch = 0
            self.buffs_ah = 0
        else:
            self.buffs_ih += buffs[0]
            self.buffs_ch += buffs[1]
            self.buffs_ah += buffs[2]
    
    def rally_buffs(self,buffs):
        if buffs == []:
            self.buffs_rally = 0
        else:
            self.buffs_rally += buffs
            
    def skill_buffs(self,buffs):
        if buffs == []:
            self.buffs_skill = 0
        else:
            self.buffs_skill += buffs
    
    def counter_buffs(self,buffs):
        if buffs == []:
            self.buffs_counter = 0
        else:
            self.buffs_counter += buffs
    

stats = [0,1,2,3,4,5,6,7,8,9,10,11]

kevin = Character(stats)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally)
kevin.civilization('Arabia')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally)
