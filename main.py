import csv
import pandas as pd
import numpy as np
import fitting

"""
read_files reads the csv file and stores it as a list
"""


def read_files(filepath):
    with open(filepath, newline="") as csvfile:
        data = list(csv.reader(csvfile))
    return data


"""
filtering takes in the raw csv file and  a list of data (20.12.2020) 
as well as a range which it should read from the raw data. Then it separates the lines and puts them 
into there own lists. 
"""


def get_cases_raw(read, dates):
    date_ranged = []
    current = []
    for i in range(7, len(read)):
        date_ranged.append(read[i])

    for i in date_ranged:
        separated = i[0].split(";")
        for index, row in dates.iterrows():
            if separated[0] == row[0]:
                current.append(int(separated[1]))
    dates["Cases"] = current

    return dates


"""
Generates dates used for reference data
"""


def generate_dates(starting, length):
    remove = []
    dates_raw = pd.date_range(start=starting, periods=length)
    dates_filtered = dates_raw.strftime('%d.%m.%Y')
    date_series = pd.DataFrame({"Dates": dates_filtered})

    for i in dates_raw:
        if i.dayofweek == 5 or i.dayofweek == 6:
            remove.append(np.where(dates_raw == i)[0].item())
    date_series = date_series.drop(remove)
    date_series["time"] = date_series.index.to_list()
    return date_series


# Read data from file and get curve parameters
read = read_files("200325_Datengrundlage_Grafiken_COVID-19-Bericht.csv")

# Generates dates which are used to generate the line
data = generate_dates("15-02-2021", 46)

# Gets cases for these dates and fits curve
data = get_cases_raw(read, data)
data = fitting.to_log(data)
a, b = fitting.get_curve(data)
n, k = fitting.line_to_expo(a, b)
print(a, b)
print(n, k)

# Get The Prediction for the following dates:
prediction_dates = ["27.04.2021"]
case_comp = pd.DataFrame()
pred_cases = []
actual_cases = []
delta = []

for i in prediction_dates:
    pred, actual, delta_time = fitting.get_prediction(data, read, i)
    pred_cases.append(pred)
    actual_cases.append(actual)
    delta.append(delta_time)

case_comp.insert(0, "preCases", pred_cases)
case_comp.insert(1, "actCases", actual_cases)
case_comp.insert(2, "DeltaTime", delta)

# Generates and plots curve as well as print prediction:
print(case_comp)
data = fitting.generate_curve(data, n, k, prediction_dates[0])
fitting.plot(data)
