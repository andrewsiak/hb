"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []


# converted into function
def data_sales_report(file_name):


    complete_report = {}

    # used with open to auto close file
    with open(file_name) as f:
    

# combined modifier functions
        for line in f:
            line = line.rstrip().split('|')

            sales_person = line[0]
            melons_sold = line[2]
            melons_sold = int(melons_sold)

            if sales_person in salespeople:
                complete_report[sales_person] += melons_sold
                
            else:
                complete_report[sales_person] = melons_sold
    for sales_person, melons_sold in complete_report:   
        print(f'{sales_person} sold {melons_sold} melons')                    
    return complete_report

     
    # need to clean this up so it doesnt rely on a printf and separate this 


