def generate(names, goals, goals_avoided, assists):
    statistics = []
    for i in range(len(names)):
        statistics.append((names[i], goals[i], goals_avoided[i], assists[i]))
    return statistics