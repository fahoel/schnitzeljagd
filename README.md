# Schnitzeljagd - Scavenger Hunt Mobile App

A mobile scavenger hunt application for exploring Hannover, Germany. This app allows users to participate in location-based scavenger hunts with photo upload capabilities.

## Features

- 🗺️ **Interactive Map**: Explore Hannover with an integrated map showing scavenger hunt locations
- 📸 **Photo Upload**: Capture and upload photos during your scavenger hunt adventure
- 📍 **Location Tracking**: GPS-based location verification for scavenger hunt checkpoints
- 🎯 **Challenge System**: Complete challenges at various locations throughout Hannover

## Technology Stack

- **Python 3.8+**: Core programming language
- **Kivy/KivyMD**: Cross-platform mobile UI framework
- **Folium**: Interactive map visualization
- **Plyer**: Access to native device features (camera, GPS)
- **Pillow**: Image processing and handling

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Android SDK (for Android builds)
- Xcode (for iOS builds, macOS only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fahoel/schnitzeljagd.git
cd schnitzeljagd
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

### Development Mode (Desktop)

Run the app in development mode on your desktop:

```bash
python src/main.py
```

### Building for Mobile

#### Android

1. Install Buildozer:
```bash
pip install buildozer
```

2. Initialize and build:
```bash
buildozer init
buildozer -v android debug
```

#### iOS (macOS only)

Follow the Kivy iOS toolchain documentation for building iOS applications.

## Project Structure

```
schnitzeljagd/
├── src/                    # Source code
│   ├── main.py            # Application entry point
│   ├── ui/                # User interface components
│   ├── map/               # Map integration and location services
│   ├── camera/            # Photo capture and upload functionality
│   └── utils/             # Utility functions and helpers
├── assets/                # Images, icons, and other static files
├── tests/                 # Test suite
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
├── buildozer.spec         # Mobile build configuration
└── README.md             # This file
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
# API Configuration
API_BASE_URL=https://your-api-server.com
API_KEY=your-api-key

# Map Configuration
DEFAULT_LATITUDE=52.3759
DEFAULT_LONGITUDE=9.7320
DEFAULT_ZOOM=13
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
```

### Linting

```bash
flake8 src/
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Next Steps

See [NEXT_STEPS.md](NEXT_STEPS.md) for a detailed roadmap of features to implement and improvements to make.

## Architecture

For detailed information about the application architecture, see [ARCHITECTURE.md](ARCHITECTURE.md).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Kivy framework for cross-platform mobile development
- Map data provided by OpenStreetMap
- Designed for exploring the beautiful city of Hannover, Germany

## Support

For issues, questions, or contributions, please open an issue on GitHub.