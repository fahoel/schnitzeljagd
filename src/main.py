"""
Schnitzeljagd - Scavenger Hunt Mobile App

Main application entry point.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class MapScreen(MDScreen):
    """Screen displaying the interactive map of Hannover."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "map"
        # Placeholder - actual map implementation to be added
        self.add_widget(MDLabel(
            text="Map Screen\n(Map of Hannover will be displayed here)",
            halign="center",
            theme_text_color="Secondary"
        ))


class CameraScreen(MDScreen):
    """Screen for capturing photos during the scavenger hunt."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "camera"
        # Placeholder - actual camera implementation to be added
        self.add_widget(MDLabel(
            text="Camera Screen\n(Photo capture will be implemented here)",
            halign="center",
            theme_text_color="Secondary"
        ))


class GalleryScreen(MDScreen):
    """Screen showing uploaded photos."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "gallery"
        # Placeholder - actual gallery implementation to be added
        self.add_widget(MDLabel(
            text="Gallery Screen\n(Captured photos will be shown here)",
            halign="center",
            theme_text_color="Secondary"
        ))


class ProgressScreen(MDScreen):
    """Screen displaying scavenger hunt progress."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "progress"
        # Placeholder - actual progress implementation to be added
        self.add_widget(MDLabel(
            text="Progress Screen\n(Challenge progress will be displayed here)",
            halign="center",
            theme_text_color="Secondary"
        ))


class SchnitzeljagdApp(MDApp):
    """Main application class for Schnitzeljagd."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Schnitzeljagd"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
    
    def build(self):
        """Build and return the root widget."""
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(MapScreen())
        sm.add_widget(CameraScreen())
        sm.add_widget(GalleryScreen())
        sm.add_widget(ProgressScreen())
        
        # Set default screen
        sm.current = "map"
        
        return sm


def main():
    """Main entry point for the application."""
    app = SchnitzeljagdApp()
    app.run()


if __name__ == "__main__":
    main()
