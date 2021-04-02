import plotly.graph_objects as go
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0.1, 0.8, 2.3, 3.2, 3.9, 5.1, 6, 6.8, 7.6, 8.2, 9]



x_mean = np.mean(x)
y_mean = np.mean(y)
a_top = []
for i in range(len(x)):
    a_top.append((x[i] - x_mean) * (y[i] - y_mean))

a_bottom = []
for i in range(len(x)):
    a_bottom.append((x[i] - x_mean) ** 2)

a1 = sum(a_top) / sum(a_bottom)
a0 = y_mean - a1 * x_mean

y1 = []
for i in x:
    y1.append(a1*i+a0)

fig = go.Figure()
fig.add_trace(go.Scatter(y=y, x=x, connectgaps=True))
fig.add_trace(go.Scatter(x=x, y=y1))
fig.show()

