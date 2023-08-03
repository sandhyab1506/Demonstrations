# function to display the content in the specified format
# accepts a list as input
# no output returned
def menu_list_to_print(items_list):
    item_length = len(items_list)
    item_counter = 0
    items_to_print = ""
    while item_counter < item_length:
        if item_counter == 0:
            items_to_print = items_list[0].capitalize()
        elif item_counter == item_length - 1:
            items_to_print = f"{items_to_print} or {items_list[item_counter].capitalize()}"
        else:
            items_to_print = f"{items_to_print}, {items_list[item_counter].capitalize()}"
        item_counter = item_counter + 1
    print(items_to_print)


# function to sort the list supplied in ascending order of corresponding prep times
# accepts a menu list as input & prep times as a dictionary
# returns the sorted menu items list
def menu_to_sort(menu_items_list, prep_times_dic):

    menu_items_with_prep_times = {}
    sorted_list_by_prep_times = []

    for menu_item in menu_items_list:
        for item_with_prep_time in prep_times_dic:
            if menu_item == item_with_prep_time:
                menu_items_with_prep_times[menu_item] = prep_times_dic[item_with_prep_time]
                break
            else:
                menu_items_with_prep_times[menu_item] = 0

    sorted_dic_by_prep_times = sorted(menu_items_with_prep_times.items(), key=lambda prep_times: prep_times[1])

    for item in sorted_dic_by_prep_times:
        sorted_list_by_prep_times.append(item[0])

    return sorted_list_by_prep_times
