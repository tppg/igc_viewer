from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def plot_flight(lons, lats):
    """plot the igc data to a map"""
    data = [Scattergeo(lon=lons, lat=lats)]
    my_layout = Layout(title='IGC flight data')

    fig = {'data': data, 'layout':my_layout}
    offline.plot(fig, filename='IGC_flight_data.html')
