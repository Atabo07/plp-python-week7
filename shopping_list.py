# Part B - Shopping List Manager
# A menu-driven program that adds, removes and shows items.

shopping = []  # start with an empty list

while True:
    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("What item would you like to add? ").strip()
        if item == "":
            print("Please type an item name.")
        else:
            shopping.append(item)
            print(item, "added.")

    elif choice == "remove":
        item = input("What item would you like to remove? ").strip()
        # Check the item is in the list BEFORE removing it
        if item in shopping:
            shopping.remove(item)
            print(item, "removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping) == 0:
            print("Your list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping:
                print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Please choose add, remove, show or done.")
