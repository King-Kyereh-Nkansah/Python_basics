command=""
started= False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car has already started")
        else:
            started=True
            print("car started...")
    elif command=="stop":
        if not started:
            print("Car has already stopped")
        else:
            started=False
            print("Car stopped...")
    elif command=="help":
        print('''
start- To start
stop-  To stop
quit-  To exit''')
    elif command=="quit":
        break
    else:
        print("Invalid command")