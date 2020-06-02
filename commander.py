#!/usr/bin/env python

from base_stats_table import set_base_stats
from city_themes import set_city_buffs

class Richard:
    def __init__(self,build,level):
        #Initiate Richard with input of skills
        self.build = build
        self.level = level
    
    def attack(self):
        return
        
class March:
    def __init__(self,primary,secondary,troop):
        self.primary = primary
        self.secondary = secondary
        self.troop = troop

class Character:
    def __init__(self,civ):
        #Initiate a character and their base stats
        self.attack_buffs([])
        self.defense_buffs([])
        self.health_buffs([])
        self.rally_buffs([])
        self.skill_buffs([])
        self.counter_buffs([])
        self.civilization(civ)
        
    def building_buffs(self,skin):
        buffs = set_city_buffs(skin)
        self.defense_buffs([buffs[1],buffs[4],buffs[7]])
        self.attack_buffs([buffs[0],buffs[3],buffs[6]])
        self.health_buffs([buffs[2],buffs[5],buffs[8]])
        self.rally_buffs(buffs[13])
        self.skill_buffs(buffs[12])
        
    def technology_buffs(self,tech):
        self.defense_buffs([tech[1],tech[4],tech[7]])
        self.attack_buffs([tech[0],tech[3],tech[6]])
        self.health_buffs([tech[2],tech[5],tech[8]])
    
    def alliance_buffs(self,tech):
        self.defense_buffs([tech[1],tech[4],tech[7]])
        self.attack_buffs([tech[0],tech[3],tech[6]])
        self.health_buffs([tech[2],tech[5],tech[8]])
    
    
    def titles(self,title):
        self.defense_buffs([title[1],title[4],title[7]])
        self.attack_buffs([title[0],title[3],title[6]])
        self.health_buffs([title[2],title[5],title[8]])

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
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Germany':
            self.attack_buffs([0,5,0])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Britain':
            self.attack_buffs([0,0,5])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'France':
            self.health_buffs([3,3,3])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Spain':
            self.defense_buffs([0,5,0])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'China':
            self.defense_buffs([3,3,3])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Japan':
            self.attack_buffs([3,3,3])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Korea':
            self.defense_buffs([0,0,5])
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Arabia':
            self.attack_buffs([0,5,0])
            self.rally_buffs(5)
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Ottoman':
            self.health_buffs([0,0,5])
            self.skill_buffs(5)
            base = set_base_stats(civ)
            self.base_stats(base)
        if civ == 'Byzantium':
            self.health_buffs([0,5,0])
            base = set_base_stats(civ)
            self.base_stats(base)
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
            
    
    

primary = 'Richard'
secondary = 'Charles'
build_Richard = [1,0,0,0]
build_Charles = [1,0,0,0]
tech = [70,70,40,70,70,40,70,70,40]
alliance_tech = [15,15,0,15,15,0,15,15,0]
titles = [0,0,0,0,0,0,0,0,0]
troop_amount = 200000



kevin = Character('Arabia')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.civilization('Germany')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.building_buffs('Hidden Lotus')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.technology_buffs(tech)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.alliance_buffs(alliance_tech)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
