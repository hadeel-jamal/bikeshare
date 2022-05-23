import time
import pandas as pd
import numpy as np 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new york city','washington']
months = ['january','february','march','april','may','june']
days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')    
  
# using while loop and If statement to receive the uesr input and to avoide errors incase the user entered the wrong city name
    while True:
        city = input('could you choose a citry chicago new york city washington: ').lower()    
        if city not in cities:
            print('choose the correct city name')
        else:
            break
    
# using while loop and If statement to receive the uesr input and to avoide errors incase the user entered the wrong month        
    while True:    
        month = input('choose a month from january to june or all: ').lower()
        if  month not in months and month != 'all':
            print('please enter a correct month or all')
        else:
            break
        
# using while loop and If statement to receive the uesr input and to avoide errors incase the user entered the wrong day        
    while True:
        day = input('could you please choose a week day or all: ').lower()
        if day not in days and day != 'all':
            print('please enter a correct day')
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
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]
    
    
    return df 



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common monthe is: ',most_common_month)

    # display the most common day of week
    most_day_of_week = df['day'].mode()[0]
    print('the most common day is: ',most_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('the most common hour to start a ride is: ',most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('the most used start station is: ',most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('the most used end station is: ',most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['frequent trip'] = 'from'  +  df['Start Station']  +  'to'  +  df['End Station']
    most_frequent_trip = df['frequent trip'].mode()[0]
    print('the most frequent trip is :',most_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is: ',total_travel_time)
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('user types counts are: ',counts_of_user_types)

    # Display counts of gender
   
    if 'Gender' in df.columns:
        counts_of_user_gender = df['Gender'].value_counts()
        print('counts of uesrs gender is: ',counts_of_user_gender)
    else:
        print('there is no Gender coloumn in this dataset')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = df['Birth Year'].min()
        recent_year_of_birth = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        
        print('the oldest user was born in: ',earliest_year_of_birth ,'\nthe youngest user was born in: ',recent_year_of_birth,'\nand the most common year of birth for users is:' ,most_common_birth_year)
    else:
        print('there is no Birth Year coloumn in this dataset')
    
def user_responce(df):
    """
    we ask the uesers if they want to display row data from the dataframe according to their choice of city , month and day, it shows 5 lines of raw data """
    view_data = input('\nWould you like to display 5 lines of raw data? Enter yes or no\n').lower()
    start_column = 0
    sking_again = True
    
    while (sking_again):
        if view_data == 'no':
            break
        print(df.iloc[start_column:start_column + 5])
        start_column += 5
    
        continue_veiwing = input("would you like to continue diplaying more data? Enter yes or no\n ").lower()
        if continue_veiwing == "no": 
           sking_again = False
    
    
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_responce(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main() 