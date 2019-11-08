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
        city = input("\nPlease select your city. new york city, chicago or washington?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Please select correct city. Try again.")
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n please select the month from january, february, march, april, may, june or type 'all' for all months\n").lower()
        if month not in ('january','february','march', 'april', 'may', 'june', 'all'):
            print("Please select correct month. Try again.")
            continue
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nPlease select your day from sunday, monday, tuesday, wednesday, thursday, friday, saturday or type 'all' for all days.\n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all'):
            print("Please select correct day. Try again.")
            continue
        else:
            break   

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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()] 
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nMost commonly use Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly use end Station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_combine_station = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost commonlt use combine Start station and End station:',common_combine_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel time:',Total_Travel_Time/864000, "Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time:', Mean_Travel_Time/60, "Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type:\n',user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #df = df.drop(['month', 'day_of_month'], axis = 1)
    row_index = 0

    view_data = input('\n would you like to see raw data for this compution?Please write yes or no \n').lower()
    while True:
        if view_data == 'no':
            return
        if view_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
            view_data = input('\n would you like to see five more raw data for this compution?Please write yes or no \n').lower()
        

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
