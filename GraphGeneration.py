import csv
import plotly.graph_objects as go
import numpy as np
import pandas as pd

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

def generat_graph(y_data, sel):
    fig = go.Figure(data=go.Scatter(y=y_data, x=sel, connectgaps=True))
    fig.show()





selection = []

exclude = ["03.10.2020", "04.10.2020", "10.10.2020", "11.10.2020", "17.10.2020", "18.10.2020", "04.10.2020",
           "24.10.2020", "25.10.2020"]

# Generating Dates I want:
for i in range(1, 27):
    if i < 10:
        selection.append("0" + str(i) + ".10.2020")
    else:
        selection.append(str(i) + ".10.2020")
df_x = pd.Series(selection)

read = read_files("200325_Datengrundlage_Grafiken_COVID-19-Bericht.csv")
y = filtering(read, selection, 400)

df_y = pd.Series(y)
remove = []
#generat_graph(y0, selection, exclude)
for i in exclude:
    if i in selection:
        print(i)
        remove.append(selection.index(i))

df_y = df_y.drop(remove)
df_x = df_x.drop(remove)


#Makes my curve striagth
df_y_log = np.log(df_y)


x_mean = len(df_y) / 2
y_mean = np.mean(df_y_log)
a_top = []
a_bottom = []
for index, value in df_y_log.items():
    a_top.append((index - x_mean) * (value - y_mean))
    a_bottom.append((index - x_mean) ** 2)


a1 = sum(a_top) / sum(a_bottom)
a0 = y_mean - a1 * x_mean

y1 = []
x1 = []
for i in range(len(df_y_log)):
    y1.append(a1*i+a0)
    x1.append(i)

print(y1)
y_normal = []
for i in y1:
    y_normal.append(np.e**i)


fig = go.Figure()
fig.add_trace(go.Scatter(y=df_y, x=df_x))
fig.add_trace(go.Scatter(y=y1, x=x1))
fig.add_trace(go.Scatter(y=y_normal, x=x1))
fig.show()



#generat_graph(y1, x1)



