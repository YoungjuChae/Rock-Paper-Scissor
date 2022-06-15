# Author: Youngju Chae
# Text Based Rock Paper Scissors Game

# Importing necessary module
import random
from art import logo
import os

# Creating necessary variables
wins = 0
losses = 0
ties = 0

rock = 0
paper = 0
scissor = 0

playing = True

clear = lambda: os.system('cls')

# Run the game
print(logo)
while playing:
  # Create score tracker
  print('{} Wins, {} Losses, {} Ties'.format(wins,losses,ties))
  while True:
      # Determine player's move
      print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
      playerMove = input()
      if playerMove == 'q':
          print('{} Wins, {} Losses, {} Ties'.format(wins,losses,ties))
          # Determine the total number of each hand played
          print('{} Rocks, {} Papers, {} Scissors'.format(rock,paper,scissor))
          # Determine the most played hand
          mostPlayed = max(rock, paper, scissor)
          if (rock > paper and rock > scissor):
              print('Your most played hand is rock, which you played {} times'.format(mostPlayed))
          elif (paper > scissor and paper > rock):
              print('Your most played hand is paper, which you played {} times'.format(mostPlayed))
          elif (scissor > rock and scissor > paper):
              print('Your most played hand is scissor, which you played {} times'.format(mostPlayed))
          else:
              print('You do not have a single most played hand')
          playing = False
          break
        
      if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
          break
      print('Type one of r, p, s, or q')
    
  # End the game
  if playing == False:
    break
    
  # Determine player's move
  if playerMove == 'r':
      print('ROCK versus...')
      rock += 1
  elif playerMove == 'p':
      print('PAPER versus...')
      paper += 1
  elif playerMove == 's':
      scissor += 1
      print('SCISSORS versus...')

  # Randomly decide computer's move
  randomNumber = random.randint(1, 3)
  if randomNumber == 1:
      computerMove = 'r'
      print('ROCK')
  elif randomNumber == 2:
      computerMove = 'p'
      print('PAPER')
  elif randomNumber == 3:
      computerMove = 's'
      print('SCISSORS')

  # Determine all possible outcomes
  if playerMove == computerMove:
      print('It is a tie!')
      ties = ties + 1
  elif playerMove == 'r' and computerMove == 's':
      print('You win!')
      wins = wins + 1
  elif playerMove == 'p' and computerMove == 'r':
      print('You win!')
      wins = wins + 1
  elif playerMove == 's' and computerMove == 'p':
      print('You win!')
      wins = wins + 1
  elif playerMove == 'r' and computerMove == 'p':
      print('You lose!')
      losses = losses + 1
  elif playerMove == 'p' and computerMove == 's':
      print('You lose!')
      losses = losses + 1
  elif playerMove == 's' and computerMove == 'r':
      print('You lose!')
      losses = losses + 1