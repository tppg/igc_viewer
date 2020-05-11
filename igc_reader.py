class IGCdata:
    """class to model data from an instance of an igc file"""

    def __init__(self, filename):
        """initialize the attributes of the file"""
        self.times = []
        self.lons = []
        self.lats = []
        self.press_alts = []
        self.gps_alts = []
        self.filename = filename

        self._read_file()


    def _read_file(self):
        """read the igc file"""
        with open(self.filename) as file_object:
            lines = file_object.readlines()
        # extract the data
        for line in lines:
            if line.startswith("B"):
                self._extract_track_data(line)
            else:
                continue

    def _extract_track_data(self, line):
        """extract time, longitute, Latitude and altitudes from track point"""
        # get time stamps
        self.times.append(line[1:7])
        # get longitude
        current_lon = self._get_longitude(line)
        self.lons.append(current_lon)
        # get the Latitude
        current_lat = self._get_latitude(line)
        self.lats.append(current_lat)
        # get the pressure altitude
        self.press_alts.append(line[25:30])
        # get the gps altitude
        self.gps_alts.append(line[30:35])


    def _get_latitude(self, line):
        """return the Latitude in the correct format for plot"""
        # get the latitude string from the igc (DDM format)
        lat_DDM = line[7:15]
        # strip out the degrees
        degrees = float(lat_DDM[0:2])
        # strip out the minutes and add decimal point in to make decimal mins
        decimal_minutes = float(lat_DDM[2:7]) / 1000
        # convert the minutes to a decimal of a degree
        decimal_degrees = decimal_minutes / 60
        # add degrees to decimal degrees to get latitude in DD format
        lat_DD = round(degrees + decimal_degrees, 6)
        # work out + or - i.e. north or south
        if lat_DDM[-1] == "S":
            lat_DD *= -1
            return lat_DD
        else:
            return lat_DD

    def _get_longitude(self, line):
        """return the longitude in the correct format for plot"""
        # get the longitude string from the igc (DDM format)
        lon_DDM = line[15:24]
        # strip out the degrees
        degrees = float(lon_DDM[0:3])
        # strip out the minutes and add decimal point in to make decimal mins
        decimal_minutes = float(lon_DDM[3:8]) / 1000
        # convert the minutes to a decimal of a degree
        decimal_degrees = decimal_minutes / 60
        # add degrees to decimal degrees to get longitude in DD format
        lon_DD = round(degrees + decimal_degrees, 6)
        # work out + or - i.e. east or west
        if lon_DDM[-1] == "W":
            lon_DD *= -1
            return lon_DD
        else:
            return lon_DD
