#!/usr/bin/env python
def set_city_buffs(skin):
    ##############################################################
    #                                                            #
    # function takes in a city theme name and assigns buff stats #
    # Currently for version 10003414_113937:p1928004:17603256    #
    ##############################################################
    base = default_stats()

    if skin == 'Trick or Treat':
        base[0] = 5             #Infantry Attack +5
        base[8] = -5            #Archer Health   -5
        return base
    elif skin == 'Sowers Song':
        base[3] = 5             #Cavalry Attack  +5
        base[8] = -5            #Archer Health   -5
        return base
    elif skin == 'Silent Night':
        base[6] = 5             #Archer Attack   +5
        base[2] = -5            #Infantry Health -5
        return base
    elif skin == 'Cupids Arrow':
        base[2] = 5             #Infantry Health +5
        base[5] = -5            #Cavalry Health  -5
        return base
    elif skin == 'Spring Blossoms':
        base[5] = 5             #Cavalry Health  +5
        base[2] = -5            #Infantry Health -5
        return base
    elif skin == 'No Place Like Home':
        base[8] = 5             #Archer Health   +5
        base[5] = -5            #Cavalry Health  -5
        return base
    elif skin == 'Twilight Falls':
        base[12] = 5            #Skill Damage    +5
        base[0] = -10           #Infantry Attack -10
        return base
    elif skin == 'Babylonian Gardens':
        base[0] = 10            #Infantry Attack +10
        base[7] = -5            #Archer Defense  -5
        base[8] = -5            #Archer Health   -5
        return base
    elif skin == 'Frozen City':
        base[7] = 5             #Archer Defense  +5
        base[3] = -5            #Cavalry Attack  -5
        return base
    elif skin == 'Temple of Vishnu':
        base[2] = 5             #Infantry Health +5
        base[4] = -5            #Cavalry Defense -5
        return base
    elif skin == 'Heliopolis':
        base[0] = 3             #Troop Attack    +3
        base[3] = 3
        base[6] = 3
        base[7] = -10           #Archer Defense  -10
    elif skin == 'Gift of the Nile':
        base[6] = 5             #Archer Attack   +5
        base[1] = -5            #Infantry Defense-5
        return base
    elif skin == 'Magpie Bridge':
        base[5] = 5             #Cavalry Health  +5
        base[7] = -5            #Archer Defense  -5
        return base
    elif skin == 'Persian Dream':
        base[1] = 3             #Troop Defense   +3
        base[4] = 3
        base[7] = 3
        base[3] = -10           #Cavalry Attack  -10
        return base
    elif skin == 'Joyful Feast':
        base[1] = 5             #Infantry Defense+5
        base[4] = -5            #Cavalry Defense -5
        return base
    elif skin == 'Age of Devotion':
        base[2] = 10            #Infantry Health +10
        base[3] = -5            #Cavalry Attack  -5
        base[7] = -5            #Archer Defense  -5
        return base
    elif skin == 'Hidden Lotus':
        base[3] = 5             #Cavalry Attack +5
        base[7] = -5            #Archer Defense -5
        return base
    elif skin == 'Wailing Keep':
        base[0] = 5             #Infantry Attack +5
        base[5] = -5            #Cavalry Health  -5
        return base
    elif skin == 'Love and Thanks':
        base[7] = 5             #Archer Defense  +5
        base[1] = -5            #Infantry Defense-5
        return base
    elif skin == 'Divine Abode':
        base[4] = 10            #Cavalry Defense +10
        base[1] = -10           #Infantry Defense-10
        return base
    elif skin == 'Gingerbread House':
        base[2] = 5             #Infantry Health +5
        base[6] = -5            #Archer Attack   -5
        return base
    elif skin == 'Saints Halo':
        base[12] = 5            #Skill Damage    +5
        base[2] = -10           #Infantry Health -10
        return base
    elif skin == 'Swans Reverie':
        base[1] = 5             #Infantry Defense+5
        base[8] = -5            #Archer Health   -5
        return base
    elif skin == 'Temple of Karnak':
        base[5] = 5             #Cavalry Health  +5
        base[2] = -5            #Infantry Health -5
        return base
    elif skin == 'Lake Palace':
        base[1] = 3             #Troop Defense   +3
        base[4] = 3
        base[7] = 3
        base[5] = -10           #Cavalry Health  -10
        return base
    elif skin == 'Flight of the Heron':
        base[6] = 10            #Archer Attack   +10
        base[0] = -10           #Infantry Attack -10
        return base
    elif skin == 'Tears of the External':
        base[6] = 5             #Archer Attack   +5
        base[3] = -5            #Cavalry Attack  -5
    elif skin == 'Temple of Artemis':
        base[4] = 5             #Cavalry Defense +5
        base[0] = -5            #Infantry Attack -5
        return base
    elif skin == 'Timbered Ensemble':
        base[7] = 5             #Archer Defense  +5
        base[4] = -5            #Cavalry Defense -5
        return base
    elif skin == 'Amber Fortress':
        base[8] = 10            #Archer Health   +10
        base[1] = -5            #Infantry Defense-5
        base[4] = -5            #Cavalry Defense -5
        return base
    elif skin == 'Kings Cottage':
        base[1] = 5             #Infantry Defense+5
        base[3] = -5            #Cavalry Attack  -5
        return base
    elif skin == 'Mayan Mystery':
        base[1] = 10            #Infantry Defense+10
        base[3] = -10           #Cavalry Attack  -10
        return base
    elif skin == 'Dragon Boat Wish':
        base[7] = 5             #Archer Defense  +5
        base[5] = -5            #Cavalry Health  -5
    elif skin == 'Melk Abbey':
        base[5] = 10            #Cavalry Health  +10
        base[2] = -5            #Infantry Health -5
        base[8] = -5            #Archer Health   -5
        return base
    elif skin == 'Default':
        return base
    else:
        print('Did not find a corresponding theme.  Use one of the following valid themes: [Trick or Treat; Sowers Song; Silent Night; Cupids Arrow; Spring Blossoms; No Place Like Home; Twilight Falls; Babylonian Gardens; Frozen City; Temple of Vishnu; Heliopolis; Gift of the Nile; Magpie Bridge; Persian Dream; Joyful Feast; Age of Devotion; Hidden Lotus; Wailing Keep; Love and Thanks; Divine Abode; Gingerbread House; Saints Halo; Swans Reverie; Temple of Karnak; Lake Palace; Flight of the Heron; Tears of the Eternal; Temple of Artemis; Timbered Ensemble; Amber Fortress; Kings Cottage; Mayan Mystery; Dragon Boat Wish; Melk Abbey]')
    
        return base

def default_stats():
    #Function sets base stats with no expertise
    #[ia,id,ih,ca,cd,ch,aa,ad,ah,sa,sd,sh,skill,rally]
    return [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
