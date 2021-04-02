import numpy as np
import pandas as pd
import plotly.graph_objects as go


def to_log(data):
    return np.log(data)


def to_expo(data):
    return np.power(np.e, data)


def curve_to_expo(a, b):
    n = np.power(np.e, a)
    k = b
    return n, k


def get_curve(data):
    x_mean = np.mean(data.index.to_list())
    y_mean = np.mean(data["Cases"].to_list())

    x_intermid = (data.index.to_list()) - x_mean
    y_intermid = data - y_mean

    x_squared = sum(x_intermid ** 2)
    x_y_comb = sum(x_intermid * y_intermid)

    b = x_y_comb / x_squared
    a = y_mean - x_mean * b

    return a, b


def plot(data):
    fig = go.Figure(data=go.Scatter(y=data["Cases"].to_list(), x=data.index.to_list(), connectgaps=True))
    fig.show()

# data_base = pd.Series([1, 1.5, 2.25, 3.375])
# data_log = to_log(data_base)
# a, b = get_curve(data_log)
# n, k = curve_to_expo(a, b)
# print(n, k)
