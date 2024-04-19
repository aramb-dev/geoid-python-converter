# GeoID Python Converter

This is a Python script that converts GeoIDs/FIPS county codes in a `CSV` Dataset to `County Name, StateCode`.

Video DEMO:

https://github.com/aramb-dev/geoid-python-converter/assets/65731416/53a6f370-2278-479a-8d17-01a907bfe5e1


## Instructions

Download the zip file in the releases.

Extract the zip file.

Optional: Open the `geoid.py` file in your favorite text editor.

Drop your dataset into the same folder as the `geoid.py` file.

Run the script.

Enter the name of the dataset file without inserting the `.csv` extension at the end. The script will automatically add the `.csv` extension.

Copy and Paste the name of the column that contains the GeoID/FIPS county codes. Do not change the format of the column name.

The script will then ask you to enter the name of the new `.csv` file. If you want to keep it the same with `updated_` added at the beginning of the file, enter `12`.

The script will then output the new `.csv` file with the updated GeoIDs/FIPS county codes.

##

Credits: [David Hochman](https://tbed.org) county [geoIDs](https://tbed.org/demo/index.php?function=search&tablename=county_vw).

If you find any issues, please [open an issue on GitHub](https://github.com/aramb-dev/geoid-python-converter/issues).

If you have any suggestions, please [open a PR on GitHub](https://github.com/aramb-dev/geoid-python-converter/pulls).