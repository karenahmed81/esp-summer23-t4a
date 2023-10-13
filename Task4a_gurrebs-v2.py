import pandas as pd
import matplotlib.pyplot as plt

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show average sales data")
        print("3. Show total sales")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8: #validate choice
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1] #-1 because list indexing starts at 0
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date between 03/03/2023 and 31/05/2023 (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date) #convert input to date format
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date between 03/03/2023 and 31/05/2023 (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date) #convert input to date format
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") #load CSV file into Pandas DataFrame
    df2 = df1.loc[df1['Menu Item'] == item] #locate row in Menu Item which is equal to selected item
    df3 = df2.loc[:,startdate:enddate] #select data between the chosen date ranges

    return df3 #return chosen data

def get_lunch_service(item, startdate, enddate):
    
    #load CSV file into dataframe
    all_data = pd.read_csv("Task4a_data.csv")
    
    #get lunch data
    lunch_data = all_data.loc[(all_data['Menu Item'] == item) & (all_data['Service'] == 'Lunch')]
    
    try:
         #specify range of data - start and end dates
        lunch_range = lunch_data.loc[:, startdate:enddate]
        return lunch_range 
    except KeyError:
        print("Sorry, you did not enter a valid date range")
        exit()
   
         
   

def get_dinner_service(item, startdate, enddate):
    #load CSV file into dataframe
    all_data = pd.read_csv("Task4a_data.csv")
    
    #get dinner data
    dinner_data = all_data.loc[(all_data['Menu Item'] == item) & (all_data['Service'] == 'Dinner')]
    
    #get dinner date range
    dinner_range = dinner_data.loc[:, startdate:enddate]
    
    return dinner_range

def find_avg(startdate, enddate):
    #load CSV file into data frame
    data = pd.read_csv("Task4a_data.csv")

    #calculate average values
    average = data.groupby(['Menu Item', 'Service']).mean()
    
    try:
        #get average sales data
        average_out = average.loc[:, startdate:enddate].sum(axis=1, numeric_only=True)
        print("The average sales from {} to {} were ".format( startdate, enddate))
        print(average_out)
    
        #display as a bar chart
        average_out.plot.bar(color=['b','b', 'g', 'g', 'r', 'r', 'c', 'c', 'm', 'm', 'y', 'y', 'k', 'k', 'purple', 'purple'])
        plt.show()
    except KeyError:
        print("Sorry, you did not enter a valid date range")
        exit()
        

def find_totals(startdate, enddate):
    data = pd.read_csv("Task4a_data.csv")
    
    #calculate totals
    total = data.groupby(['Menu Item']).sum()
    try:
        #get total sales data
        total_out = total.loc[:, startdate:enddate].sum(axis=1, numeric_only = True)
        print("The total sales from {} to {} were: ".format(startdate, enddate))
        print(total_out)
    
        #find max value
        max_values = total_out.max()
        max_label = total_out.idxmax()
 
        print("The best selling item from {} to {} was {} with {} sales".format(startdate, enddate, max_label, max_values))
    
        #create a pie chart
        plt.pie(total_out, labels=total_out.index, autopct='%1.1f%%')
        plt.title('Total sales from {} to {}'.format(startdate, enddate))
        plt.show()
        
    except KeyError:
        print("Sorry, you did not enter a valid date range")
        exit()
     
main_menu = menu()
match main_menu:
    case 1: #get sales data for lunch and dinner
        
        item = get_product_choice() #get item name
        start_date = get_start_date() #get start date
        end_date = get_end_date() #get end date

        #get sales for lunch items
        print()
        lunch_data = get_lunch_service(item, start_date, end_date)
        print("Here is the sales data for lunch for {} between dates {} and {}:".format(item, start_date, end_date))
        try:
            lunch_no_index = lunch_data.to_string(index=False)
            print(lunch_no_index)
            print()
        except Exception:
            print("You have entered an invalid date")
    
        #get sales for dinner items
        dinner_data = get_dinner_service(item, start_date, end_date)
        print("Here is the sales data for dinner for {} between dates {} and {}:".format(item, start_date, end_date))
        dinner_no_index = dinner_data.to_string(index=False)
        print(dinner_no_index)
        print()
    
    case 2: #get average sales data
        start_date = get_start_date() #get start date
        end_date = get_end_date() #get end date
        
        #find average sales for all items
        find_avg(start_date, end_date)
    
    case 3: #total sales for all items
        start_date = get_start_date()
        end_date = get_end_date()
        
        #find total sales for all items
        find_totals(start_date, end_date)
