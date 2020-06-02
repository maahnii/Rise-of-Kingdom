#!/usr/bin/env python
def set_base_stats(civ):
    ##############################################################
    #                                                            #
    # function takes in civilization name and assigns base stats #
    # Currently only for T5 builds                               #
    ##############################################################
    base = default_stats()
    #infantry Civilizations
    if civ == 'Rome':
        base[0] = 221
        base[1] = 222
        base[2] = 216
    if civ == 'Japan':
        base[0] = 232
        base[1] = 212
        base[2] = 216
    if civ == 'France':
        base[0] = 221
        base[1] = 212
        base[2] = 227
    #Calvary Civilizations
    if civ == 'Germany':
        base[3] = 220
        base[4] = 217
        base[5] = 222
    if civ == 'Spain':
        base[3] = 232
        base[4] = 212
        base[5] = 216
    if civ == 'Arabia':
        base[3] = 227
        base[4] = 212
        base[5] = 222
    if civ == 'Byzantium':
        base[3] = 221
        base[4] = 222
        base[5] = 216
    #Archer Civilizations
    if civ == 'Ottoman':
        base[6] = 227
        base[7] = 216
        base[8] = 216
    if civ == 'Britain':
        base[6] = 232
        base[7] = 216
        base[8] = 211
    if civ == 'China':
        base[6] = 227
        base[7] = 222
        base[8] = 212
    if civ == 'Korea':
        base[6] = 221
        base[7] = 227
        base[8] = 212
    return base

def default_stats():
    #Function sets base stats with no expertise
    return [220,212,216,220,212,216,220,216,212,220,216,212]
