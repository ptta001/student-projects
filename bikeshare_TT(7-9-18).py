import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input('Which one of the following three cities would you like to analyze?\n'
                  'Chicago, New York, or Washington DC?\n')
        if city == "Chicago" or city == "chicago": 
            city = 'chicago'
            break
        elif city == "New York" or city == "new york": 
            city = 'new york city'
            break
        elif city == "Washington DC" or city == "washington dc":
            city = 'washington'
            break
        else: print('Please include your input as one of the cities to analyze.\n')
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input('Which month would you like to review?\n'
                  'January, February, March, April, May, June, or all?\n')
        if month == "January" or month == "january": 
            month = 'january'
            break
        elif month == "February" or month == "february": 
            month = 'february'
            break
        elif month == "March" or month == "march":
            month = 'march'
            break
        elif month == "April" or month == "april": 
            month = 'april' 
            break
        elif month == "May" or month == "may":
            month = 'may'
            break
        elif month == "June" or month == "june": 
            month = 'june'
            break
        elif month == "All" or month == "all":
            month = 'all'
            break
        else: print('Please include your input as one of the valid month selections to select from.\n')    
       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input('Which day of the week would you like to review?\n'
                  'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n')
        if day == "Monday" or day == "monday": 
            day = 'monday'
            break
        elif day == "Tuesday" or day == "tuesday": 
            day = 'february'
            break
        elif day == "Wednesday" or day == "wednesday":
            day = 'Wednesday'
            break
        elif day == "Thursday" or day == "thursday": 
            day = 'thursday'
            break
        elif day == "Friday" or day == "friday":
            day = 'friday'
            break
        elif day == "Saturday" or day == "saturday": 
            day = 'saturday'
            break
        elif day == "Sunday" or day == "sunday":
            day = 'sunday'
            break
        elif day == "All" or day == "all":
            day = 'all'
            break
        else: print('Please include your input as one of the valid day selections to select from.\n')    

    print('-'*40)
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
  
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
            
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        print(df)      
   
    # filter by day of week if applicable
    if day != 'all':
         
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print(df)
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
  
    if popular_month == 1:
        print('Most Popular Month: January')
    elif popular_month == 2:
        print('Most Popular Month: February')
    elif popular_month == 3:
        print('Most Popular Month: March')
    elif popular_month == 4:
        print('Most Popular Month: April')
    elif popular_month == 5:
        print('Most Popular Month: May')
    else:
        print('Most Popular Month: June')
  
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week: ', popular_day)
    
    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', popular_sstation)

    # TO DO: display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    print('Most Popular End Station: ', popular_estation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'].astype(str) + ' to ' + df['End Station']
    popular_cstation = df['Station Combination'].mode()[0]
    print('Most Popular Station Combination: ', popular_cstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_seconds = df['Trip Duration'].sum()
    seconds = int(total_seconds)
    days, seconds = divmod(seconds, 24*60*60)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        print('Total travel time is %d days, %d hours, %d minutes, and %d seconds' % (days, hours, minutes, seconds))
    elif hours > 0:
        print('Total travel time is %d hours, %d minutes, and %d seconds' % (hours, minutes, seconds))
    elif minutes > 0:
        print('Total travel time is %d minutes and %d seconds' % (minutes, seconds))
    else:
         print('Total travel time is %d seconds' % (seconds,))
    

    # TO DO: display mean travel time
    average_seconds = df['Trip Duration'].mean()
    seconds = int(average_seconds)
    days, seconds = divmod(seconds, 24*60*60)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        print('Average travel time is %d days, %d hours, %d minutes, and %d seconds' % (days, hours, minutes, seconds))
    elif hours > 0:
        print('Average travel time is %d hours, %d minutes, and %d seconds' % (hours, minutes, seconds))
    elif minutes > 0:
        print('Average travel time is %d minutes and %d seconds' % (minutes, seconds))
    else:
         print('Average travel time is %d seconds' % (seconds,))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Here are the different types of users and their counts:\n')
    utype = (user_type).reset_index()
    print (utype.to_string(header=None, index=None))
    
    # TO DO: Display counts of gender
    try: 
        gender = df['Gender'].value_counts()
        print('\nHere are the counts by gender, if available:\n')
        gtype = (gender).reset_index()
        print (gtype.to_string(header=None, index=None))
    except: 
        print('\nWashington DC does not have the counts by gender available.\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try: 
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth reflected in this bikeshare data set is: ', int(earliest_birth))
        print('\nThe most recent year of birth reflected in this bikeshare data set is: ', int(recent_birth))
        print('\nThe most common year of birth reflected in this bikeshare data set is: ', int(common_birth))
    except: 
        print('Washington DC does not have the years of birth by bikeshare riders available.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()