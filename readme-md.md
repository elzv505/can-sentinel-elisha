# Automotive ECU Intrusion Detection System - Data Logger

This repository contains the tools and datasets for logging Controller Area Network (CAN) traffic to be used in training Machine Learning models for ECU intrusion detection.

## Files in this Repository

### 1. `can_logger.py`
The core Python utility for data acquisition.
- **Function**: Connects to a CAN interface (SocketCAN, Virtual, or Vector) and listens for incoming frames.
- **Data Extraction**: For every message received, it parses the system timestamp, the Arbitration ID (CAN ID), the Data Length Code (DLC), and the hexadecimal payload.
- **Storage**: Appends captured data in real-time to a CSV file.

### 2. `normal_can_traffic.csv`
The resulting dataset from the logging process.
- **Format**: CSV (Comma Separated Values).
- **Use Case**: This file serves as the "Normal" baseline for training Anomaly Detection models. It contains legitimate vehicle communication patterns.

### 3. `dataset_documentation.docx`
A formal technical report.
- **Contents**: Detailed field descriptions, setup instructions for the `python-can` library, and validation metrics (e.g., message counts and data integrity checks).

### 4. `requirements.txt`
A standard Python dependency file.
- **Purpose**: Lists the libraries needed to run the logger (`python-can`).

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Logger**:
   ```bash
   python can_logger.py
   ```

3. **Stop Logging**:
   Press `Ctrl+C` to safely close the bus connection and finalize the CSV file.
