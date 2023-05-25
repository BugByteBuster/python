def tournamentWinner(competitions, results):
  teams_won = []
  teams_lost = []
  for i in range(len(results)):     #O(n)
    if results[i] == 0:
      winner = competitions[i][1]
      teams_won.append(winner)
    else: 
      winner = competitions[i][0]
      teams_won.append(winner)
  print(max(teams_won, key=teams_won.count))    #O(n), max function


tournamentWinner(
    competitions = [ ["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"] ], 
    results = [0, 0, 1]
)

#timecomplexity = O(n)