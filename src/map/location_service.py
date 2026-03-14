"""
Location Service

Handles GPS and location-based services.
"""

from typing import Optional, Callable


class LocationService:
    """Service for accessing device GPS and location data."""
    
    def __init__(self):
        """Initialize the location service."""
        self.current_latitude = None
        self.current_longitude = None
        self.is_enabled = False
        self.callbacks = []
    
    def request_permissions(self) -> bool:
        """
        Request location permissions from the user.
        
        Returns:
            True if permissions granted, False otherwise
        """
        # Placeholder - actual implementation will use Plyer
        # TODO: Implement using plyer.gps
        print("Location permissions requested")
        return True
    
    def start_tracking(self):
        """Start tracking user location."""
        if not self.is_enabled:
            self.is_enabled = True
            # TODO: Implement using plyer.gps
            print("Location tracking started")
    
    def stop_tracking(self):
        """Stop tracking user location."""
        if self.is_enabled:
            self.is_enabled = False
            # TODO: Implement using plyer.gps
            print("Location tracking stopped")
    
    def get_current_location(self) -> Optional[tuple]:
        """
        Get the current location.
        
        Returns:
            Tuple of (latitude, longitude) or None if not available
        """
        if self.current_latitude is not None and self.current_longitude is not None:
            return (self.current_latitude, self.current_longitude)
        return None
    
    def on_location_update(self, callback: Callable):
        """
        Register a callback for location updates.
        
        Args:
            callback: Function to call when location updates
        """
        self.callbacks.append(callback)
    
    def _notify_location_update(self, latitude: float, longitude: float):
        """
        Notify all callbacks of a location update.
        
        Args:
            latitude: Updated latitude
            longitude: Updated longitude
        """
        self.current_latitude = latitude
        self.current_longitude = longitude
        
        for callback in self.callbacks:
            callback(latitude, longitude)
