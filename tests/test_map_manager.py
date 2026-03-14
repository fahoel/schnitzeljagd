"""
Tests for MapManager
"""

import pytest
from src.map.manager import MapManager


def test_map_initialization():
    """Test that map initializes with default Hannover location."""
    manager = MapManager()
    assert manager.latitude == 52.3759
    assert manager.longitude == 9.7320
    assert manager.zoom == 13


def test_set_location():
    """Test setting map location."""
    manager = MapManager()
    manager.set_location(52.0, 9.0)
    assert manager.latitude == 52.0
    assert manager.longitude == 9.0


def test_add_marker():
    """Test adding markers to the map."""
    manager = MapManager()
    manager.add_marker(52.3759, 9.7320, "Test Marker", "Test Description")
    
    markers = manager.get_markers()
    assert len(markers) == 1
    assert markers[0]["name"] == "Test Marker"
    assert markers[0]["latitude"] == 52.3759


def test_update_current_location():
    """Test updating current location."""
    manager = MapManager()
    manager.update_current_location(52.0, 9.0)
    
    assert manager.current_location is not None
    assert manager.current_location["latitude"] == 52.0
    assert manager.current_location["longitude"] == 9.0


def test_distance_calculation():
    """Test distance calculation to markers."""
    manager = MapManager()
    manager.add_marker(52.3759, 9.7320, "Marker")
    manager.update_current_location(52.3759, 9.7320)
    
    distance = manager.get_distance_to_marker(0)
    assert distance is not None
    assert distance < 100  # Should be very close (near 0)
