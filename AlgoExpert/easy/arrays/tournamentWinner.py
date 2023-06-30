# O(n) time complex
def tournamentWinner(competitions, results):
    i = 0
    team_score = {}
    max_score = 0
    winner = ""

    while i < len(results):
        if results[i] == 0:
            winner = competitions[i][1]
        else:
            winner = competitions[i][0]
        if winner not in team_score:
            team_score[winner] = 1
        else:
            team_score[winner] = team_score[winner] + 1

        if team_score[winner] > max_score:
            max_score = team_score[winner]
            winning_team = winner
        i = i + 1

    return winning_team


tournamentWinner(
    competitions=[["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
    results=[0, 0, 1],
)
