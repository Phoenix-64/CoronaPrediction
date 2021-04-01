import csv
import plotly.graph_objects as go


# Opening and reading .csv file:
def read_files(filepath):
    with open(filepath, newline="") as csvfile:
        data = list(csv.reader(csvfile))
    return data


def filtering(data, dates, file_range):
    date_ranged = []
    current = []
    # Throwing everything away that is outside the relavant range must be adjusted to accomodated further datea:
    for i in range(7, file_range):
        date_ranged.append(data[i])

    # FInding my selection and extracting data for said dates
    for i in date_ranged:
        seperated = i[0].split(";")
        for x in dates:
            if seperated[0] == x:
                current.append(seperated[1])
        date_ranged[date_ranged.index(i)] = seperated

    return current


# Generating Dates I want:
selection = []
for i in range(1, 31):
    if i < 10:
        selection.append("0" + str(i) + ".10.2020")
    else:
        selection.append(str(i) + ".10.2020")

# reading csv file and returing raw data:
read = read_files("200325_Datengrundlage_Grafiken_COVID-19-Bericht.csv")
# Filtering raw data and extracting daily cases
y = filtering(read, selection, 400)

# Graphing
fig = go.Figure(data=go.Scatter(y=y, x=selection))
fig.show()
