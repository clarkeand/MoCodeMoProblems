class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_elevation = 0
        highest_altitude = 0
        for elevation in gain:
            current_elevation += elevation
            if current_elevation > highest_altitude: 
                highest_altitude = current_elevation
        return highest_altitude
