melon_cost = 1.00

# tokenize the list (txt file)
# split into categories, 
# find compare to pricing who underpaid
def order_data(filename):
    
    # save to new array
    order_info = []

    # open the file
    the_file = open(filename)

    # tokenize the list
    for line in the_file:
        items = line.split('|')

        # label categories of the txt file
        order_number = items[0]
        customer_name = items[1]
        melon_count = float(items[2])
        customer_paid = float(items[3])
        over_under = (melon_cost * melon_count) - customer_paid


        #write to new array
        order_info.extend([order_number, customer_name, melon_count, customer_paid, over_under])    

        # read the solution and realize you dont need an array, and just have a printf statement
        # did not do underpaid, overpaid, zero balance specific statements
        print(f"{customer_name} ordered {melon_count} melons, for {customer_paid}, remaining balance is {over_under:.2f}")
        
    # close the file
    the_file.close()




# def print_payment_status(payment_data_filename):
#     """Calculate cost of melons and determine who has underpaid."""

#     payment_data = open(payment_data_filename) # open the file

#     # Iterate over lines in file
#     for line in payment_data:
#         # Split line by '|' to get a list of strings
#         order = line.split('|')

#         # Get customer's full name
#         full_name = order[1]

#         # Split `customer_name` by space (' ') to get
#         # a list of [first_name, last_name].
#         #
#         # Then, assign first name (at index 0) to `customer_first`
#         first_name = full_name.split(" ")[0]

#         # Get no. of melons in the order and amount customer paid
#         melons_qty = float(order[2])  # also ok to typecast melons_qty as an int
#         amt_paid = float(order[3])

#         # Calculate expected price of customer's order
#         expected_price = melons_qty * MELON_COST

#         # Print general payment info
#         print(f"{full_name} paid ${amt_paid:.2f}, expected",
#               f"${expected_price:.2f}")

#         # Print payment status
#         #
#         # If customer overpaid, print that they've overpaid for their melons. If
#         # customer underpaid, print that they've underpaid for their melons.
#         if expected_price < amt_paid:
#             print(f"{first_name} has overpaid for their melons.")

#         elif expected_price > amt_paid:
#             print(f"{first_name} has underpaid for their melons.")

#     # Close the file
#     payment_data.close()


# Call the function
# print_payment_status("customer-orders.txt")





# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
