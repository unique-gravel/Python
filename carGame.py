command = input('> ')
started = False
while command.lower() != "quit":
    if command.lower() == "help":
        print("""
        start: to start the car
        stop: to stop the car
        quit: to quit the game
        """)
    elif command.lower() == "start":
        if started:
            print("The car is already moving!")
        else:
            started = True
            print("The car has started moving.")
    elif command.lower() == "stop":
        if not started:
            print("The car is already not moving!")
        else:
            started = False
            print("The car has stopped moving.")
    else:
        print(("I don't understand that."))
    command = input("> ")

print("The game has ended.")