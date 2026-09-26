def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            return 0,[]

        total = float(lines[0].strip())

        history = []
        for line in lines[1:]:
            if line.strip() != "":
                history.append(float(line.strip()))
        return total, history
    except FileNotFoundError:
        return 0,[]

def main():
    total, transaction_history = load_inventory()

    print("Total:", total)
    print("Transaction History:", transaction_history)

if __name__ == "__main__":
    main()