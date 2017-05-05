"""
Shopping List (Hackbright Prep dictionary code challenge)

Create a dictionary of shopping lists, and be able to 
    * add / remove lists
    * add / remove items from lists

"""


def add_new_shopping_list(lists_by_name, new_list_name):
    """Add new shopping list to dict: key is list name, value is empty list

    Will not allow duplicate shopping list names to be added.  This method
    is case-sensitive.

    Arguments:
      lists_by_name: dict of shopping lists
      new_list_name: string name of the new list to add
    Returns:
      None
    """

    # your code here! 
    pass


def remove_shopping_list(lists_by_name, list_name_to_remove):
    """Remove shopping list from shopping lists dict.

    If the shopping list name does not exist in the dictionary, print a message
    and do nothing. This method is case-sensitive.

    Arguments:
      lists_by_name: dict of shopping lists
      list_name_to_remove: string name of the list to remove
    Returns:
      None
    """

    # your code here! 
    pass


def add_to_shopping_list(lists_by_name, list_name, items):
    """Add given items to shopping list.

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
      items: list of items to add to the list
    Returns:
      None
    """

    # your code here! 
    pass


def remove_from_shopping_list(lists_by_name, list_name, items):
    """Remove given items from shopping list.

    If an item doesn't exist in the list, print an error, and continue to 
    attempt to remove the other items.

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
      items: list of items to remove from the list
    Returns:
      None
    """

    # your code here! 
    pass


def display_shopping_list(lists_by_name, list_name):
    """Print the contents of a shopping list.

    If the list is missing, return a string message saying so. This function is
    case sensitive.

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
    Returns:
      None
    """

    # your code here! 
    pass


def show_all_lists(lists_by_name):
    """Given a dictionary of shopping lists, print out each list.

    Arguments:
      lists_by_name: dict of shopping lists
    Returns:
      None
    """

    # your code here! 
    pass


def parse_string_of_items(items_string):
    """Split input sting on commas and return the list of items.

    Trim leading and trailing whitespace.

    Arguments:
      items_string: a string with 0 or more commas separating items
    Returns:
      list of strings
    """

    # list to return, starts out empty
    items = []

    # split the items_string on commas into a temporary list
    temp_items = items_string.split(',')

    # iterate through the temporary list and strip white space from each item
    # before appending it to the list to be returned
    for item in temp_items:
        items.append(item.strip())

    return items


def edit_shopping_list(lists_by_name, list_name, add_or_remove):
    """Get items from user and add / remove them from the shopping list

    Arguments:
      lists_by_name: dict of shopping lists
      list_name: string name of a shopping list
      add_or_remove: string that is either 'add' or 'remove', indicating whether
        the collected items should be added to or removed from the list
    Returns:
      None          

    """

    # if so, get items to add to the list
    input_str = raw_input('Please enter items separated by commas: ')

    # list-ify the input string
    items = parse_string_of_items(input_str)

    # add or remove, according to the argument
    if add_or_remove == 'add':
        add_to_shopping_list(shopping_lists_by_name, list_name, items)
    else:
        remove_from_shopping_list(shopping_lists_by_name, list_name, items)


def get_menu_choice():
    """Print a menu and asks the user to make a choice.

    Arguments:
      None
    Returns:
      int: the user's menu choice
    """
    print '\n    0 - Main Menu'
    print '    1 - Show all lists.'
    print '    2 - Show a specific list.'
    print '    3 - Add a new shopping list.'
    print '    4 - Add item(s) to a shopping list.'
    print '    5 - Remove items(s) from a shopping list.'
    print '    6 - Remove a list by name.'
    print '    7 - Exit the program.\n'

    choice = int(raw_input('Choose from the menu options: '))

    return choice


def execute_repl(shopping_lists_by_name):
    """Execute the repl loop for the control structure of the program. 

    (REPL stands for Read - Eval - Print Loop. For more info: 
    https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)

    Arguments:
        shopping_lists_by_name: dict of shopping lists
    Returns:
        None
    """

    while True:

        # get the next choice from the user
        choice = get_menu_choice()

        if choice == 0:
            # main menu

            continue  # continue goes to the next loop iteration

        elif choice == 1:
            # show all lists

            # call function to display all lists
            show_all_lists(shopping_lists_by_name)

        elif choice == 3:
            # Add a new shopping list

            # get name of list and add it
            list_name = raw_input('Enter the name for your list: ')
            add_new_shopping_list(shopping_lists_by_name, list_name)

            # get items for list and add them
            input_str = raw_input('Please enter items separated by commas: ')
            items = parse_string_of_items(input_str)
            shopping_lists_by_name[list_name] = items

        elif choice == 7:
            # quit
            break

        else:

            # all of the remaning choices require an existing list. First, run
            # code to get the list name from the user and verify it exists in
            # the dict

            # determine which list
            list_name = raw_input('Which list would you like to see? ')

            # test to see if the list is in the shopping list dict
            if list_name not in shopping_lists_by_name:
                # no list by this name :-(
                print 'There is no {} list.'.format(list_name)            
                continue

            # if the code reaches this point, it means the list exists in the
            # dictionary, so proceed according to which choice was chosen

            if choice == 2:
                # show a specific list

                display_shopping_list(shopping_lists_by_name, list_name)

            elif choice == 4:
                # Add item(s) to a shopping list

                # add items to the shopping list
                edit_shopping_list(shopping_lists_by_name, list_name, 'add')

            elif choice == 5:
                # Remove an item from a shopping list

                # add items to the shopping list
                edit_shopping_list(shopping_lists_by_name, list_name, 'remove')

            elif choice == 6:
                # remove list

                remove_shopping_list(shopping_lists_by_name, list_name)

# Main code here

shopping_lists_by_name = {}  # key is list name, value is [shopping list]
execute_repl(shopping_lists_by_name)
