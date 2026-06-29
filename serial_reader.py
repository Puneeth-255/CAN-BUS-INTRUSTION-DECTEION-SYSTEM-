import argparse
import os
import serial
import serial.tools.list_ports as list_ports
import pandas as pd
import joblib

parser = argparse.ArgumentParser(description="Read CAN data from serial and classify it.")
parser.add_argument("--port", default=os.getenv("SERIAL_PORT", "COM3"), help="Serial port to connect to")
parser.add_argument("--baudrate", type=int, default=int(os.getenv("SERIAL_BAUDRATE", "115200")), help="Serial baud rate")
parser.add_argument("--auto", action="store_true", help="Choose the first available serial port automatically")
args = parser.parse_args()

if args.auto:
    ports = list(list_ports.comports())
    if not ports:
        raise SystemExit("No serial ports available to select automatically.")
    args.port = ports[0].device

model = joblib.load("model.pkl")

try:
    arduino = serial.Serial(args.port, args.baudrate)
except serial.SerialException as exc:
    available = "\n".join(f"{p.device} - {p.description}" for p in list_ports.comports())
    raise SystemExit(
        f"Could not open serial port {args.port}: {exc}\n"
        f"Available ports:\n{available}"
    )

while True:

    line = arduino.readline().decode(errors="ignore").strip()
    if not line:
        continue

    values = line.split(",")
    if len(values) < 3:
        print(f"Skipping non-CAN line: {line}")
        continue

    try:
        can_id = int(values[0])
        dlc = int(values[1])
        data_sum = int(values[2])
    except ValueError:
        print(f"Skipping invalid CAN data: {line}")
        continue

    df = pd.DataFrame([[
        can_id,
        dlc,
        data_sum
    ]],
    columns=[
        "CAN_ID",
        "DLC",
        "DATA_SUM"
    ])

    prediction = model.predict(df)

    if prediction[0] == -1:

        print(
            f"ATTACK DETECTED → ID:{can_id}"
        )

    else:

        print(
            f"NORMAL → ID:{can_id}"
        )