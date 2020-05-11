from igc_reader import IGCdata
from igc_plotter import plot_flight

my_file = "96LX1021.igc"
my_flight = IGCdata(my_file)
plot_flight(my_flight.lons, my_flight.lats)
