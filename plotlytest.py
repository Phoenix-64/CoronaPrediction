import plotly.graph_objects as go
import numpy as np

z = np.arange(50)
fig = go.Figure(data=go.Scatter(x=z, y=1.2**z))
fig.show()
