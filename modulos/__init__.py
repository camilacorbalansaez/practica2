def generate (names, goals, goals_avoided, assists):
    """
    Genera una lista de tuplas con los datos que se pasan como argumentos.

    names= Corresponde a una lista de los nombres de los jugadores.
    goals= Corresponde a una lista con la cantidad de goles realizados por los jugadores.
    goals_avoided= Corresponde a una lista con la cantidad de goles evitados por los jugadores.
    assists= Corresponde a una lista con la cantidad de asistencias realizadas por los jugadores. 

    Retorna la lista generada.
    
    """
    statistics = []
    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        statistics.append((name, goal, goal_avoided, assist))
    return statistics

def max_scorer(statistics):
    """
    Busca al máximo goleador, el jugador con mayor cantidad de goles realizados.

    statistics= Corresponde a la lista de tuplas con las estadísticas de los jugadores realizada previamente.

    Retorna el nombre del goleador y la cantidad de goles realizados.  
    """
    max_goals_player = max(statistics, key=lambda x: x[1])
    return max_goals_player[0], max_goals_player[1]

def most_influent(statistics):
    """
    Busca al jugador más influyente calculando los goles realizados, goles evitados y asistencias según su valor.
    Los goles realizados valen 1.5 puntos, los goles evitados valen 1.25 puntos y las asistencias valen 1 punto. 

    statistics= Corresponde a la lista de tuplas con las estadísticas de los jugadores realizada previamente. 

    Retorna el nombre del jugador más influyente y la cantidad total de puntos.
    """
    most_influent_player = max(statistics, key=lambda x: x[1] * 1.5 + x[2] * 1.25 + x[3])
    most_influent_total = most_influent_player[1] * 1.5 + most_influent_player[2] * 1.25 + most_influent_player[3]
    return most_influent_player[0], most_influent_total

def calculate_average_scores(statistics, matches):
    """
    Calcula el promedio de goles realizados por partido.

    statistics= Corresponde a la lista de tuplas, tendrá en cuenta el valor [1] que es donde se almacenan los goles realizados. 
    matches= Corresponde a la cantidad de partidos jugados en la temporada. 

    Retorna el promedio de goles por partido.  
    """
    total_goals=sum(match[1] for match in statistics)
    average=total_goals/matches
    return average

def calculate_average_scorer(goals, matches):
    """
    Calcula el promedio de goles del máximo goleador.

    goals= Corresponde a la cantidad de goles realizados por el goleador. 
    matches= Corresponde a la cantidad de partidos jugados en la temporada. 

    Retorna el promedio de goles por partido del goleador.   
    """
    average_scorer=goals/matches
    return average_scorer