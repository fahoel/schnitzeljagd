"""
Map Manager

Handles map state, interactions, and location markers for the scavenger hunt.
"""

from typing import List, Tuple, Optional


class MapManager:
    """Manages map display and interactions for Hannover."""
    
    # Default location: Hannover, Germany
    DEFAULT_LATITUDE = 52.3759
    DEFAULT_LONGITUDE = 9.7320
    DEFAULT_ZOOM = 13
    
    def __init__(self):
        """Initialize the map manager."""
        self.latitude = self.DEFAULT_LATITUDE
        self.longitude = self.DEFAULT_LONGITUDE
        self.zoom = self.DEFAULT_ZOOM
        self.markers = []
        self.current_location = None
    
    def set_location(self, latitude: float, longitude: float):
        """
        Set the current map center location.
        
        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
        """
        self.latitude = latitude
        self.longitude = longitude
    
    def set_zoom(self, zoom: int):
        """
        Set the map zoom level.
        
        Args:
            zoom: Zoom level (typically 1-20)
        """
        self.zoom = zoom
    
    def add_marker(self, latitude: float, longitude: float, 
                   name: str, description: str = ""):
        """
        Add a marker to the map.
        
        Args:
            latitude: Marker latitude
            longitude: Marker longitude
            name: Marker name/title
            description: Optional marker description
        """
        marker = {
            "latitude": latitude,
            "longitude": longitude,
            "name": name,
            "description": description
        }
        self.markers.append(marker)
    
    def get_markers(self) -> List[dict]:
        """
        Get all markers on the map.
        
        Returns:
            List of marker dictionaries
        """
        return self.markers
    
    def update_current_location(self, latitude: float, longitude: float):
        """
        Update the user's current location.
        
        Args:
            latitude: Current latitude
            longitude: Current longitude
        """
        self.current_location = {
            "latitude": latitude,
            "longitude": longitude
        }
    
    def get_distance_to_marker(self, marker_index: int) -> Optional[float]:
        """
        Calculate distance from current location to a marker.
        
        Args:
            marker_index: Index of the marker in the markers list
            
        Returns:
            Distance in meters, or None if current location is not set
        """
        if self.current_location is None or marker_index >= len(self.markers):
            return None
        
        marker = self.markers[marker_index]
        
        # PLACEHOLDER: Simplified distance calculation
        # TODO: Replace with geopy.distance.geodesic() for accurate geodesic distances
        # Current implementation uses Euclidean approximation which is inaccurate
        # at higher latitudes (like Hannover at 52.3759°N)
        lat_diff = abs(self.current_location["latitude"] - marker["latitude"])
        lon_diff = abs(self.current_location["longitude"] - marker["longitude"])
        
        # Very rough approximation (1 degree ≈ 111km)
        distance = ((lat_diff ** 2 + lon_diff ** 2) ** 0.5) * 111000
        
        return distance
