class TorunamentTree:

    class TorunamentTreeNode:

        def __init__(self, key, team):
            self.key = key
            self.team = team
            self.left = None
            self.right = None

        def add(self, key, team):
            if key < self.key:
                if self.left is None:
                    self.left = TorunamentTree.TorunamentTreeNode(key, team)
                else:
                    self.left.add(key, team)#this is recursive of the left until you reach the end of the 'node'

            elif key > self.key:
                if self.right is None:
                    self.right = TorunamentTree.TorunamentTreeNode(key, team)
                else:
                    self.right.add(key, team)#this is recursive of the right until you reach the end of the 'node'

            else:
                raise Exception("Duplicate Key")

        def teams_left(self, teams):
            if self.team == "":
                self.left.teams_left(teams)
                self.right.teams_left(teams)
            else:
                teams.add(self.team)

    #TrounamentTree
    def __init__(self, name):
        self.name = name
        self.root = None

    def add(self, key, team):
        if self.root is None:
            self.root = TorunamentTree.TorunamentTreeNode(key, team)
        else:
            self.root.add(key, team)

    def __str__(self):
        return self.name

    def teams_left(self):
        teams = set()
        if self.root == None:
            return teams
        else:
           self.root.teams_left(teams)

        return teams

    def points_1(self, key_bracket):
        if self.root ==  None:
            return (0, 0)
        else:
            return self.root.points(key_bracket.root, 32)

    def points(key_bracket, round_number, tournament_key, points_from_round, possible_points):
        level_pts = 32
        while tournament_key <= 32:
            level_pts = level_pts/2
            teams_alive = 0
            teams_alive = key_bracket(brackets.root, teams_alive)
            points_from_round = (2 ^ round_number * teams_alive)
            possible_points = teams_alive * (63-(2^round_number * 2 -1))
        return (points_from_round, possible_points)

    #function that reads down each of the nodes to figure out what teams are still alive
    def compare_key_to_bracket(bracket, teams_alive, left, right):
        if TorunamentTree.left != None:
            teams_alive = key_bracket(TorunamentTree.left, teams_alive)

        elif TorunamentTree.right != None:
            teams_alive = key_bracket(TorunamentTree.right, teams_alive)

        else:
            teams_alive += 1

        return teams_alive

def ReadBracket(name):
    file_name = ("Brackets\\" + name + ".txt")
    with open(file_name, mode='r')as in_file:
        n = 0
        for line in in_file:
            line = line.strip('\n\r')
            n += 1
            if n == 1:
                print("Name:", line)
                bracket =  TorunamentTree(line)
            else:
                (team_no, team) = line.split('\t')
                team_no = int(team_no)
                #print("Team: [{}] {}".format(team_no, team) )
                bracket.add(team_no, team)

    return bracket

players = [ "Bashardoust", "Graves", "Haab", "Horton", "Shelly.Art", "Shelly.Lisa", "Short", "Wilson", "Siekman", "Staton", "Lawniczak" ]#To read in all the brackets use all the names in the class
# brackets = []#array that holds all the brackets
# for player in players:
#     brackets.append(ReadBracket(player))
#key_bracket = ReadBracket("First_Round")
key_bracket = ReadBracket("Second_Round")

brackets = [ReadBracket(name) for name in players]

#bracket = ReadBracket("Short")
# #print( brackets)
# for bracket in brackets:
#     (actual, possible) = bracket.points(key_bracket)
#print("{:<15} : {:^15} : {:^15} vs {:^15}".format(bracket.name, bracket.root.team, bracket.root.left.team, bracket.root.right.team))
#print("{:<15} : {:^15} : {}".format(bracket.name, bracket.root.team, (bracket.root.team in teams_left)))


#print out of points, possible points, and overall score
for players in brackets: #Prints out each players bracket with their standings.
    print("{:   },:  {: },: {:  },: {:  }".format(brackets), TorunamentTree.points())

teams_left = key_bracket.teams_left()
print ( teams_left)
