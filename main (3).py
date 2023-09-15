'''Implement a class called player that represents a cricket player.
method called play() which prints "The player is playing cricket , Derive two classes,
batsman and bowler, from the player class. override the play() method in each derived class to print
"The batsman is batting" and "The bowler is bowling ",respectively.
Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.'''


# Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket.")

#Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The bowleris bowling.")

# create objects of Batsman and classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()
