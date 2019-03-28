import random
import copy

d1 = ["Ross", "Austin", "Thomas", "Kurt", "Nick"]
d2 = ["Eric", "Matt", "Logan", "Danny", "Graeme"]
rivalry = [("Ross", "Eric"), ("Austin", "Graeme"), ("Kurt", "Danny"), ("Matt", "Logan"), ("Thomas", "Nick")]
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12"]
base_schedule = {"Week 1": [],
                 "Week 2": [],
                 "Week 3": [],
                 "Week 4": [],
                 "Week 5": [],
                 "Week 6": [],
                 "Week 7": [],
                 "Week 8": [],
                 "Week 9": [],
                 "Week 10": [],
                 "Week 11": [],
                 "Week 12": [],
                 "Week 13": [("Ross", "Eric"), ("Austin", "Graeme"), ("Kurt", "Danny"),
                             ("Matt", "Logan"), ("Thomas", "Nick")]}


def add_game(schedule, week):
    teams = d1 + d2
    for game in schedule[week]:
        home, away = game
        teams.remove(home)
        teams.remove(away)
    schedule[week].append((teams[0], teams[1]))


def in_division(name1, name2):
    if name1 in d1:
        if name2 in d1:
            return True
    if name1 in d2:
        if name2 in d2:
            return True
    return False


def check_rivalry(name1, name2):
    for riv in rivalry:
        if name1 in riv and name2 in riv:
            return True


def check_games(schedule, name1, name2):
    cnt = 0
    for week in schedule.keys():
        for game in schedule[week]:
            if name1 in game and name2 in game:
                cnt += 1
    return cnt


def check_week(week, name1, name2):
    for game in week:
        if name1 in game or name2 in game:
            return True
    return False


def game(schedule, name, opp, played):
    temp_weeks = weeks[:]
    while check_games(schedule, name, opp) < played:
        c = random.choice(temp_weeks)
        if check_week(schedule[c], name, opp):
            temp_weeks.remove(c)
        else:
            schedule[c].append((name, opp))
            temp_weeks.remove(c)
            if len(schedule[c]) is 4:
                add_game(schedule, c)


def pretty_print(schedule):
    for week in weeks:
        print week
        for home, away in schedule[week]:
            print home + " v. " + away
    print "Week 13"
    for home, away in schedule["Week 13"]:
        print home + " v. " + away


def run():
    schedule = copy.deepcopy(base_schedule)
    for name in d1:
        for opp in d1:
            if not(name is opp):
                game(schedule, name, opp, 2)
        for opp in d2:
            game(schedule, name, opp, 1)
    for name in d2:
        for opp in d2:
            if not(name is opp):
                game(schedule, name, opp, 2)
        for opp in d1:
            game(schedule, name, opp, 1)
    pretty_print(schedule)


while True:
    try:
        run()
        break
    except IndexError:
        print "Fail"
