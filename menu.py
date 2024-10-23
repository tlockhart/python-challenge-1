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
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")
print("")
# Customers may want to order multiple items, so let's create a continuous
# loop
# PLACE_ORDER IS THE WHILE LOOP EXIT CONDITION
#_____________________________________
place_order = True
#_____________________________________
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        #_____________________________________________________________
        # IMPORTANT: Store the menu category associated with its 
        # menu item number
        # {number: menu_item_name}
        #_____________________________________________________________
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    print("")
    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")
    print("")
    
    # # [Optional: Exit the loop if user typed 'q']
    if menu_category == 'q':
        break
    
    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        menu_category_key = int(menu_category)
        if menu_category_key in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[menu_category_key]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            print("")
            # Print out the sub menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item's (Desert) value is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "name": key + " - " + key2,
                            "price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "name": key,
                        "price": value
                    }
                    i += 1
            print("")
            # 2. Ask customer to input sub menu item number
            menu_selection = input("Type menu number: ")
            print("")
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                submenu_category_key = int(menu_selection)
                submenu_category_dict = menu_items[submenu_category_key]
                # 4. Check if the menu selection (submenu_category_key)is in the menu items (submenu_item_keys)
                submenu_item_keys = menu_items.keys()
                # print(f'Submenu Keys: {submenu_item_keys} Selection: {submenu_category_key} Object: {submenu_category_dict}')
                if submenu_category_key in submenu_item_keys:
                    # Store the item name as a variable
                    # print(f'Answer: {submenu_category_key in submenu_item_keys}')
                    submenu_category_name = submenu_category_dict["name"]
                    submenu_category_price = submenu_category_dict["price"]
                    # print(f'Submenu Category Name: {submenu_category_name}')
                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"Enter a quantity for the {submenu_category_name}, or the quantity will default to 1 if invalid: ")
                    selected_item = {}
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    selected_item = {
                        "name": submenu_category_name,
                        "price": submenu_category_price,
                        "quantity": quantity
                    }
                    # Add the item name, price, and quantity to the order list
                    order.append(selected_item)
                    # print(f'selected_item: {selected_item} Order_list: {order}')

                # Tell the customer they didn't select a menu option
                else:
                    print(f'You did not enter a valid menu option')
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
    
    while True:
        print("")
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        print("")
        # 5. Check the customer's input
        match keep_ordering.lower():
                # Keep ordering
                case 'y':
                    # place_order = True
                    break
                # Exit the keep ordering question loop
                case 'n':
                    place_order = False
                    print("Thank you for your order")
                    break
                case _:
                    print(f'Try again because your selection was invalid')
        print("")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order:

    # 7. Store the dictionary items as variables
    item_name = item["name"]
    item_price = " " + str(item["price"])
    item_quantity = " " + str(item["quantity"])
    
    # 8. Calculate the number of spaces for formatted printing
    # num_of_digits = len(str(abs(item_counter)))
    item_name_spaces = 26 - len(item_name)
    item_price_spaces = 8 - (len(str(item_price)))

    # 9. Create space strings
    item_name_string = ' ' * item_name_spaces
    item_price_string = ' ' * item_price_spaces
    
    # 10. Print the item name, price, and quantity
    print(f'{item_name}{item_name_string}|{item_price}{item_price_string}|{item_quantity}')

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
list_of_prices = [item['price'] * item['quantity']for item in order]

print("")

print(f'Total: ${sum(list_of_prices):.2f}')
# print(f'List of Prices: {list_of_prices}')