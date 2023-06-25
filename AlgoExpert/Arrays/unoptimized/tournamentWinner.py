def tournamentWinner(competitions, results):
    max_score = 0
    winner = ""
    team_scores = {}

    for i in range(len(results)):
        if results[i] == 0:
            winner = competitions[i][1]
        else:
            winner = competitions[i][0]
        if winner not in team_scores:
            team_scores[winner] = 0
        team_scores[winner] += 1

        if team_scores[winner] > max_score:
            max_score = team_scores[winner]
            winning_team = winner

    return winning_team


tournamentWinner(
    competitions=[
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"],
    ],
    results=[0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
)
