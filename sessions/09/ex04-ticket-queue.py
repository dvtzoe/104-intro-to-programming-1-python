from collections import deque

queue = deque()

while (command := input("join/serve/show/quit")) != "quit":
    if command == "join":
        name = input("Name: ")

        queue.append(name)

        print(f"{name} joined, position {len(queue)}")
    elif command == "serve":
        serving = queue.popleft()
        if serving:
            print(f"Serving {serving}")
        else:
            print("Nobody waiting")
    elif command == "show":
        raise NotImplementedError
