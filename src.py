from Table import Table

overhead = 0.35
growth_rate = 0.10
num_years = 3

more_tab = True

tab_stack = []

# Are there more tables?
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


total = 0
print("\n\n\n TABLE VOLUMETRICS:")
for table in tab_stack:
    answer = table.calc_volumization(overhead, growth_rate, num_years)
    print(table.tab_name + " : " + str(answer) + "\n")
    total += answer


print("--------------------------------------\n\n")
print("Database Total: " + str(total))


