from datetime import datetime
from typing import List
from schemas import TelemetryPayload

def parse_raw_telemetry(raw_stream: str) -> List[TelemetryPayload]:
    payloads = []
    for line in raw_stream.strip().split("\n"):
        if line.strip():
            parts = line.split(":")
            component = parts[0]
            data = {"component": component, **dict(p.split("=") for p in parts[1].split(","))}
            data["timestamp"] = datetime.utcnow()
            payloads.append(TelemetryPayload(**data))
    return payloads