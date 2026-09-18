total_inventory = 0
failed_entries = 0

print("--- Inventory Auditor System ---")
print("Enter stock quantities to add. Type 'quit' to exit.\n")

while True:
    user_input = input("Enter stock quantity: ").strip()
    if user_input.lower() == 'quit':
        print("Exiting auditor program.")
        break

    if not user_input.isdigit():
        if user_input.startswith('-') and user_input[1:].isdigit():
            print("Error: Negative numbers are not allowed. Please enter a positive integer.")
        else:
            print("Error: Invaild input. Please enter a vaild whole number (integer).") 
        failed_entries += 1
        continue

    stock_value = int(user_input)

    total_inventory += stock_value
    print(f"added {stock_value} units. Current total inventory: {total_inventory}")

    if total_inventory > 500:
        print(f"\n OVERSTOCK ALERT: Total inventory ({total_inventory}) exceeds the maximum limit!")
        break

print("\n--- Audit Summary Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")

