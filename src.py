from Table import Table

overhead = 0.35
growth_rate = 0.10
num_years = 3
tab_stack = []

def console_input():
    more_tab = True
    while more_tab:

        print("What is the name of your table?\n")
        tab_name = input()

        print("What is the average record length?\n")
        avg_record_size = input()

        print("What is the table's initial size?\n")
        init_tab_size = input()

        new_table = Table(tab_name, avg_record_size, init_tab_size)
        tab_stack.append(new_table)

        print("Are there more tables? (Y/N)")
        answer = input()

        if answer == "N":
            more_tab = False

def read_input_csv():
    input_file = open('input.csv', 'r')
    for line in input_file:
        tab_name = line.split(',')[0]
        avg_record_size = line.split(',')[1]
        init_tab_size = line.split(',')[2]
        new_table = Table(tab_name, avg_record_size, init_tab_size)
        tab_stack.append(new_table)


def print_init_volumetrics():
    total = 0
    print("INITIAL TABLE VOLUMETRICS")
    print("--------------------------------------\n")
    for table in tab_stack:
        answer = table.calc_initial_volume(overhead)
        str_answer = "{:,.2f}".format(answer)
        print(table.tab_name + " : " + str_answer + "\n")
        total += answer
        str_total = "{:,.2f}".format(total)
    print("--------------------------------------\n")
    print("Database Total: " + str_total)
    print("--------------------------------------\n")

def print_growth_volumetrics():
    total = 0
    print("TABLE VOLUMETRICS AFTER " + str(num_years) + " YEARS")
    print("--------------------------------------\n")
    for table in tab_stack:
        answer = table.calc_growth_volume(overhead, growth_rate, num_years)
        str_answer = "{:,.2f}".format(answer)
        print(table.tab_name + " : " + str_answer + "\n")
        total += answer
        str_total = "{:,.2f}".format(total)
    print("--------------------------------------\n")
    print("Database Total: " + str_total)
    print("--------------------------------------\n")

def print_volumetrics():
    print_init_volumetrics()
    print_growth_volumetrics()

made_selection = False
while made_selection == False:
    print("Are you going to input the table information yourself, or read input.csv?\n"
          + "'I' for input, 'R' for read.\n")
    selection = input()

    if selection == "I":
        made_selection = True
        console_input()
    elif selection == "R":
        made_selection = True
        read_input_csv()
    else:
        print("Wrong input. Must be 'I' or 'R'.\n")


print_volumetrics()
