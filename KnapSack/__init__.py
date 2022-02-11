import random
import math
from typing import List, Any, Union
from otree.api import *

def moonroverfun(startx,starty,first,second,third,fourth,fifth):

    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    x =      [8, 8, 8, 7, 7, 7, 5, 2, 1, 4]
    y =      [7, 4, 1, 8, 6, 3, 2, 3, 8, 9] # stratford y coord changed from 10 to 9
    points = [1, 1, 2, 2, 1, 2, 4, 3, 3, 5]
    #sites = ['Plains', 'Boulder', 'Rocks', 'Cliffs', 'Water', 'Life', 'Volcano', 'Mountain', 'Crater', 'Electromagnetic']
    sites = ['Barking','Pier','Shooters Hill','East Ham','Beckton','Woolwich','Greenwich','Millwall','Bow','Stratford']
    ifirst = sites.index(first)
    isecond = sites.index(second)
    ithird = sites.index(third)
    ifourth = sites.index(fourth)
    ififth = sites.index(fifth)

    yourpoints = points[ifirst]

    if isecond is not ifirst:
        yourpoints = yourpoints + points[isecond]

    if ithird is not isecond:
        if ithird is not ifirst:
            yourpoints = yourpoints + points[ithird]

    if ifourth is not ithird:
        if ifourth is not isecond:
            if ifourth is not ifirst:
                yourpoints = yourpoints + points[ifourth]

    if ififth is not ifourth:
        if ififth is not ithird:
            if ififth is not isecond:
                if ififth is not ifirst:
                    yourpoints = yourpoints + points[ififth]

    yourdist = distance(startx,starty,x[ifirst],y[ifirst]) + \
               distance(x[ifirst],y[ifirst],x[isecond],y[isecond]) + \
               distance(x[isecond],y[isecond],x[ithird],y[ithird]) + \
               distance(x[ithird],y[ithird],x[ifourth],y[ifourth]) + \
               distance(x[ifourth],y[ifourth],x[ififth],y[ififth])

    return [yourpoints, yourdist]


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url="Test"
    num_rounds = 1

    item_1_weight = 10
    item_2_weight = 20
    item_3_weight = 30
    item_4_weight = 40
    item_5_weight = 50
    item_6_weight = 1
    item_7_weight = 2
    item_8_weight = 3
    item_9_weight = 4
    item_10_weight = 5

    item_1_value = 100
    item_2_value = 200
    item_3_value = 300
    item_4_value = 400
    item_5_value = 500
    item_6_value = 10
    item_7_value = 20
    item_8_value = 30
    item_9_value = 40
    item_10_value = 50

    T_Weight = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    startx = models.IntegerField()
    starty = models.IntegerField()
    firstsite = models.StringField(blank=True)
    secondsite = models.StringField(blank=True)
    thirdsite = models.StringField(blank=True)
    fourthsite = models.StringField(blank=True)
    fifthsite = models.StringField(blank=True)
    points = models.IntegerField(blank=True)













class Travelling_Salesman(Page):
    form_model = 'player'
    form_fields = ['startx','starty','firstsite','secondsite','thirdsite','fourthsite','fifthsite','points']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        [yourpoints, yourdist] = moonroverfun(player.startx, player.starty, player.firstsite, player.secondsite, player.thirdsite, player.fourthsite, player.fifthsite)

        if yourdist > 10:
            player.points = 0
        else:
            player.points = yourpoints








class TS_Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        [yourpoints, yourdist] = moonroverfun(player.startx, player.starty, player.firstsite, player.secondsite, player.thirdsite, player.fourthsite, player.fifthsite)

        text2 = ""
        if yourdist > 10:
            text = 'Unfortunately the distance was more than allowed for the drone, therefore your answer cannot be accepted. Go ahead and try again.'
        else:
            if yourpoints < 12 and yourpoints > 9:
                text = "Close! The maximum profit you could achieve is £12,000. Go ahead and try again!"
            elif yourpoints <= 9:
                text = "You could do better, go ahead and try again!"
            else:
                text = "Congratulations! You achieved the maximum profit."

        return {
            'startx': player.startx,
            'starty': player.starty,
            'firstsite': player.firstsite,
            'secondsite': player.secondsite,
            'thirdsite': player.thirdsite,
            'fourthsite': player.fourthsite,
            'fifthsite': player.fifthsite,
            'text': text,
            'dist': yourdist,
            'points': yourpoints,
            'profit': '£' + str(yourpoints) + ',000'
        }






class KnapSack(Page):
    pass



class Maze(Page):
    pass





class knapsack(Page):
    pass
















page_sequence = [
    KnapSack

]
