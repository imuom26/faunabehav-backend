FaunaBehav Backend

AI-powered wildlife behaviour monitoring and intelligent deterrence backend system for smart farming environments.

Overview

FaunaBehav is a Final Year Project focused on detecting wildlife activity and analysing animal behaviour to support intelligent deterrence systems in agricultural environments.

The backend provides:

Wildlife event processing
Behaviour recognition workflows
Risk assessment engine
Alert generation
Device monitoring
Dashboard analytics
API integration with frontend systems
Tech Stack
FastAPI
Python
Supabase
PostgreSQL
Computer Vision
YOLOv8
R3D-18
SlowFast
TensorFlow
OpenCV
Features
Animal detection
Behaviour classification
Risk scoring
Alert management
Device management
Dashboard summary APIs
Event logging
Feedback collection
API Endpoints
GET /dashboard/summary

GET /devices

GET /alerts

GET /events

POST /observations

POST /feedback
System Architecture
Camera
   ↓
Detection Model (YOLOv8)
   ↓
Behaviour Model (R3D-18)
   ↓
Risk Engine
   ↓
Deterrence Engine
   ↓
Supabase Database
   ↓
Frontend Dashboard
Author

Tasnia Haque Moumi

Taylor's University

Computer Science (Artificial Intelligence)
