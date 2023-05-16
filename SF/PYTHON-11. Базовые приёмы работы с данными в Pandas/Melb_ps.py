import pandas as pd

melb_data = pd.read_csv('D:/Миша/Ide/SF/PYTHON-11. Базовые приёмы работы \
                        с данными в Pandas/data/melb_data_ps.csv', sep=',')
melb_df = melb_data.copy()

melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
years_sold = melb_df['Date'].dt.year
melb_df['MonthSale'] = melb_df['Date'].dt.month
melb_df['MonthSale'].value_counts(normalize=True)
delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01')
melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
melb_df = melb_df.drop('YearBuilt', axis=1)
melb_df['WeekdaySale'] = melb_df['Date'].dt.day_of_week
weekend_count = melb_df['WeekdaySale'].value_counts()
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) |
                        (melb_df['WeekdaySale'] == 6)].shape[0]


def get_street_type(address):
    exclude_list = ['N', 'S', 'W', 'E']
    address_list = address.split(' ')
    street_type = address_list[-1]
    if street_type in exclude_list:
        street_type = address_list[-2]
    return street_type


street_types = melb_df['Address'].apply(get_street_type)
popular_stypes = street_types.value_counts().nlargest(10).index
print(popular_stypes)
