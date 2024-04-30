import pandas as pd

def df_geo_to_county():
    dataset = input("""Copy the dataset csv file name and paste it here:
(Note: Be sure to keep the file in the same folder.
Do not add .csv at the end of the file name)
> """)
    # Load geoid.csv and dataset_1.csv
    geoid_df = pd.read_csv('geoid.csv')
    dataset = dataset + '.csv'
    dataset_df = pd.read_csv(dataset)
    geoid_column = input("""What is the name of the column in the dataset that contains the geoID?
Note: Be sure to keep it in the exact format of as it appears in the dataset.
> """)
    geoid_column = str(geoid_column)
    # Remove 'geoId/' from place column
    dataset_df[geoid_column] = dataset_df[geoid_column].str.replace('geoId/', '')
    # Define a function to convert geoID to County Name, State
    def geo_to_county(geo_id):
        county_state = geoid_df.loc[geoid_df['id'] == int(geo_id), ['county', 'state']]
        return f"{county_state['county'].values[0]}, {county_state['state'].values[0]}"

    # Apply the function to convert geoID to County Name, State
    dataset_df[geoid_column] = dataset_df[geoid_column].apply(geo_to_county)
    csv_name = input("""What would you like to name the new CSV file?
Enter 12 if you would like to name it updated_{dataset}.csv.
Note: Do not add .csv at the end of the file name.
> """)
    csv_name = str(csv_name)
    if csv_name == '12':
        dataset_df.to_csv(f'updated_{dataset}.csv', index=False)
        print(f"Updated {dataset} has been saved as updated_{dataset}.csv")
        exit(1)
    # Write updated dataset_1 to a new CSV file
    dataset_df.to_csv(csv_name, index=False)

    print("Updated dataset_1.csv has been saved as updated_dataset_1.csv")

df_geo_to_county()