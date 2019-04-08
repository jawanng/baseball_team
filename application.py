import constants
import random

def dedup_player(orig, removal):
  hold = []
  # print("Orig count: {}. Removal count: {}".format(len(orig), len(removal)))
  for itr in orig:
    match = False
    for itr_other in removal:
      if (itr['name'] == itr_other['name']):
        match = True
    if match:
      pass
    else:
      hold.append(itr)
  # print("Hold count: {}".format(len(hold)))
  return hold

def place_players():
  # sample_number = len(constants.PLAYERS) // len(constants.TEAMS)
  teams = {}
  players = constants.PLAYERS[:]
  exp = []
  inexp = []
  for itr in players:
    if itr['experience'].upper() == 'YES':
      exp.append(itr)
    else:
      inexp.append(itr)
  sample_exp = len(exp) // len(constants.TEAMS)
  sample_inexp = len(inexp) // len(constants.TEAMS)
  for team in constants.TEAMS:
    teams[team] = random.sample(exp, sample_exp)
    teams[team] += random.sample(inexp, sample_inexp)
    exp = dedup_player(exp, teams[team])
    inexp = dedup_player(inexp, teams[team])
  players = exp + inexp
  while players:
    for team in constants.TEAMS:
      if players:
        teams[team] += players.pop()
  return teams

def print_team(team, team_name):
  exp = 0
  inexp = 0
  height = 0
  holder = "Team: " + team_name + " Stats"
  members = []
  guardians = []
  for itr in team:
    members.append(itr['name'])
    if itr['experience'].upper() == 'YES':
      exp += 1
    else:
      inexp += 1
    height += int(itr['height'].split()[0])
    guardians += itr['guardians'].split(' and ')
  print("\n{}".format(holder))
  print("-" * len(holder))
  print("Total players: {}".format(len(team)))
  print("  expierenced: {}".format(exp))
  print("inexpierenced: {}".format(inexp))
  print("\nThe Average Height of the players: {}".format(height / len(team)))
  print("\nPlayers on Team:")
  print("  {}\n".format(", ".join(members)))
  print("Guardians on Team:")
  print("  {}\n".format(", ".join(guardians)))
  
def main_menu():
  while 1:
    print("  Here are your choices:")
    print("   1) Display Team Stats")
    print("   2) Quit\n")
    opt = input("Enter an option > ")
    if opt == '2':
      print("\nHave a great day!\n")
      exit(0)
    elif opt == '1':
      return 1
    
def team_select():
  while 1:
    opt = input("\n1) Panthers\n2) Bandits\n3) Warriors\n\nEnter an option > ")
    if opt == '1':
      return 'Panthers'
    elif opt == '2':
      return 'Bandits'
    elif opt == '3':
      return 'Warriors'

if __name__ == '__main__':
  print("BASKETBALL TEAM STATS TOOL\n\n---- MENU----\n")
  teams = place_players()
  # print_team(teams['Panthers'], 'Panthers')
  while 1:
    main_menu()
    team = team_select()
    print_team(teams[team], team)
    input("Press ENTER to continue...")
