"""
Make a two-player Rock-Paper-Scissors game.

Hint:
Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game


"""

class Player():

    def __init__(self, name):
        self.name = name
        self.matches = 0
        self.hits = 0

    def newHit(self):
        self.hits += 1

    def newMatch(self):
        self.matches += 1
'''
class Match():
    def __init__(self, Player1, Player2:
        self.Player1 = Player1()
        self.Player2 = Player2()

    def startMatch(self):
        print(Player1.name)
'''
def newMatch(player1, player2):
    print("Lets begin the game:")
    print("Player1: %s  Player2: %s" % (player1.name,player2.name))
    print("·················································")
    print("The rules:")
    print("In each turn you can choose a move:")
    print(" Rock >>> 1")
    print(" Scissors >>> 2")
    print(" Paper >>> 3")
    print("The first one who reaches 3 hits wins the match")
    print("·················································")

    while player1.hits < 3 and player2.hits < 3:
        player1Move = int(input("Whats your move %s?" % player1.name))
        player2Move = int(input("Whats your move %s?" % player2.name))
        if player1Move == 1:
            if player2Move == 1:
                print("No hit for anyone")
            if player2Move == 2:
                player1.newHit()
                print("%s hits" % player1.name)
            if player2Move == 3:
                player2.newHit()
                print("%s hits" % player2.name)
        elif player1Move == 2:
            if player2Move == 2:
                print("No hit for anyone")
            if player2Move == 3:
                player1.newHit()
                print("%s hits" % player1.name)
            if player2Move == 1:
                player2.newHit()
                print("%s hits" % player2.name)
        elif player1Move == 3:
            if player2Move == 3:
                print("No hit for anyone")
            if player2Move == 1:
                player1.newHit()
                print("%s hits" % player1.name)
            if player2Move == 2:
                player2.newHit()
                print("%s hits" % player2.name)

    if player1.hits > player2.hits:
        player1.newMatch()
        print("The winner for this match is %s" % player1.name)
    else:
        player2.newMatch()
        print("The winner for this match is %s" % player2.name)

def revenge(player1, player2):
    print("·················································")
    print("The score until now is:")
    print("%s has: %s match(es)" % (player1.name,player1.matches))
    print("%s has: %s match(es)" % (player2.name,player2.matches))
    print("·················································")
    playAgain = input("Do you want to play another match?")
    if playAgain == "yes":
        player1.hits = 0
        player2.hits = 0
        newMatch(player1,player2)
    else:
        print("Ok, it may be the next time. See ya!")

if __name__ == '__main__':
    bob = Player("Bob")
    tom = Player("Tom")

    newMatch(bob,tom)
    revenge(bob,tom)
