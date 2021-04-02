import numpy as np
import pandas as pd
import plotly.graph_objects as go


def to_log(data):
    return np.log(data)


def to_expo(data):
    return np.power(np.e, data)


def drop_unwanted(data, remove):
    return data.drop(remove)


def curve_to_expo(a, b):
    A = np.power(np.e, a)
    k = b
    return A, k


def get_curve(data):
    x_mean = np.mean(data.keys())
    y_mean = np.mean(data)

    x_intermid = (data.keys()) - x_mean
    y_intermid = data - y_mean

    x_suqared = sum(x_intermid ** 2)
    x_y_comb = sum(x_intermid * y_intermid)

    b = x_y_comb / x_suqared
    a = y_mean - x_mean * b

    return a, b


def plot(data):
    fig = go.Figure(data=go.Scatter(y=data.to_list(), x=data.keys(), connectgaps=True))
    fig.show()




# Testing data: (Base 2)
data_base = pd.Series([1, 1.5, 2.25, 3.375])

data_log = to_log(data_base)

a, b = get_curve(data_log)

A, k = curve_to_expo(a, b)

print(A, k)


