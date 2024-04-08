def generate (names, goals, goals_avoided, assists):
    statistics = []
    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        statistics.append((name, goal, goal_avoided, assist))
    return statistics