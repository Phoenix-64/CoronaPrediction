import csv
import pandas as pd
import numpy as np
import fitting

"""read_files reads the csv file and stores it as a list"""


def read_files(filepath):
    with open(filepath, newline="") as csvfile:
        data = list(csv.reader(csvfile))
    return data


"""filtering takes in the raw csv file and  a list of dates (20.12.2020) 
as well as a range which it should read from the raw data. Then it separates the lines and puts them 
into there own lists. """


def filtering(data, dates):
    date_ranged = []
    current = []
    for i in range(7, len(data)):
        date_ranged.append(data[i])

    for i in date_ranged:
        separated = i[0].split(";")
        for index, row in dates.iterrows():
            if separated[0] == row[0]:
                current.append(int(separated[1]))
    dates["Cases"] = current

    return dates


def generate_dates(starting, length):
    remove = []
    dates_raw = pd.date_range(start=starting, periods=length)
    dates_filtered = dates_raw.strftime('%d.%m.%Y')
    date_series = pd.DataFrame(dates_filtered)

    for i in dates_raw:
        if i.dayofweek == 5 or i.dayofweek == 6:
            remove.append(np.where(dates_raw == i)[0].item())
    date_series = date_series.drop(remove)

    return date_series




read = read_files("200325_Datengrundlage_Grafiken_COVID-19-Bericht.csv")

dates = generate_dates("26-09-2020", 20)
data = filtering(read, dates)

fitting.plot(data)




