import csv

if __name__ == '__main__':
    
    """Make a list of team Dict's"""
    ##################################################################
    sharks = {}
    dragons = {}
    raptors = {}
    teams = [sharks, dragons, raptors]
    
    """Open the CSV file and "unpack" the data within a main_list"""
    ###################################################################
    
    with open("soccer_players.csv", newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter = ",")
        rows = list(player_reader)
    main_list = []
    for row in rows:
        for items in row:
            main_list.append(row[items])
            
    """Set up lists to separate the main list"""
    ############################################
    
    players_list = main_list[0::4]
    height_list = main_list[1::4]
    experience_list = main_list[2::4]
    parent_list = main_list[3::4]
    
    """Set up a Dict for the players """    
    ########################################
    
    player_dict = {}
    count = 0
    for player in players_list:
        player_dict[player] = [height_list[count], experience_list[count], parent_list[count]]
        count += 1
    
    """Make two lists YES and NO players"""
    #######################################
    
    previous_players = []
    no_experience = []
    
    for key,value in player_dict.items():
        if player_dict[key][1] == "YES":
            previous_players.append(key)
        else:
            no_experience.append(key)
            
            
    """Add players to team from the previous_players and no_experience lists"""
    ###############################################################################
    
    for player in previous_players:
        sharks["Sharks"] = previous_players[0::3]
        dragons["Dragons"] = previous_players[1::3]
        raptors["Raptors"] = previous_players[2::3]
    
    sharks["Sharks"] += no_experience[0::3]
    dragons["Dragons"] += no_experience[1::3]
    raptors["Raptors"] += no_experience[2::3]
    
    """Add the list to a file"""
    ##############################
    
    with open("teams.txt", "a") as f:
        for team in teams:
            for key, value in team.items():
                f.write("#" * 40 + '\n')
                f.write(key + ":" + "\n")
                f.write("#" * 40 + '\n')
                for players in value:         
                    f.write(players + ", " + player_dict[players][1].title() + ", " + player_dict[players][2] + "\n")
            f.write('\n')
                    
    
    #####################"""Testing"""#########################
    ###########################################################             
    