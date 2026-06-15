# GestVoice: Intent-Aware HCI using Gesture & Voice Integration

Welcome to the **GestVoice** (also referred to as **AETHER_CORE**) project. This is a state-of-the-art Human-Computer Interaction (HCI) system that integrates computer vision hand tracking, text-to-speech, local voice recognition, and generative AI (multimodal Gemini) to control system-level actions and run a web dashboard.

---

## 📁 Directory & File Map

Here is the complete layout of the project, detailing the role of each directory and file:

```yaml
📦 Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main
 ┣ 📂 intent_os                         # Django Backend Project
 ┃ ┣ 📂 dashboard                       # Django Application for the control panel
 ┃ ┃ ┣ 📄 admin.py                      # Django admin settings
 ┃ ┃ ┣ 📄 apps.py                       # App configuration
 ┃ ┃ ┣ 📄 forms.py                      # Custom signup and profile forms
 ┃ ┃ ┣ 📄 models.py                     # Schema declarations
 ┃ ┃ ┣ 📄 views.py                      # Route logic and MongoDB database initialization/seeding
 ┃ ┃ ┗ 📄 tests.py                      # Django app tests
 ┃ ┣ 📂 intent_os                       # Django Project Configuration
 ┃ ┃ ┣ 📄 asgi.py                       # ASGI entrypoint
 ┃ ┃ ┣ 📄 settings.py                   # Django app configurations (MongoDB, SQLite, auth)
 ┃ ┃ ┣ 📄 urls.py                       # Global url routing rules
 ┃ ┃ ┗ 📄 wsgi.py                       # WSGI entrypoint
 ┃ ┣ 📂 static                          # Static assets for Dashboard UI
 ┃ ┃ ┣ 📂 css
 ┃ ┃ ┃ ┗ 📄 styles.css                  # Custom styling for dashboard panels, buttons, grids
 ┃ ┃ ┗ 📂 js
 ┃ ┃   ┗ 📄 app.js                      # Core JS logic for AJAX logs, status checks, updates
 ┃ ┣ 📂 templates                       # HTML Templates
 ┃ ┃ ┣ 📂 registration                  # Auth templates
 ┃ ┃ ┃ ┣ 📄 login.html                  # Dashboard login view
 ┃ ┃ ┃ ┗ 📄 signup.html                 # Dashboard registration view
 ┃ ┃ ┣ 📄 base.html                     # Shared skeleton layout
 ┃ ┃ ┣ 📄 cursor_control.html           # Virtual mouse control panel
 ┃ ┃ ┣ 📄 dashboard.html                # Main systems overview and live monitor
 ┃ ┃ ┣ 📄 gesture_settings.html         # Custom action mapping for hand gestures
 ┃ ┃ ┣ 📄 help_guide.html               # User documentation & instructions
 ┃ ┃ ┣ 📄 live_nodes.html               # Real-time state / camera node monitor
 ┃ ┃ ┣ 📄 system_controls.html          # Core system power & diagnostic buttons
 ┃ ┃ ┣ 📄 vault.html                    # Password & private credential safe
 ┃ ┃ ┗ 📄 voice_settings.html           # Voice command mapping list
 ┃ ┣ 📄 db.py                           # MongoDB client connection configuration
 ┃ ┣ 📄 db.sqlite3                      # SQLite database for Django Django Session/Auth tables
 ┃ ┗ 📄 manage.py                       # Django CLI management script
 ┣ 📂 build                             # Temporary build artifacts from PyInstaller
 ┣ 📄 .gitignore                        # Git ignore patterns
 ┣ 📄 build_exe.py                      # Automates building GestVoice into a standalone EXE
 ┣ 📄 cursor_control.py                 # Virtual Mouse system using hand pinch-gestures
 ┣ 📄 error.log.txt                     # Execution log file
 ┣ 📄 GestVoice.spec                    # PyInstaller bundling spec
 ┣ 📄 launcher.py                       # unified orchestration launcher (Django + Browser + OpenCV main loop)
 ┣ 📄 new.py                            # Main system engine (Camera Capture, AI Gestures, Voice Assistant)
 ┣ 📄 setup_mongo.py                    # Downloads, installs and launches local MongoDB server
 ┣ 📄 Start_GestVoice.bat               # Single-click Windows execution batch script
 ┣ 📄 system_logger.py                  # Logger class to push system events into MongoDB
 ┗ 📄 test_cam.py                       # Utility script to diagnose available camera indices
```

---

## 🛠️ Core Components & Architecture

### 1. Unified Launcher & Orchestrator
* **[launcher.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/launcher.py)**: Acts as the unified entry point. It spawns the Django server on a background thread, launches your default web browser pointing to the dashboard (`http://127.0.0.1:8000/`), and triggers the core AI gesture and voice engine on the main thread (essential for OpenCV frame window rendering).
* **[Start_GestVoice.bat](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/Start_GestVoice.bat)**: A Windows Batch script that automates starting MongoDB via `setup_mongo.py` followed by running `launcher.py`.

### 2. Main System AI Engine
* **[new.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/new.py)**: The heartbeat of the gesture and voice system.
  * **Computer Vision**: Utilizes MediaPipe Hands and OpenCV for hand gesture tracking, landmark extraction, and visual feedback drawing.
  * **System Activation**: Features state tracking (Passive, Activating, Active) with stability and drop tolerance timers to prevent false-triggering.
  * **Text-To-Speech**: Integrates `pyttsx3` for fast, offline speech synthesis feedback.
  * **Speech Recognition**: Configured with optimized silence thresholds for capturing voice commands.
  * **AI Voice Intent Classifier**: Implements a machine learning pipeline using `scikit-learn` (TF-IDF Vectorizer + Naive Bayes Classifier) trained on 40+ command variations.
  * **Multimodal Generative AI**: Connects to the Gemini API (`gemini-1.5-flash`). Features a **Do Anything Mode** that dynamically generates Python execution scripts (using PyAutoGUI/subprocess) to execute advanced complex user instructions. It also features a **Vision Mode** that takes desktop screenshots and sends them to Gemini to determine `[X, Y]` coordinates to click on UI components.
  * **Face Verification/Registration**: Connects with `face_recognition` to register and verify user identities.

### 3. System-Level Virtual Mouse
* **[cursor_control.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/cursor_control.py)**: Driven by hand tracking.
  * **Cursor Tracking**: Maps the index fingertip (landmark 8) coordinate space smoothly to screen resolution.
  * **Click / Pinch Gestures**: Triggers Left Click/Drag (Thumb + Index pinch) and Right Click (Thumb + Middle pinch) using Euclidean distance thresholds.
  * **Smoothing & Dead Zones**: Applies exponential moving average smoothing and a pixel dead-zone to eliminate micro-jitter and enhance precision.
  * **Gestural Deactivation**: Exits virtual mouse tracking when the "Peace Sign" gesture is detected.

### 4. Storage & Diagnostics
* **[setup_mongo.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/setup_mongo.py)**: Downloads standard MongoDB zip for Windows, extracts it to the local workspace, and runs it on port `27017` in the background.
* **[system_logger.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/system_logger.py)**: Establishes a database logger that writes event categories, input prompts, status codes, and execution timestamps into MongoDB.
* **[test_cam.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/test_cam.py)**: Loops through camera APIs (`CAP_ANY`, `CAP_DSHOW`, `CAP_MSMF`) across indices `0-4` to troubleshoot video source capture issues.

### 5. Control Panel & Dashboard Backend
* **[intent_os](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/intent_os)**: Django web backend.
  * **Seed Database**: [views.py](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/intent_os/dashboard/views.py) seeds standard list mapping for static commands and gestures to MongoDB.
  * **REST APIs**: Provides endpoints to update custom actions mapped to gestures/voice triggers, monitor live status of subsystems, query execution logs, and retrieve system status.
  * **Front-end UI**: Templates are designed with styling from [styles.css](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/intent_os/static/css/styles.css) and script operations in [app.js](file:///c:/Users/Junaid%20Khan/Downloads/Intent-Aware-HCL-using-Gesture-and-Voice-Integration-main/intent_os/static/js/app.js) to display status, security vault entries, settings modification sliders, and help cards.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed. Install the necessary dependencies:

```bash
pip install opencv-python mediapipe pyttsx3 speechrecognition pyautogui scikit-learn numpy google-generativeai fuzzywuzzy pygetwindow face-recognition pillow django pymongo
```

*Note: The `face_recognition` library requires `dlib`, which might need C++ build tools installed on Windows.*

### Running the Project

1. Run the unified batch script:
   ```cmd
   Start_GestVoice.bat
   ```
2. The launcher will:
   * Start the local MongoDB database.
   * Initialize the Django dashboard backend.
   * Open the login panel at `http://127.0.0.1:8000/` in your browser.
   * Open your camera feed and begin tracking hand activation gestures.

### Creating the Standalone Executable
To bundle the project into a single `.exe` file:
```bash
python build_exe.py
```
This script will produce `dist/GestVoice.exe` which contains all the required libraries (OpenCV, MediaPipe, Scikit-learn, etc.).
