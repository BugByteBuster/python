def tournamentWinner(competitions, results):
    i = 0 
    winning_teams = []
    loosing_teams = []
    for result in results:
        if result == 0:
            winning_teams.append(competitions[i][1])
            loosing_teams.append(competitions[i][0])
        else: 
            winning_teams.append(competitions[i][0])
            loosing_teams.append(competitions[i][1])
        i = i+1
    print(winning_teams)
    print(loosing_teams)


tournamentWinner(  
        competitions = [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ],
        
        results = [0, 0, 1]
  )


"""
{
  "competitions": [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ],
  "results": [0, 0, 1]
}
output: Python
"""