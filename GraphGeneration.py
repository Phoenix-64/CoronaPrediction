import csv
import plotly.graph_objects as go
import numpy as np

"""read_files reads the csv file and stores it as a list"""


def read_files(filepath):
    with open(filepath, newline="") as csvfile:
        data = list(csv.reader(csvfile))
    return data


"""filtering takes in the raw csv file and  a list of dates (20.12.2020) 
as well as a range which it should read from the raw data. Then it separates the lines and puts them 
into there own lists. """


def filtering(data, dates, file_range):
    date_ranged = []
    current = []
    for i in range(7, file_range):
        date_ranged.append(data[i])

    for i in date_ranged:
        separated = i[0].split(";")
        for x in dates:
            if separated[0] == x:
                current.append(int(separated[1]))
        date_ranged[date_ranged.index(i)] = separated

    return current

def fitting(cases, time):
    # Here is the Function that should be fitted: y = a*x^b
    # then we take the Natural log of both sides:  ln(y) = ln(a) + b*ln(x)
    # this is now a linear Equation with slope ln(a) and intercept b
    # on which we do box least square fitting
    #
    a_top = []
    a_bottom = []
    a1 = 0
    b = 0
    cases_mean = np.mean(cases)
    time_mean = time / 2

    for i in range(0, len(cases)):
        a_top.extend((i + time_mean) * (cases[i] + cases_mean))
        a_bottom.extend(cases[i])

    # y_new =



selection = []
# Dates to be excluded:
exclude = ["03.10.2020", "04.10.2020", "10.10.2020", "11.10.2020", "17.10.2020", "18.10.2020", "04.10.2020",
           "24.10.2020", "25.10.2020", "27.10.2020", "28.10.2020", "29.10.2020", "30.10.2020", ]

# Generating Dates I want:
for i in range(1, 31):
    if i < 10:
        selection.append("0" + str(i) + ".10.2020")
    else:
        selection.append(str(i) + ".10.2020")

read = read_files("200325_Datengrundlage_Grafiken_COVID-19-Bericht.csv")
y = filtering(read, selection, 400)

# Removes dates that should be excluded:
for i in exclude:
    if i in selection:
        y[selection.index(i)] = None

# Graphing
fig = go.Figure(data=go.Scatter(y=y, x=selection, connectgaps=True))
fig.show()
