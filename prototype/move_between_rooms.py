"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

current_room = "Great Hall"
print("Dragon Text Game Prototype")
print(" \n------------------------------\n ")
print("""Move betweens rooms using the following:
Move commands: north, south, east, west.
To quit game, type 'exit'.""")
print(" \n------------------------------\n ")
print(f"You are in the {current_room}.")

while current_room != "exit":  # When current room is not equal to "exit",
    # game is in progress.
    print("Enter a move command: ")
    move = (
        input().lower()
    )  # Assign user input to "move" and covert to lowercase
    if move in rooms[current_room]:  # When move in the "rooms" dictionary
        # Assign to current_room the value of the key in rooms
        current_room = rooms[current_room][move]
        print(f"You are in the {current_room}.")  # Output the current room
        print(" \n------------------------------\n ")
    elif move not in rooms[current_room] and move != "exit":
        # When move is not in the "rooms" dictionary and is not "exit"
        if (
            move != "north"
            and move != "south"
            and move != "east"
            and move != "west"
        ):  # When move is not a direction, output invalid input message
            print("Invalid input. Please enter a valid move command.")
            print(" \n------------------------------\n ")
        else:  # When move is a direction but not a valid move from current room
            # Output invalid move message
            print("You can't go that way. Please enter a valid move command.")
            print(" \n------------------------------\n ")
    elif move == "exit":  # Ends the game when player inputs "exit"
        print("You typed 'exit'. GAME OVER.!")
        break
