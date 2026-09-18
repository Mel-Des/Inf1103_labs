def get_vaild_input():
    user_input = input("Enter stock quantity: ").strip()

    if user_input.lower() == 'quit':
        return "quit"

    if not user_input.isdigit():
        if user_input.startswith('-') and user_input[1:].isdigit():
            print("Error: Negative numbers are not allowed. Please enter a positive integer.")
        else:
            print("Error: Invaild input. Please enter a vaild whole number (integer).") 
        return None

    return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_inventory, failed_entries):
    print("\n--- Audit Summary Report ---")
    print(f"Total Units Processed: {total_inventory}")
    print(f"Number of Failed/Rejected Entries: {failed_entries}")

if __name__ == "__main__":
    total_inventory = 0
    failed_entries = 0

    print("--- Modular Inventory Auditor System ---")
    print("Enter stock quantities to add. Type 'quit' to exit.\n")

    while True:
        result = get_vaild_input()

        if result == "quit":
            print("Exiting auditor program.")
            break

        if result is None:
            failed_entries += 1
            print()
            continue

        delivery_amount = result

        total_inventory = process_delivery(total_inventory, delivery_amount)

        tax_amount = calculate_tax(delivery_amount)

        print(f"Added {delivery_amount} units (Tax for this delivery: {tax_amount:.2f}).")
        print(f"Current total inventory: {total_inventory}\n")

        if total_inventory > 500:
            print("Total inventory exceeds 500 units!")
            print("Shutting down system.")

    generate_report(total_inventory, failed_entries)