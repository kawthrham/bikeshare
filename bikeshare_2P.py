import time
import pandas as pd


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
     
   # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city  = str(input('Would you like to see the data for Chicago, New York City, or Washington? Choose one of them.\n ').lower().title())
        try:
            if city in ['Chicago', 'New York City', 'Washington']:             
                print(city)
                break
            else:
                print ('Invalid city! Please choose from Chicago, New York City, or Washington.')            
        except ValueError:
            print('Value Error occurred')
    # get user input for month (all, January, February, March, April, May, June)    
    while True :
        month = str (input('Which month? All, January, February, March, April, May, June ? \n').lower().title())
        try:
            if month in ['All', 'January', 'February', 'March', 'April', 'May', 'June']:             
                print(month)                
                break
            else:
                print ('Invalid month! Please choose from which is appears to you .')              

        except ValueError:
            print ('Invalid month! Please choose a valid month or "all" for no fillter.'.lower().title())
            
     # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day  = str (input('Choose which day  of the week? All, Sunday, Manday, Tuesday, Wednesday,Thursday, February, or Saturday? \n').lower().title())
        try:
            if day in ['All', 'Sunday', 'Manday', 'Tuesday', 'Wednesday','Thursday', 'February', 'Saturday']:
                 print (day)
                 
                 break
            else:
                 print ('Invalid day! Please choose a valid day or "all" for no fillter.')
        except ValueError:
             print ('Invalid day! Please choose a valid day or "all" for no fillter.')
        
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data from CITY_DATA
    df = pd.read_csv(CITY_DATA[city])
    
    #convert 'Date' column to datetime formate
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #filter by month
    if month != 'all':
         #Extract the month from the 'Start Time' column
         df['month'] = df['Start Time'].dt.month
         months = ['January', 'February', 'March', 'April', 'May', 'June']
         month = months.index(month) + 1
    #filter by the specified month
         df = df[df['month'] == month] 
         
    #filter by day
    if day != 'all':
        #Extract the day of the week from the 'Date' column
        df['day'] = df['Start Time'].dt.day_name()
        #filter by the specified month
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert 'Start Time' column to datatime format-----
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #---Extract month, day of the week, and hour from 'Start Time'
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print("The most common month: ", most_common_month)

    # display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]
    print("The most common day of the week: ", most_common_day)

    # display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print("The most common start hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    return df

    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    #Calculate most commoly start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", most_common_start_station)

    # display most commonly used end station
    #Calculate most commoly end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    #calculation:
    most_frequent_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start and end station: ', most_frequent_trip)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    return df   


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    #Calculation
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:" , total_travel_time)

    # display mean travel time
    #Calculation:
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:" , mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    return df
    
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print ("Counts of user types: \n", user_type_counts.to_string(dtype=False))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print ("Counts of gender: \n", gender_counts.to_string(dtype=False))
    else:
        print("Gender information not available. \n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        
        print(" Earliest birth year: ", earliest_birth_year)
        print(" Most recent birth year: ", most_recent_year)
        print(" Common recent birth year: ", most_common_birth_year)
    else:
        print("Birth year information not available. \n")
        
    execution_time = time.time() - start_time

    print("\nThis took %s seconds." % (execution_time))
    
    return df
    
    
def display_row_data(df):
    """ Display the row data 5 rows at a time.  """
    current_row = 0
    view_row_data = input("Would you like to see the row data? (yes/no) \n").lower()
    if view_row_data == 'yes':  
        while True:        
                display_data = df[current_row:current_row + 5]
                print(display_data)
            # ask the user if they want to see the row data                            
                if current_row + 5 >= len(df):
                  print("End of data.")
                  break
                show_more = input("Would you like to see 5 more rows of the data? (yes/no) \n").lower()
                if show_more != 'yes':
                    print('Stopping display data.')
                    break
                current_row += 5   
             
    else:
         print ("No row data will be displayed. \n")
       
  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('-'*40)
        time_stats(df)
        print('-'*40)
        station_stats(df)
        print('-'*40)
        trip_duration_stats(df)
        print('-'*40)
        user_stats(df)
        print('-'*40)
        display_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
