import plotly.graph_objects as go
import numpy as np

x = []
y = []
for i in range(0,20):
    x.append(i)

for i in x:
    y.append(2**i)

fig = go.Figure(data=go.Scatter(y=y, x=x, connectgaps=True))
fig.show()
