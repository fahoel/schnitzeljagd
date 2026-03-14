"""
Configuration Module

Manages application configuration and environment variables.
"""

import os
from typing import Optional


class Config:
    """Application configuration."""
    
    # API Configuration
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.schnitzeljagd.example.com")
    API_KEY = os.getenv("API_KEY", "")
    
    # Map Configuration - Hannover, Germany
    DEFAULT_LATITUDE = float(os.getenv("DEFAULT_LATITUDE", "52.3759"))
    DEFAULT_LONGITUDE = float(os.getenv("DEFAULT_LONGITUDE", "9.7320"))
    DEFAULT_ZOOM = int(os.getenv("DEFAULT_ZOOM", "13"))
    
    # Photo Storage
    PHOTO_STORAGE_DIR = os.getenv("PHOTO_STORAGE_DIR", "photos")
    PHOTO_QUALITY = int(os.getenv("PHOTO_QUALITY", "85"))
    THUMBNAIL_SIZE = (200, 200)
    
    # Location Settings
    PROXIMITY_THRESHOLD = int(os.getenv("PROXIMITY_THRESHOLD", "50"))  # meters
    GPS_UPDATE_INTERVAL = int(os.getenv("GPS_UPDATE_INTERVAL", "5"))  # seconds
    
    # App Settings
    APP_NAME = "Schnitzeljagd"
    APP_VERSION = "0.1.0"
    
    @classmethod
    def load_from_env_file(cls, env_file: str = ".env"):
        """
        Load configuration from .env file.
        
        Args:
            env_file: Path to the .env file
        """
        if os.path.exists(env_file):
            try:
                from dotenv import load_dotenv
                load_dotenv(env_file)
                print(f"Configuration loaded from {env_file}")
            except ImportError:
                print("python-dotenv not installed, skipping .env file")
        else:
            print(f"No {env_file} file found, using defaults")
    
    @classmethod
    def get_info(cls) -> dict:
        """
        Get configuration information.
        
        Returns:
            Dictionary with configuration values
        """
        return {
            "app_name": cls.APP_NAME,
            "app_version": cls.APP_VERSION,
            "api_base_url": cls.API_BASE_URL,
            "default_location": (cls.DEFAULT_LATITUDE, cls.DEFAULT_LONGITUDE),
            "default_zoom": cls.DEFAULT_ZOOM,
            "proximity_threshold": cls.PROXIMITY_THRESHOLD
        }
