# Menu based program for Set Operations

# Take input sets from user
set1 = set(input("Enter elements of Set 1 (space separated): ").split())
set2 = set(input("Enter elements of Set 2 (space separated): ").split())

while True:
    print("\n--- Set Operations Menu ---")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (Set1 - Set2)")


    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("Union:", set1.union(set2))
    elif choice == '2':
        print("Intersection:", set1.intersection(set2))
    elif choice == '3':
        print("Difference (Set1 - Set2):", set1.difference(set2))
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")
