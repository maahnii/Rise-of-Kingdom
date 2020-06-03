#!/usr/bin/env python
def set_civ_buffs(civ):
    ##############################################################
    #                                                            #
    # function takes in civilization and assigns buff stats      #
    # Currently for version 10003414_113937:p1928004:17603256    #
    ##############################################################
    base = default_stats()

    if civ == 'Rome':
        base[1] = 5
        return base
    if civ == 'Germany':
        base[3] = 5
        return base
    if civ == 'Britain':
        base[6] = 5
        return base
    if civ == 'France':
        base[2] = 3
        base[5] = 3
        base[8] = 3
        return base
    if civ == 'Spain':
        base[4] = 5
        return base
    if civ == 'China':
        base[1] = 3
        base[4] = 3
        base[7] = 3
        return base
    if civ == 'Japan':
        base[0] = 3
        base[3] = 3
        base[6] = 3
        return base
    if civ == 'Korea':
        base[7] = 5
        return base
    if civ == 'Arabia':
        base[3] = 5
        base[13] = 5
        return base
    if civ == 'Ottoman':
        base[8] = 5
        base[12] = 5
        return base
    if civ == 'Byzantium':
        base[5] = 5
        return base


def default_stats():
    #Function sets base stats with no expertise
    #[ia,id,ih,ca,cd,ch,aa,ad,ah,sa,sd,sh,skill,rally,counter]
    return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
