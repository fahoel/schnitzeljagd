"""
Photo Storage

Manages local storage and uploading of photos.
"""

import os
from typing import List, Optional, Dict
from datetime import datetime


class PhotoStorage:
    """Handles photo storage, metadata, and upload queue."""
    
    def __init__(self, storage_dir: str = "photos"):
        """
        Initialize photo storage.
        
        Args:
            storage_dir: Directory to store photos
        """
        self.storage_dir = storage_dir
        self.upload_queue = []
        self.photos = []
        
        # Create storage directory if it doesn't exist
        os.makedirs(storage_dir, exist_ok=True)
    
    def save_photo(self, photo_path: str, latitude: Optional[float] = None,
                   longitude: Optional[float] = None, 
                   challenge_id: Optional[str] = None) -> Dict:
        """
        Save a photo with metadata.
        
        Args:
            photo_path: Path to the photo file
            latitude: Optional latitude where photo was taken
            longitude: Optional longitude where photo was taken
            challenge_id: Optional ID of associated challenge
            
        Returns:
            Dictionary with photo metadata
        """
        timestamp = datetime.now().isoformat()
        
        photo_metadata = {
            "path": photo_path,
            "timestamp": timestamp,
            "latitude": latitude,
            "longitude": longitude,
            "challenge_id": challenge_id,
            "uploaded": False
        }
        
        self.photos.append(photo_metadata)
        self.upload_queue.append(photo_metadata)
        
        print(f"Photo saved: {photo_path}")
        return photo_metadata
    
    def get_all_photos(self) -> List[Dict]:
        """
        Get all stored photos.
        
        Returns:
            List of photo metadata dictionaries
        """
        return self.photos
    
    def get_upload_queue(self) -> List[Dict]:
        """
        Get photos pending upload.
        
        Returns:
            List of photo metadata dictionaries pending upload
        """
        return [p for p in self.upload_queue if not p["uploaded"]]
    
    def mark_as_uploaded(self, photo_path: str):
        """
        Mark a photo as successfully uploaded.
        
        Args:
            photo_path: Path to the uploaded photo
        """
        for photo in self.photos:
            if photo["path"] == photo_path:
                photo["uploaded"] = True
                print(f"Photo marked as uploaded: {photo_path}")
                break
    
    def compress_photo(self, photo_path: str, quality: int = 85) -> str:
        """
        Compress a photo for upload.
        
        Args:
            photo_path: Path to the photo to compress
            quality: JPEG quality (1-100)
            
        Returns:
            Path to the compressed photo
        """
        # TODO: Implement using Pillow
        print(f"Compressing photo: {photo_path} (quality: {quality})")
        return photo_path  # Placeholder
    
    def generate_thumbnail(self, photo_path: str, size: tuple = (200, 200)) -> str:
        """
        Generate a thumbnail for a photo.
        
        Args:
            photo_path: Path to the photo
            size: Thumbnail size as (width, height)
            
        Returns:
            Path to the thumbnail
        """
        # TODO: Implement using Pillow
        thumbnail_path = photo_path.replace(".jpg", "_thumb.jpg")
        print(f"Generating thumbnail: {thumbnail_path}")
        return thumbnail_path
