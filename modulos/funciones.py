def generate (names, goals, goals_avoided, assists):
    statistics = []
    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        statistics.append((name, goal, goal_avoided, assist))
    return statistics

def max_scorer(statistics):
    max_goals_player = max(statistics, key=lambda x: x[1])
    return max_goals_player[0], max_goals_player[1]

def most_influent(statistics):
    most_influent_player = max(statistics, key=lambda x: x[1] * 1.5 + x[2] * 1.25 + x[3])
    most_influent_total = most_influent_player[1] * 1.5 + most_influent_player[2] * 1.25 + most_influent_player[3]
    return most_influent_player[0], most_influent_total

def calculate_scores_average(statistics, matches):
    total_goals=sum(match[1] for match in statistics)
    average=total_goals/matches
    return average