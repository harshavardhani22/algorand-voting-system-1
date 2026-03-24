# Simple Voting System (Simulation)

votes = {"A": 0, "B": 0}

def vote(candidate):
    if candidate in votes:
        votes[candidate] += 1
        print("Vote recorded!")
    else:
        print("Invalid candidate")

def results():
    print("Voting Results:")
    for candidate, count in votes.items():
        print(candidate, ":", count)

# Example usage
vote("A")
vote("B")
vote("A")
results()
