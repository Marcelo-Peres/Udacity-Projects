
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("\nReading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("\nOk!")

# Let's check how many rows do we have
print("\nNumber of rows:\n")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("\nRow 0:\n")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("\nRow 1:\n")
print(data_list[1])

input("\nPress Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\nTASK 1: Printing the first 20 samples:\n")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]
print("The first 20 Rows:\n")
for rows in range(20):
     print(str(rows+1) +" - "+ str(data_list[rows]))

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("\nPress Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples\n")
print("The first 20 genders:\n")

for rows in range(20):
    print(str(rows+1) +" - "+ str(data_list[rows][6]))

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("\nPress Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    '''
        Right here you can count users by using a def:
            param1: Generate a data list.
            param2: Create a index.
            Return: Column List.
    '''
    column_list = []
    for rows in data:
        column_list.append(rows[index])
# Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples\n")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for rows in range(len(data_list)):
    if data_list[rows][6] == 'Male':
        male += 1
    if data_list[rows][6] == 'Female':
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found\n")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    '''
        Right here you can count users by using a def:
            param1: Generate a data list.
            Return: Quantity by Gender
    '''
    male = 0
    female = 0

    for rows in range(len(data_list)):
        if data_list[rows][6] == 'Male':
            male += 1
        elif data_list[rows][6] == 'Female':
            female += 1

    return [male, female]

print("\nTASK 5: Printing result of count_gender\n")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.

def most_popular_gender(data_list):
    '''
        Right here you can count users by using a def:
            param1: Generate a data list.
            Return: Column List by gender
    '''
    answer = ""
    if male > female:
        answer = 'Male'
    elif female > male:
        answer = 'Female'
    return answer

print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("\nPress Enter to continue...")

# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!\n")

def count_user(data_list):
    '''
        Right here you can count users by using a def:
            param1: Generate a data list.
            Return: List by Users
    '''
    customer = 0
    subscriber = 0

    for rows in range(len(data_list)):
        if data_list[rows][5] == 'Customer':
            customer += 1
        elif data_list[rows][5] == 'Subscriber':
            subscriber += 1

    return [customer, subscriber]

user_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User')
plt.xticks(y_pos, types)
plt.title('Quantity by User')
plt.show(block=True)

print('User Type: \n')

user_counter = {}

for user in user_list:
    user_counter[user] = user_counter.get(user, 0) + 1

for user, value in user_counter.items():
    print("User {} total values = {}".format(user, value))

input("\nPress Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list),'\n')
answer = 'Because we have a total of '+str(len(data_list))+' rows in list splitted as showed below:'
print("Answer:", answer,"\n")
gender_list = column_to_list(data_list, -2)

gender_counter = {}

for gender in gender_list:
    gender_counter[gender] = gender_counter.get(gender, 0) + 1

for gender, value in gender_counter.items():
    if gender == '':
        print("Gender Empty total values = {}".format(value))
    else:
        print("Gender {} total values = {}".format(gender, value))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = sorted(list(map(float, trip_duration_list)))
tdl = trip_duration_list

min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

min_trip = round(tdl[0])
max_trip = round(tdl[-1])
mean_trip = round(sum(tdl)/len(tdl))

if len(tdl)%2 > 0:
    median_trip = round(tdl[(len(tdl)//2+len(tdl)%2)])
else:
    median_trip = round(tdl[((len(tdl)//2-1)+(len(tdl)//2+1))//2])

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("\nPress Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
start_station = sorted(set(column_to_list(data_list, 3)))
print("\nTASK 10: Printing start stations:\n")

for rows, start_station in enumerate(start_station):
    print(str(rows+1)+' - ', str(start_station))

start_station = sorted(set(column_to_list(data_list, 3)))
print('\nTotal Available Start Stations: ',len(start_station), '\n')

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(start_station) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("\nPress Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it does. Example:
# def new_function(param1: int, param2: str) -> list:
print('\nTASK 11: All functions were explained.\n')

"""
      Example function with annotations.
      Args:
          param1: The first parameter.
          param2: The second parameter.
      Returns:
          List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")

answer = "yes"

def count_items(column_list):
    
    item_types = list(column_list)
    item_counter = {}

    for item in item_types:
        item_counter[item] = item_counter.get(item, 0) + 1

    item_types = list(item_counter.keys())
    count_items = list(item_counter.values())


    return item_types, count_items



if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 12: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 12: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 12: Returning wrong result!"
    # -----------------------------------------------------
