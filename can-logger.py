import can
import csv
import os
from datetime import datetime

def start_logger(interface='virtual', channel='vcan0', output_file='normal_can_traffic.csv'):
    """
    Logs CAN traffic to a CSV file.
    
    Args:
        interface (str): The CAN interface (e.g., 'socketcan', 'vector', 'virtual').
        channel (str): The channel name.
        output_file (str): Path to the output CSV file.
    """
    print(f"Starting CAN Logger on {channel} ({interface})...")
    
    # Define CSV headers
    headers = ['Timestamp', 'CAN_ID', 'DLC', 'Payload']
    
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.isfile(output_file)

    try:
        # Initialize the CAN bus
        # Note: interface='virtual' is used for testing without hardware
        bus = can.interface.Bus(interface=interface, channel=channel, bitrate=500000)

        with open(output_file, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            if not file_exists:
                writer.writerow(headers)

            print("Logging started. Press Ctrl+C to stop.")
            
            count = 0
            while True:
                message = bus.recv(timeout=1.0)
                
                if message is not None:
                    # Extract data
                    timestamp = datetime.fromtimestamp(message.timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
                    can_id = hex(message.arbitration_id)
                    dlc = message.dlc
                    payload = message.data.hex(' ')
                    
                    # Write to CSV
                    writer.writerow([timestamp, can_id, dlc, payload])
                    
                    count += 1
                    if count % 10 == 0:
                        print(f"Messages collected: {count}", end='
')

    except KeyboardInterrupt:
        print(f"
Logging stopped. Total messages saved: {count}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # To use a physical interface, change interface to 'socketcan' and channel to 'can0'
    start_logger(interface='virtual', channel='vcan0')
