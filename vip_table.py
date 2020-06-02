#!/usr/bin/env python
def set_vip_buffs(vip):
    ##############################################################
    #                                                            #
    # function takes in vip level and assigns buff stats         #
    # Currently for version 10003414_113937:p1928004:17603256    #
    ##############################################################
    base = default_stats()

    if vip == 11:
        base[0] = 5         #Attack + 5
        base[3] = 5
        base[6] = 5
        base[9] = 5
        return base
    elif vip == 12:
        base[0] = 5         #Attack/Defense +5
        base[3] = 5
        base[6] = 5
        base[9] = 5
        base[1] = 5
        base[4] = 5
        base[7] = 5
        base[10] = 5
        return base
    elif (vip == 13) | (vip == 14) | (vip == 15) | (vip == 16):
        base[0] = 5         #Attack/Defense/Health +5
        base[1] = 5
        base[2] = 5
        base[3] = 5
        base[4] = 5
        base[5] = 5
        base[6] = 5
        base[7] = 5
        base[8] = 5
        base[9] = 5
        base[10] = 5
        base[11] = 5
        return base
    elif vip == 17:
        base[0] = 10       #Attack/Defense/Health/All Damage +5
        base[1] = 5
        base[2] = 5
        base[3] = 10
        base[4] = 5
        base[5] = 5
        base[6] = 10
        base[7] = 5
        base[8] = 5
        base[9] = 10
        base[10] = 5
        base[11] = 5
        base[12] = 5
        base[14] = 5
        return base
    else:
        return base
 
def default_stats():
    #Function sets base stats with no expertise
    #[ia,id,ih,ca,cd,ch,aa,ad,ah,sa,sd,sh,skill,rally,counter]
    return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
