import re

def tally(tournament_results):
    header = "Team                           | MP |  W |  D |  L |  P\n"

    teams = {}
    skel = {'MP':0, 'W':0, 'D':0, 'L':0, 'P':0}

    output = []

    lines = tournament_results.split("\n")

    for line in lines:
        if not line: break
        m = re.search('(.*);(.*);(.*)\n?',line)
        team1 = m.group(1); team2 = m.group(2); outcome = m.group(3)
        if not team1 in teams: teams[team1] = skel
        if not team2 in teams: teams[team2] = skel
        if outcome == "win":
            teams[team1]['MP'] += 1; teams[team1]['W'] += 1; teams[team1]['P'] += 3
            teams[team2]['MP'] += 1; teams[team2]['L'] += 1; 
        elif outcome == "loss":
            teams[team1]['MP'] += 1; teams[team1]['L'] += 1; 
            teams[team2]['MP'] += 1; teams[team2]['W'] += 1; teams[team2]['P'] += 3
        elif outcome == "draw":
            teams[team1]['MP'] += 1; teams[team1]['D'] += 1; teams[team1]['P'] += 1
            teams[team2]['MP'] += 1; teams[team2]['D'] += 1; teams[team2]['P'] += 1

    #print("teams: ",teams)
    
    #for name, data in sorted(teams.items(), key = lambda team: (team[-1], team[0:5])):
    for team in sorted(teams.keys(), key = lambda team: (_teamscore(**teams[team]), team)):
        output.append("{:<30s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s} | {!s:>2s}".format(team, 
            teams[team]['MP'], teams[team]['W'], teams[team]['D'], teams[team]['L'], teams[team]['P']))
        #print("name: {} data: {}".format(team, teams[team]))

            
    # return the list as a string with last newline omitted
    if output: return header+"\n".join(output).rstrip("\n")
    else: return header.rstrip("\n")


def _teamscore(MP, W, D, L, P):
    return P + D





if __name__ == "__main__":
    print(tally('Allegoric Alaskans;Blithering Badgers;win'))
