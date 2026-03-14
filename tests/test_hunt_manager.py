"""
Tests for HuntManager
"""

import pytest
from src.utils.hunt_manager import HuntManager


def test_hunt_manager_initialization():
    """Test hunt manager initializes correctly."""
    manager = HuntManager()
    assert manager.current_score == 0
    assert len(manager.challenges) == 0


def test_add_challenge():
    """Test adding a challenge."""
    manager = HuntManager()
    manager.add_challenge("ch1", "Test Challenge", "Description", 52.0, 9.0, 10)
    
    challenges = manager.get_challenges()
    assert len(challenges) == 1
    assert challenges[0]["name"] == "Test Challenge"
    assert challenges[0]["points"] == 10


def test_complete_challenge():
    """Test completing a challenge."""
    manager = HuntManager()
    manager.add_challenge("ch1", "Test Challenge", "Description", 52.0, 9.0, 10)
    
    result = manager.complete_challenge("ch1")
    assert result is True
    assert manager.current_score == 10
    assert "ch1" in manager.completed_challenges


def test_get_progress():
    """Test getting hunt progress."""
    manager = HuntManager()
    manager.add_challenge("ch1", "Challenge 1", "Desc", 52.0, 9.0, 10)
    manager.add_challenge("ch2", "Challenge 2", "Desc", 52.1, 9.1, 10)
    
    manager.complete_challenge("ch1")
    
    progress = manager.get_progress()
    assert progress["total_challenges"] == 2
    assert progress["completed_challenges"] == 1
    assert progress["remaining_challenges"] == 1
    assert progress["completion_percentage"] == 50.0


def test_hunt_completion():
    """Test checking if hunt is complete."""
    manager = HuntManager()
    manager.add_challenge("ch1", "Challenge 1", "Desc", 52.0, 9.0, 10)
    
    assert manager.is_hunt_complete() is False
    
    manager.complete_challenge("ch1")
    assert manager.is_hunt_complete() is True
