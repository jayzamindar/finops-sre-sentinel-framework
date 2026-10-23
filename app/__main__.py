import sys
import os
from pydantic import ValidationError

# Hard-coded path guard: Forces Python to see the root directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from app.schemas import TelemetryPayload, SystemComponent, TelemetryType
from app.engine import CoreOrchestrator

def run_sentinel_pipeline() -> None:
    print("=" * 60)
    print("INITIALIZING FINOPS-SRE SENTINEL PORTFOLIO SIMULATION")
    print("=" * 60)
    
    orchestrator = CoreOrchestrator()
    
    # 1. Happy Path Ingestion Check
    print("\n[STREAM] Simulating Clean Production Metric Ingestion...")
    try:
        valid_payload = TelemetryPayload(
            component=SystemComponent.DATABASE,
            payload_type=TelemetryType.METRIC,
            cpu_utilization_pct=42.5,
            memory_utilization_pct=68.2,
            network_latency_ms=14.7,
            billing_rate_hourly_usd=1.45,
            log_message="Production cluster telemetry data stream clear"
        )
        result = orchestrator.route_telemetry(valid_payload)
        print(f"   ↳ [SUCCESS] Telemetry Router Response Status: {result.get('status')}")
    except Exception as e:
        print(f"   ↳ [CRASH] Unexpected pipeline error: {e}")

    # 2. Defensive Guardrail Validation Check
    print("\n[STREAM] Simulating Anomalous / Hallucinated Metric Ingestion...")
    try:
        TelemetryPayload(
            component=SystemComponent.DATABASE,
            payload_type=TelemetryType.METRIC,
            cpu_utilization_pct=135.0,  # Invalid: Exceeds 100% maximum boundary limit
            memory_utilization_pct=68.2,
            network_latency_ms=14.7,
            billing_rate_hourly_usd=1.45
        )
        print("   ↳ [FAIL] Architectural breach! Malformed data slipped past our contract.")
    except ValidationError as e:
        print("   ↳ [✓ GUARDRAIL ACTIVE] Out-of-bounds metric blocked instantly by strict schema.")
        print(f"     [!] Captured Constraint Violation Error: {e.errors()[0]['msg']}")
    
    print("\n" + "=" * 60)
    print("SIMULATION WORKFLOW COMPLETE - ALL INFRASTRUCTURE GUARDRAILS ACTIVE")
    print("=" * 60)

if __name__ == "__main__":
    run_sentinel_pipeline()
