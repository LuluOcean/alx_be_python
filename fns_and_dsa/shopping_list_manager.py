def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            items_input = input("Enter item(s) to add (separate multiple with commas): ")
            items = [item.strip() for item in items_input.split(',') if item.strip()]
            shopping_list.extend(items)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item_remove = int(input("Enter item number to remove from list: "))
            shopping_list.remove(shopping_list[item_remove-1])
            pass
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(f"{shopping_list.index(item)+1}. {item}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()