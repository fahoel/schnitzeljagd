"""
API Client

Handles communication with backend API.
"""

from typing import Dict, Optional, List
from src.utils.logger import logger


class APIClient:
    """Client for communicating with the Schnitzeljagd backend API."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize the API client.
        
        Args:
            base_url: Base URL of the API
            api_key: Optional API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key
        self.auth_token = None
    
    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticate with the API.
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            True if authentication successful, False otherwise
        """
        # TODO: Implement using requests library
        logger.info(f"Authenticating user: {username}")
        self.auth_token = "dummy_token"  # Placeholder
        return True
    
    def get_hunts(self) -> List[Dict]:
        """
        Get available scavenger hunts.
        
        Returns:
            List of hunt dictionaries
        """
        # TODO: Implement using requests library
        logger.info("Fetching available hunts")
        return []  # Placeholder
    
    def get_hunt_details(self, hunt_id: str) -> Optional[Dict]:
        """
        Get details for a specific hunt.
        
        Args:
            hunt_id: ID of the hunt
            
        Returns:
            Hunt details dictionary or None if not found
        """
        # TODO: Implement using requests library
        logger.info(f"Fetching hunt details: {hunt_id}")
        return None  # Placeholder
    
    def upload_photo(self, photo_path: str, challenge_id: str,
                    latitude: Optional[float] = None,
                    longitude: Optional[float] = None) -> bool:
        """
        Upload a photo to the server.
        
        Args:
            photo_path: Path to the photo file
            challenge_id: Associated challenge ID
            latitude: Optional photo latitude
            longitude: Optional photo longitude
            
        Returns:
            True if upload successful, False otherwise
        """
        # TODO: Implement using requests library
        logger.info(f"Uploading photo: {photo_path} for challenge: {challenge_id}")
        return True  # Placeholder
    
    def sync_progress(self, completed_challenges: List[str], score: int) -> bool:
        """
        Synchronize progress with the server.
        
        Args:
            completed_challenges: List of completed challenge IDs
            score: Current score
            
        Returns:
            True if sync successful, False otherwise
        """
        # TODO: Implement using requests library
        logger.info(f"Syncing progress: {len(completed_challenges)} challenges, {score} points")
        return True  # Placeholder
    
    def get_leaderboard(self, hunt_id: str) -> List[Dict]:
        """
        Get leaderboard for a hunt.
        
        Args:
            hunt_id: ID of the hunt
            
        Returns:
            List of leaderboard entries
        """
        # TODO: Implement using requests library
        logger.info(f"Fetching leaderboard for hunt: {hunt_id}")
        return []  # Placeholder
