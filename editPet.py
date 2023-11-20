# This file is designed for edit pet.
# This defines a function named editPet that takes a list of pets as a parameter.
def editPet(pets):
    # The try block will catch the potential error and handles that.
    try:
        # A message to prompt the user to choose a pet for editing.
        print("Which pet would you like to edit?")

        # Enumerate is a built-in function that allows to iterate over a sequence (such as a list, tuple, or string).
        # Also keeps track of the position of current element and returns the pair.
        for i, pet in enumerate(pets, 1):
            # It prints the index and name of each pet in the list.
            print(f"[{i}] {pet.name}")

        # To add the quit to the list
        print("[Q] Quit")
        # This let the user input his/her choice.
        choice = input("Input your choice: ")

        # This will quit the edit process if choice is q.
        if choice.lower() == 'q':
            print("Quitting the edit process.")
            print()
            # This will break the editPet, and return to calling code.
            return

        # If user input valid input it will check and proceed to edit process.
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(pets):
                pet = pets[choice - 1]
                # Informing user which pet is selected.
                print(f"You are going to edit {pet.name}")
                # Let the user know about pressing enter will not change anything.
                print(f"If you press Enter, it will not change the name and age")

                # This will allow user to input a new name.
                newName = input(f"New name: ")
                if newName:
                    pet.name = newName
                    # When user input the name this will print the name.
                    print(f"The pet's name has been updated to {pet.name}.")

                # This will prompt user to input new age.
                newAge = input(f"New age: ")

                # This while true loop will continue the program till explicitly broken
                while True:
                    # This condition checks if the user has entered something for the new age
                    if newAge:
                        # This will catch the error and handle under newAge function.
                        try:
                            pet.age = int(newAge)
                            # Will print the updated pet age.
                            print(f"The pet's age has been updated to {pet.age}.")
                            # Break out of the loop if the age input is valid
                            break
                        # If user input something invalid, it will catch that and print error massage.
                        except ValueError:
                            print("Invalid input. Age must be a valid integer.")

                    # If the user press enter, without providing a new age this line will printed.
                    else:
                        print("No new age provided. The pet's age will remain unchanged.")
                        # exit the loop
                        break  # Break out of the loop if the user presses Enter without providing a new age

                    # Ask the user for another input or provide an option to proceed with the rest of the information
                    choice = input("Would you like to edit age? (Y/N): ").strip().lower()
                    if choice != 'y':
                        # Break out of the loop if the user chooses not to try again
                        break
                    # If the user enters 'Y', it allows for a new age input
                    newAge = input(f"New age: [{pet.age}] ")

                print()
                # For the pet just edited.
                print(f"Updated Pet:")
                # Will print the updated pet information.
                print(f"{pet.name} is a {pet.animal_type} owned by {pet.owner}. {pet.name} is {pet.age} years old.")
                # I like some space.
                print()
                # Will print the pet list with new update.
                print(f"Updated Pet List:")
                # This will iterate the pet and track the position.(same stated before).
                for i, pet in enumerate(pets, 1):
                    print(f"[{i}] {pet.name}")
                # Add the quit to the list.
                print(f"[Q] Quit")

            # When user input something other than the list, will get the massage.
            else:
                print(f"Invalid number. Please choose a valid one.")
    # If unexpected input is encountered during the execution of the input
    except EOFError:
        print(f"Unexpected input. Quitting the edit process.")

