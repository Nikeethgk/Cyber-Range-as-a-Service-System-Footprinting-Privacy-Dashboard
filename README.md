# Cyber-Range-as-a-Service-System-Footprinting-Privacy-Dashboard
A GUI-based Python simulation built with `tkinter` that teaches reconnaissance anddefense within a CRaaS framework. Students experience phase-based attacks network discovery, OS fingerprinting, service enumeration while a live privacy dashboard tracks risk scores. Activate defenses, export logs, and reset instantly. Fully offline, zero dependencies

# 🛡️ System Footprinting & Privacy Dashboard

> A GUI-based Python simulation for practicing system reconnaissance and defensive hardening within a Cyber Range as a Service (CRaaS) environment.

## 📖 Overview
This application simulates attacker footprinting phases and provides an interactive privacy dashboard for monitoring system exposure. Built entirely with Python’s standard library and `tkinter`, it runs completely offline, requires zero external dependencies, and operates in a safe, isolated sandbox. Ideal for security training, workflow demonstration, and understanding the attack-defense lifecycle.

## ✨ Features
- **Phase-Based Footprinting:** Sequential simulation of Network, OS, Service, and Environment enumeration
- **Real-Time Privacy Dashboard:** Dynamic risk scoring with visual exposure tracking
- **Interactive Defense Controls:** Toggle Firewall, Service Hardening, and Privacy Mode to mitigate exposure
- **Session Management:** Live activity logging, JSON export, and one-click session reset
- **Zero Dependencies:** Runs on Python standard library only (`tkinter`, `platform`, `socket`, `os`)
- **Fully Offline & Safe:** No network calls, packet capture, or privileged system commands

## 🛠️ Requirements
- Python 3.8+ 
- `tkinter` (bundled with standard Python installers for Windows/macOS/Linux)
- No third-party packages required

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cyber_range_footprint_dashboard.git
   cd cyber_range_footprint_dashboard
