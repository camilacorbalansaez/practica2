def generate (names, goals, goals_avoided, assists):
    statistics = []
    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        statistics.append((name, goal, goal_avoided, assist))
    return statistics

def know_player_goals(statistics):
    for player in statistics:
        print(f'El jugador ' ,player[0], ' anotó ' ,player[1], ' goles en la última temporada.')