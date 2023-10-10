"""Restaurant rating lister."""


def dicting_rest_data(file_name):
    
    score_dict = {}

    with open(file_name) as file:
    
        for line in file:
            line = line.replace('\n', '').split(":")
            score_dict[line[0]] = score_dict.get(line[0], line[1])
    
    return score_dict
# print(dicting_rest_data("scores.txt"))
        

def rating_in_alph_order(restaurants):

    print()
    for restaurant in sorted(restaurants):
        print(f"{restaurant} is rated at {restaurants[restaurant]}.")
    print()


def entry_from_user():

    print("Enter your restaurant name: ")
    restaurant_name = input(">>>")
    
    if restaurant_name == "quit" or restaurant_name == "q":
        
        print("Thanks for playing!")
        return "quit"

    while True:        

        print()
        print("Enter your score rating for this restaurant:")
        restaurant_score = input(">>>")

        if restaurant_score.isdigit():
            restaurant_score = int(restaurant_score)

            if restaurant_score >= 1 and restaurant_score <= 5:
            
                return [restaurant_name, restaurant_score]

            else:
                print("Our ratings are only 1-5, please enter 1, 2, 3, 4, or 5: ")
        else:
            print("Sorry, please enter 1-5 as the rating.")


#new_restaurant = [name of restaurant, score]
#current_restaurants = {rest1:score1, rest2:score2, ect}
def add_user_restaurants(new_restaurant, current_restaurants):
    
    current_restaurants[new_restaurant[0]] = current_restaurants.get(new_restaurant[0], new_restaurant[1])

    return current_restaurants



restaurant_collection = dicting_rest_data('scores.txt')

while True:
    rating_in_alph_order(restaurant_collection)
    user_input_restaurant = entry_from_user()
    if user_input_restaurant == "quit":
        break
    add_user_restaurants(user_input_restaurant, restaurant_collection)

    