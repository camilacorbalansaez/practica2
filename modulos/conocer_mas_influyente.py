def most_influent(statistics):
    most_influent_player = max(statistics, key=lambda x: x[1] * 1.5 + x[2] * 1.25 + x[3])
    most_influent_total = most_influent_player[1] * 1.5 + most_influent_player[2] * 1.25 + most_influent_player[3]
    print(f'El jugador más influyente fue  {most_influent_player[0]} con una puntuación total de : {most_influent_total}.')
