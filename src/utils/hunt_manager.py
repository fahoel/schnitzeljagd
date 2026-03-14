"""
Hunt Manager

Manages scavenger hunt challenges, progress, and scoring.
"""

from typing import List, Dict, Optional


class HuntManager:
    """Manages scavenger hunt state and logic."""
    
    PROXIMITY_THRESHOLD = 50  # meters
    
    def __init__(self):
        """Initialize the hunt manager."""
        self.challenges = []
        self.completed_challenges = []
        self.current_score = 0
    
    def add_challenge(self, challenge_id: str, name: str, description: str,
                     latitude: float, longitude: float, points: int = 10):
        """
        Add a challenge to the hunt.
        
        Args:
            challenge_id: Unique challenge identifier
            name: Challenge name
            description: Challenge description
            latitude: Challenge location latitude
            longitude: Challenge location longitude
            points: Points awarded for completion
        """
        challenge = {
            "id": challenge_id,
            "name": name,
            "description": description,
            "latitude": latitude,
            "longitude": longitude,
            "points": points,
            "completed": False
        }
        self.challenges.append(challenge)
    
    def get_challenges(self) -> List[Dict]:
        """
        Get all challenges.
        
        Returns:
            List of challenge dictionaries
        """
        return self.challenges
    
    def get_incomplete_challenges(self) -> List[Dict]:
        """
        Get all incomplete challenges.
        
        Returns:
            List of incomplete challenge dictionaries
        """
        return [c for c in self.challenges if not c["completed"]]
    
    def check_proximity(self, challenge_id: str, user_latitude: float,
                       user_longitude: float) -> bool:
        """
        Check if user is close enough to a challenge location.
        
        Args:
            challenge_id: ID of the challenge to check
            user_latitude: User's current latitude
            user_longitude: User's current longitude
            
        Returns:
            True if user is within proximity threshold, False otherwise
        """
        challenge = self._get_challenge_by_id(challenge_id)
        if not challenge:
            return False
        
        # Simple distance calculation (should use proper geodesic)
        lat_diff = abs(user_latitude - challenge["latitude"])
        lon_diff = abs(user_longitude - challenge["longitude"])
        distance = ((lat_diff ** 2 + lon_diff ** 2) ** 0.5) * 111000  # meters
        
        return distance <= self.PROXIMITY_THRESHOLD
    
    def complete_challenge(self, challenge_id: str) -> bool:
        """
        Mark a challenge as completed and award points.
        
        Args:
            challenge_id: ID of the challenge to complete
            
        Returns:
            True if challenge was completed successfully, False otherwise
        """
        challenge = self._get_challenge_by_id(challenge_id)
        if not challenge or challenge["completed"]:
            return False
        
        challenge["completed"] = True
        self.completed_challenges.append(challenge_id)
        self.current_score += challenge["points"]
        
        print(f"Challenge completed: {challenge['name']} (+{challenge['points']} points)")
        return True
    
    def get_progress(self) -> Dict:
        """
        Get current hunt progress.
        
        Returns:
            Dictionary with progress information
        """
        total = len(self.challenges)
        completed = len(self.completed_challenges)
        
        return {
            "total_challenges": total,
            "completed_challenges": completed,
            "remaining_challenges": total - completed,
            "completion_percentage": (completed / total * 100) if total > 0 else 0,
            "current_score": self.current_score
        }
    
    def is_hunt_complete(self) -> bool:
        """
        Check if all challenges are completed.
        
        Returns:
            True if all challenges completed, False otherwise
        """
        return len(self.completed_challenges) == len(self.challenges)
    
    def _get_challenge_by_id(self, challenge_id: str) -> Optional[Dict]:
        """
        Get a challenge by its ID.
        
        Args:
            challenge_id: ID of the challenge
            
        Returns:
            Challenge dictionary or None if not found
        """
        for challenge in self.challenges:
            if challenge["id"] == challenge_id:
                return challenge
        return None
