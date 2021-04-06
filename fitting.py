import numpy as np
from datetime import date
import pandas as pd
import plotly.graph_objects as go

"""
Straightens curve by taking the ln of the y axis.
"""


def to_log(data):
    data["logCases"] = np.log(data["Cases"])
    return data


"""
Stretches y axis back out exponentially.
"""


def to_expo(data):
    data["Cases"] = np.power(np.e, data["Cases"])
    return data


"""
Converts line formula to exponential form n1 = n * e^kx
"""


def line_to_expo(a, b):
    n = np.power(np.e, a)
    k = b
    return n, k


"""
Fits curve to linear dataset:
"""


def get_curve(data):
    x_mean = np.mean(data["time"].to_list())
    y_mean = np.mean(data["logCases"].to_list())

    x_intermid = (data["time"].to_list()) - x_mean
    y_intermid = data["logCases"] - y_mean

    x_squared = sum(x_intermid ** 2)
    x_y_comb = sum(x_intermid * y_intermid)

    b = x_y_comb / x_squared
    a = y_mean - x_mean * b

    return a, b


"""
Computes days between input and last entry to data
"""


def compute_delta(data, input_date):
    prediction_date = str_to_date(input_date)
    orig_date = str_to_date(data["Dates"].iloc[-1:].to_list()[0])
    delta = prediction_date - orig_date
    return delta.days


"""
Generates curve that fits to the dataset.
"""


def generate_curve(data, n, k, input_date):
    delta = compute_delta(data, input_date)

    time_range = np.arange(data["time"].iloc[-1:].to_list()[0] + 1, data["time"].iloc[-1:].to_list()[0] + delta)
    rang = pd.DataFrame(time_range.tolist(), columns=["time"])
    data = data.append(rang, ignore_index=True)
    data["Interpolated"] = n * (np.e ** (k * data["time"]))

    return data


"""
Computes the cases at input_date and if possible gets the true cases fro comparison
"""


def get_prediction(data, read, input_date):
    true_cases = []
    delta = compute_delta(data, input_date)
    data = to_log(data)
    a, b = get_curve(data)
    n, k = line_to_expo(a, b)

    cases = data["Cases"].iloc[-1:].to_list()[0] * (np.e ** (k * delta))

    for i in read:
        if input_date in i[0]:
            print(i[0], "Yes")
            true_cases = i[0].split(";")[1]

    return cases, true_cases, delta


"""
Converts a date from form(20.01.2020) to a datetime.date object
"""


def str_to_date(string):
    sepperate = string.split(".")
    date_obj = date(int(sepperate[2]), int(sepperate[1]), int(sepperate[0]))
    return date_obj


"""
Plots column in data against time
"""


def plot(data):
    fig = go.Figure()
    for column in data.columns[2:]:
        fig.add_trace(go.Scatter(y=data[column].to_list(), x=data["time"].to_list(), connectgaps=True))
    fig.show()
