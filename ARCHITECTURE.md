# Architecture Documentation

## Overview

The Schnitzeljagd app is a cross-platform mobile application built with Python and Kivy. It follows a modular architecture with clear separation of concerns.

## Architecture Diagram

```
┌─────────────────────────────────────────┐
│         User Interface Layer            │
│  (Kivy/KivyMD UI Components)           │
└──────────────┬──────────────────────────┘
               │
┌──────────────┴──────────────────────────┐
│      Application Logic Layer            │
│  ┌──────────┐  ┌──────────┐  ┌────────┐│
│  │   Map    │  │  Camera  │  │  Hunt  ││
│  │ Manager  │  │ Manager  │  │Manager ││
│  └──────────┘  └──────────┘  └────────┘│
└──────────────┬──────────────────────────┘
               │
┌──────────────┴──────────────────────────┐
│       Data & Services Layer             │
│  ┌──────────┐  ┌──────────┐  ┌────────┐│
│  │Location  │  │  Photo   │  │ API    ││
│  │ Service  │  │ Storage  │  │Service ││
│  └──────────┘  └──────────┘  └────────┘│
└─────────────────────────────────────────┘
```

## Core Components

### 1. User Interface Layer

**Technology**: Kivy/KivyMD

The UI layer handles all user interactions and visual components:

- **MapScreen**: Displays the interactive map of Hannover
- **CameraScreen**: Camera interface for photo capture
- **HuntScreen**: Scavenger hunt challenges and progress
- **GalleryScreen**: View uploaded photos
- **SettingsScreen**: App configuration

### 2. Application Logic Layer

#### Map Manager (`src/map/manager.py`)
- Manages map state and interactions
- Handles location markers and waypoints
- Processes location updates
- Calculates distances between locations

#### Camera Manager (`src/camera/manager.py`)
- Controls camera access via Plyer
- Processes captured photos
- Manages photo metadata (location, timestamp)
- Handles photo upload queue

#### Hunt Manager (`src/utils/hunt_manager.py`)
- Manages scavenger hunt state
- Tracks challenge progress
- Validates location-based completions
- Calculates scores and achievements

### 3. Data & Services Layer

#### Location Service (`src/map/location_service.py`)
- GPS access via Plyer
- Location permission handling
- Real-time location updates
- Geocoding and reverse geocoding

#### Photo Storage (`src/camera/photo_storage.py`)
- Local photo storage
- Photo compression and optimization
- Upload queue management
- Sync with backend API

#### API Service (`src/utils/api_client.py`)
- RESTful API communication
- Authentication and authorization
- Data synchronization
- Error handling and retry logic

## Data Flow

### Photo Upload Flow

```
1. User captures photo → Camera Manager
2. Photo saved locally → Photo Storage
3. Add to upload queue → Photo Storage
4. Upload to server → API Service
5. Update UI status → Camera Manager → UI
```

### Location Verification Flow

```
1. Location update → Location Service
2. Check proximity → Hunt Manager
3. Validate challenge → Hunt Manager
4. Update progress → UI
5. Sync to server → API Service
```

## Design Patterns

### 1. Observer Pattern
- Used for location updates and hunt state changes
- Components subscribe to events and react accordingly

### 2. Singleton Pattern
- Applied to managers and services to ensure single instances
- Prevents duplicate GPS listeners or API clients

### 3. Strategy Pattern
- Different map providers can be swapped
- Multiple photo upload strategies (WiFi-only, immediate, etc.)

## Technologies and Libraries

### Core Framework
- **Kivy 2.3.0**: Cross-platform UI framework
- **KivyMD 1.2.0**: Material Design components for Kivy

### Mapping and Location
- **Folium 0.15.1**: Interactive map generation
- **Geopy 2.4.1**: Geocoding and distance calculations
- **Plyer 2.1.0**: Access to device GPS

### Image Processing
- **Pillow 10.2.0**: Image manipulation and optimization

### Networking
- **Requests 2.31.0**: HTTP client for API communication

## Mobile Platform Considerations

### Android
- Uses Buildozer for packaging
- Requires GPS and Camera permissions in AndroidManifest.xml
- Handles background location updates via Android services

### iOS (Future Support)
- Will use Kivy iOS toolchain
- Requires Info.plist configuration for permissions
- Background location updates via iOS capabilities

## Performance Optimization

### Map Rendering
- Lazy loading of map tiles
- Caching of previously viewed areas
- Progressive detail loading based on zoom level

### Photo Management
- Automatic image compression before upload
- Thumbnail generation for gallery view
- Background upload with queue management

### Battery Optimization
- Adjustable GPS update frequency
- Location updates only when app is active
- Smart caching to reduce network calls

## Security Considerations

### Data Protection
- API keys stored securely in environment variables
- User photos encrypted on device
- HTTPS for all API communication

### Permissions
- Request permissions only when needed
- Clear explanation of why permissions are required
- Graceful degradation if permissions denied

## Scalability

### Horizontal Scaling
- API backend can scale independently
- Photo storage can use CDN
- Database can be sharded by geographic region

### Offline Support
- Local caching of hunt data
- Queue-based photo uploads
- Sync when connectivity restored

## Testing Strategy

### Unit Tests
- Individual component logic
- Mock external dependencies (GPS, Camera, API)

### Integration Tests
- Component interactions
- End-to-end user flows

### UI Tests
- Screen navigation
- Touch interactions
- Visual regression testing

## Future Enhancements

1. **Multiplayer Mode**: Real-time competition between users
2. **AR Features**: Augmented reality for finding hidden locations
3. **Social Sharing**: Share progress on social media
4. **Custom Hunts**: Users can create their own scavenger hunts
5. **Achievements System**: Badges and rewards for completions

## Deployment

### Development
- Local testing on desktop (Linux/Windows/macOS)
- USB debugging on Android devices

### Production
- APK distribution via Google Play Store
- TestFlight for iOS beta testing
- Continuous integration with GitHub Actions

## Monitoring and Analytics

- Crash reporting integration
- User analytics for feature usage
- Performance monitoring
- Server-side logging for API calls
