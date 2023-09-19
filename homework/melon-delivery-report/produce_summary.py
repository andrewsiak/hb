


def melon_delivery_summary(day):
    """Updating file to remobe redundancy and provide a daily report of melons stuffs"""

    print("Day", day)    
    file_name = "um-deliveries-day-1.txt"
        # f string
    the_file = open(file_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        # would not have needed this if i didnt break the text with extra lines
        if line == "":
            continue

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


for input_day in range(1,4):
    melon_delivery_summary(input_day)