# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [
    {
        "Item name": "",
        "Price": 0,
        "Quantity": 0
    }
]

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_item_names_by_number = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    
    # STEP 1: Print Categories:
    #_________________________
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category name as the value of the menu item number key
        menu_item_names_by_number[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input as a menu_item_num number, 
    # to be used to reference a menu category number
    # inside menu_item_names_by_number
    menu_item_num = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_item_num.isdigit():
        # Check if customer's input is in menu_item_names_by_number
        if int(menu_item_num) in menu_item_names_by_number.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_item_names_by_number[int(menu_item_num)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_item_names_by_number = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            # For the menu_category_name the user selected (Snacks, Meals, etc.)
            # loop through each item, key for the specific item and display 
            # the item number, item name, and price
            
            for menu_subitem_name, menu_subitem_price in menu[menu_category_name].items():
                # print(f"menu_subitem_name: {menu_subitem_name}")
                # Check if the submenu item is also a dictionary, which would be handled differently
                # Step 2a: Check if sub-items is also a dictionary: NOT GOING HERE
                #_____________________________
                
                if type(menu_subitem_price) is dict:
                    for sub_item_key, sub_item_value in menu_subitem_price.items():
                        combined_length = menu_subitem_name + sub_item_key;
                        seperator_space = 3 #  space-dash-space " - " between the main item and sub-item names.
                        num_item_spaces = 24 - len(combined_length) - seperator_space
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {menu_subitem_name} - {sub_item_key}{item_spaces} | ${sub_item_value}")
                        # Store the item in a dictionary (object) to be printed
                        menu_item_names_by_number[i] = {
                            "Item name": key + " - " + sub_item_key,
                            "Price": sub_item_value
                        }
                        i += 1
                # Step 2b: Print the Sub items:
                #_____________________________
                 
                else:
                    num_item_spaces = 24 - len(menu_subitem_name)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {menu_subitem_name}{item_spaces} | ${menu_subitem_price}")
                    menu_item_names_by_number[i] = {
                        "Item name": menu_subitem_name,
                        "Price": menu_subitem_price
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            # menu_selection => sub_menu_selection
            sub_menu_selection = input("Please enter a selection from the submenu: ")

            # 3. Check if the customer typed a number
            if sub_menu_selection.isdigit():
                # Convert the menu selection to an integer
                sub_menu_selection = int(sub_menu_selection)

                # 4. Check if the menu selection is in the menu items
                subcategory = menu[menu_category_name]
                print(f"Submenu item object: {subcategory}")
                print(f"Submenu selection:", sub_menu_selection)
                print(f"Length of subItems: {range(len(subcategory))}")
                print(f"Submenu keys List: {list(subcategory.keys())}")
                print(f"Submenu values List: {list(subcategory.values())}")
                print(f"Submenu items Tuples List: {list(subcategory.items())}")
                list_of_dicts = [{key: value} for key, value in subcategory.items()]
                print(f"First object in list of dicts: {list_of_dicts[sub_menu_selection]}")
                print(f"Submenu items List of Dicts: {list_of_dicts}")
                if sub_menu_selection in range(len(subcategory)):
                    print(True)
                    # Store the item name as a variable
                    sub_item_name = list(subcategory.keys())[sub_menu_selection-1]
                    print(f"Sub item name: {sub_item_name}")

                    # Ask the customer for the quantity of the menu item

                    sub_item_quantity = input(f"How many {sub_item_name}/s would you like? ")
                    # Check if the quantity is a number, default to 1 if not (break condition)
                    if sub_item_quantity.isdigit():
                        sub_item_quantity = int(sub_item_quantity)
                    else:
                        sub_item_quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": sub_item_name,
                        "Price": list(subcategory.values())[sub_menu_selection-1],
                        "Quantity": sub_item_quantity
                    })

                    # Tell the customer that their input isn't valid
                    if sub_item_quantity == 1:
                        print(f"You did not enter a number")

                # Tell the customer they didn't select a submenu option
                else:
                    print(f"{sub_menu_selection} was not a submenu option.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_item_num} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

# Part II: Do something withe the Snack Items selected
    while True:
        # Ask the customer if they would like to order anything else
        # ___________________________________________________________
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        #____________________________________________________________
        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
