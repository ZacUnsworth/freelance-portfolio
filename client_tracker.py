import json

clients = []

def add_client(name, email):
    clients.append({"name": name, "email": email})
    with open("clients.json", "w") as file:
        json.dump(clients, file, indent=4)
    print(f"Client {name} added.")

def load_clients():
    global clients
    try:
        with open("clients.json", "r") as file:
            clients = json.load(file)
    except FileNotFoundError:
        clients = []

if __name__ == "__main__":
    load_clients()
    while True:
        print("\n1. Add Client\n2. View Clients\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Client Name: ")
            email = input("Client Email: ")
            add_client(name, email)
        elif choice == "2":
            for c in clients:
                print(f"{c['name']} - {c['email']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")