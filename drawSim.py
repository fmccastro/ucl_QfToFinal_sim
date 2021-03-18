import math, os, random
os.chdir("/media/fmccastro/My_Passport/Part Time Projects/uclDrawSimulator")

class Club:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Match:
    def __init__( self, club1, club2 ):
        self.homeTeam = club1
        self.awayTeam = club2

nbClubs = 8
info = []
matches = []

if __name__ == '__main__':

    index = 0

    f = open("listClubs.txt", "r") 

    while( index < nbClubs ):

        line = f.readline()
        line = line.split()

        club = " ".join( line[:-1] )
        country = line[-1]

        info += [ Club( club, country ) ]

        index += 1
    
    f.close()

    index = 0

    while( index < nbClubs/2.0 ):

        club1 = random.choice( info )
        info.remove( club1 )

        club2 = random.choice( info )
        info.remove( club2 )

        matches += [ Match( club1.name, club2.name ) ]

        index += 1

    print("|--------- UCL Quarter-Final Matches ---------|" )

    index = 0

    while( index < nbClubs/2.0 ):

        match = matches[index]

        print( "| " + match.homeTeam + " vs " + match.awayTeam, "     |" )

        index += 1
    
    print("|---------------------------------------------|")