
def register_customers(group_size):
    global current_tables
    if group_size <= table_capacity:
        if current_tables > 0:
            current_tables -= 1
            print(f"Group of {group_size} people is seated at a table. Free tables left: {current_tables}.")
        elif current_tables < max_tables:
            current_tables += 1
            print(f"New table is created.Group of {group_size} people is seated at a table. Free tables left: {current_tables}.")
        else:
            print(f"Failed to accommodate a group of {group_size} people. The table limit has been reached")
    else:
        print(f"A group of {group_size} people is to big for one table.Denied")


if __name__ == '__main__':
    current_tables = 3
    max_tables = 5
    table_capacity = 4
    customers_group_1 = 3
    customers_group_2 = 5
    customers_group_3 = 2
    customers_group_4 = 4
    customers_group_5 = 6
    customers_group_6 = 2
    customers_group_7 = 3
    customers_group_8 = 1
    customers_group_9= 2
register_customers(customers_group_1)
register_customers(customers_group_2)
register_customers(customers_group_3)
register_customers(customers_group_4)
register_customers(customers_group_5)
register_customers(customers_group_6)
register_customers(customers_group_7)
register_customers(customers_group_8)
register_customers(customers_group_9)