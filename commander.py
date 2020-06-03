#!/usr/bin/env python
from character_profile import Character

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
            
    
    

primary = 'Richard'
secondary = 'Charles'
build_Richard = [1,0,0,0]
build_Charles = [1,0,0,0]
tech = [70,70,40,70,70,40,70,70,40]
alliance_tech = [15,15,0,15,15,0,15,15,0]
titles = [0,0,0,0,0,0,0,0,0]
holy_sites = [6,6,5,6,6,5,6,6,5]
building = [2,2,6,2,2,6,2,2,6]
vip = 15
troop_amount = 200000



kevin = Character('Ottoman')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
#kevin.civilization('Germany')
#print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.city_theme_buffs('No Place Like Home')
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.technology_buffs(tech)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.alliance_buffs(alliance_tech)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.alliance_buffs(holy_sites)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.building_buffs(building)
print(kevin.aa,kevin.sh,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
kevin.vip_buffs(vip)
print(kevin.aa,kevin.ad,kevin.ah,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
print(kevin.buffs_ia,kevin.buffs_id,kevin.buffs_ih,kevin.buffs_ca,kevin.buffs_cd,kevin.buffs_ch,kevin.buffs_aa,kevin.buffs_ad,kevin.buffs_ah,kevin.buffs_skill,kevin.buffs_rally,kevin.buffs_counter)
kevin.change_civ('Germany')
print(kevin.aa,kevin.ad,kevin.ah,kevin.buffs_ca,kevin.buffs_id,kevin.buffs_skill,kevin.buffs_rally,kevin.ca)
print(kevin.buffs_ia,kevin.buffs_id,kevin.buffs_ih,kevin.buffs_ca,kevin.buffs_cd,kevin.buffs_ch,kevin.buffs_aa,kevin.buffs_ad,kevin.buffs_ah,kevin.buffs_skill,kevin.buffs_rally,kevin.buffs_counter)
