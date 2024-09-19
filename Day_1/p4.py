import sys

# Capture command-line arguments
statecaps = sys.argv
states = []
capitals = []

# Loop through the arguments, starting from index 1 to skip the script name
for i in range(1, len(statecaps)):
    # Split each argument into state and capital
    arr = statecaps[i].split()
    # Append the state and capital to their respective lists
    states.append(arr[0])
    capitals.append(arr[1])

# Print the lists of states and capitals
print(states)
print(capitals)