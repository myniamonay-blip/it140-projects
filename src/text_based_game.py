"""Project Two starter for the student's text-based adventure game."""

# Mynia Gloster
# IT-140 Project Two
# Zombie Unicorn Apocalypse


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to Zombie Unicorn Apocalypse!")
    print("Collect all 6 magical items before facing the Zombie Unicorn Queen!")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get 'item name'")
    print("----------------------------------------")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("----------------------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        if item not in inventory:
            Print(f"You see a {item}")

    print("----------------------------------------")


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

        rooms = {
        "Rainbow Cottage": {
            "north": "Enchanted Forest",
            "east": "Mushroom Meadow"
        },
        "Enchanted Forest": {
            "south": "Rainbow Cottage",
            "east": "Crystal Cave",
            "item": "Silver Horseshoe"
        },
        "Mushroom Meadow": {
            "west": "Rainbow Cottage",
            "north": "Crystal Cave",
            "item": "Healing Mushroom"
        },
        "Crystal Cave": {
            "west": "Enchanted Forest",
            "south": "Mushroom Meadow",
            "east": "Rainbow Falls",
            "item": "Magic Crystal"
        },
        "Rainbow Falls": {
            "west": "Crystal Cave",
            "north": "Fairy Garden",
            "item": "Rainbow Water"
        },
        "Fairy Garden": {
            "south": "Rainbow Falls",
            "east": "Abandoned Potion Lab",
            "item": "Moonflower"
        },
        "Abandoned Potion Lab": {
            "west": "Fairy Garden",
            "north": "Dark Unicorn Castle",
            "item": "Cure Potion"
        },
        "Dark Unicorn Castle": {
            "south": "Abandoned Potion Lab",
            "villain": "Zombie Unicorn Queen"
        }
    }
    current_room = "Rainbow Cottage"
    inventory = []
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
        show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()
        if command.startswith("go "):
            direction = command[3:]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way! Try another direction.")       
            elif command.startswith("get "):
            item_name = command[4:]

            if ("item" in rooms[current_room]
                    and item_name == rooms[current_room]["item"].lower()
                    and rooms[current_room]["item"] not in inventory):
                inventory.append(rooms[current_room]["item"])
                print("You collected the item!")
            else:
                print("That item is not available in this room.")
        else:
            print("Invalid command! Use 'go' to move or 'get' to collect an item.")  
        if current_room == "Dark Unicorn Castle":
            if len(inventory) == 6:
                print("Congratulations! You collected all 6 magical items!")
                print("You defeated the Zombie Unicorn Queen and saved Rainbow Valley!")
            else:
                print("Oh no! The Zombie Unicorn Queen has defeated you!")
                print("GAME OVER! You did not collect all 6 magical items.")

            print("Thanks for playing Zombie Unicorn Apocalypse!")
            break            

if __name__ == "__main__":
    main()
