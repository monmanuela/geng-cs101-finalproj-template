# FINAL PROJECT Q2 - HACKATHON MATCHING
# Generation Girl Winter Club 2020 - CS101 English Class
# Mentors: Johanna Gunawan, Monika Manuela Hengki
# TAs: Saskia Latievarya, Shafira Naya Aprisadianti

# Developer: <PUT YOUR NAME HERE>

# ---------------------------------------------------------------
# Part 1 - Sign Up
# ---------------------------------------------------------------

# Ask for the person's name
name = input('Please enter your name: ')

# Helper function - rate_skill
# Input: the name of the skill (e.g. 'leadership')
# Output: a number between 1 to 10 corresponding to the skill level
def rate_skill(skill_type):
  while True:
    # Ask for user input to rate the skill_type from 1 to 10
    skill = ...
    
    # Input validation - skill must be a number, and it must be between 1 to 10
    if ...:
      # Invalid input - ask the user again
      print('Please enter a valid number between 1-10')
      continue
    
    # Valid input - return the skill as a number
    return ...

# Ask for the leadership, coding, and design skill
# Hint: use rate_skill helper function
leadership_skill = ...
coding_skill = ...
design_skill = ...

# Get the highest skill level among the 3 skills
max_skill = ...
position = ''

# Assign position based on which skill ranks the highest
# leadership skill: CEO; coding skill: CTO; design skill: Designer
# If there is a tie, prioritise becoming a CEO, CTO, then Designer
if ...:
  position = ...
elif ...:
  position = ...
else:
  position = ...

# List of 10 fields to choose from for the person's interest
fields = ...

print('Please enter 3 numbers of the fields you are interested in from this list')

# Print the 10 options, numbered from 1 to 10
for ...:
  ...

# Ask the user for their 3 fields of interest
count = 1
interests = []
while count <= 3:
  # Ask for user input of a number that correspond to their interest
  interest = ...

  # Input validation - interest must be a number, and it must be between 1 to 10
  if not interest.isnumeric() or int(interest) < 1 or int(interest) > 10:
    # Invalid input - ask the user again
    print('Please enter a valid number between 1-10')
    continue
  
  # Valid input, add it to the list of interests
  ...
  count += 1

print('=====PROFILE=====')
# Print the name, position, and list of interests
...
...
...
print('=====END PROFILE=====')

# ---------------------------------------------------------------
# Part 2 - Suggestion
# ---------------------------------------------------------------

# List of other participants data
# Each participant data is a list of the name, position, and a list of numbers that correspond to an index of the fields list
participants = [
  ['Seo Dalmi', 'CEO', [1,3,5]],
  ['Han Jipyeong', 'CEO', [2,4,8]],
  ['Kim Soo Hyun', 'CEO', [6,7,9]],
  ['Son Yejin', 'CEO', [6,7,10]],
  ['Jennie', 'CTO', [1,4,9]],
  ['Hyun Bin', 'CTO', [2,3,7]],
  ['Nam Dosan', 'CTO', [5,6,10]],
  ['Bae Suzy', 'CTO', [1,4,8]],
  ['Park Seo Joon', 'Designer', [1,3,5]],
  ['Gong Yoo', 'Designer', [2,4,8]],
  ['Jungkook', 'Designer', [7,9,10]],
  ['IU', 'Designer', [3,6,7]],
]

# Helper function - get_common_interests
# Input: 2 lists of interests
# Output: a list of interests that exist in both lists (if no common interests, return empty list)
def get_common_interests(interests1, interests2):
  # Initialize the variable common that will keep track of the list of common interests
  common = ...
  
  # Iterate through every element in the first list
  for ...:
    # Check if the element exists in the second list
    if ...:
      # Found a common interest - add it to the common list
      ...
  
  # Return the list of common interests
  return ...

print('=====SUGGESTED PEOPLE=====')
print('Here are some people you should talk to!')

# Iterate through the list of other participants
for ...:
  # Obtain the other participant's name, position and interests and save in variables
  other_name = ...
  other_position = ...
  other_interests = ...
  
  # Get common interests between my interests and the other participant's interests
  common_interests = ...

  # Don't suggest this participant if we have the same position (e.g. both are CEOs)
  if ...:
    continue
  # Don't suggest this participant if we don't have any common interest
  elif ...:
    continue
  
  # This other participant fulfilled all the criteria - print their data (name, position, common interests)
  ...
  ...
  ...
  print('\n')
print('=====END SUGGESTED PEOPLE=====')
