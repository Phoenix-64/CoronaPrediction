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

def generat_graph(y_data, sel, exc):

    for i in exc:
        if i in sel:
            print(i)
            y_data[sel.index(i)] = None

    fig = go.Figure(data=go.Scatter(y=y_data, x=sel, connectgaps=True))
    fig.show()





selection = []

exclude = ["03.10.2020", "04.10.2020", "10.10.2020", "11.10.2020", "17.10.2020", "18.10.2020", "04.10.2020",
           "24.10.2020", "25.10.2020", "27.10.2020", "28.10.2020", "29.10.2020", "30.10.2020", ]

# Generating Dates I want:
for i in range(1, 31):
    if i < 10:
        selection.append("0" + str(i) + ".10.2020")
    else:
        selection.append(str(i) + ".10.2020")


read = read_files("200325_Datengrundlage_Grafiken_COVID-19-Bericht.csv")
y0 = filtering(read, selection, 400)

generat_graph(y0, selection, exclude)


y = filtering(read, selection, 400)
#Makes my curve striagth
for i in y:
    y[y.index(i)] = np.log(i)

generat_graph(y, selection, exclude)












y = filtering(read, selection, 400)
for i in y:
    y[y.index(i)] = np.log(i)

for i in y:
    y[y.index(i)] = pow(np.e, i)

generat_graph(y, selection, exclude)



