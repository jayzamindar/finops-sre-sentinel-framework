import pytest
from pydantic import ValidationError
from app.schemas import TelemetryPayload, SystemComponent, TelemetryType
from app.engine import CoreOrchestrator

def test_valid_telemetry_routing():
    orchestrator = CoreOrchestrator()
    payload = TelemetryPayload(
        component=SystemComponent.DATABASE,
        payload_type=TelemetryType.METRIC,
        cpu_utilization_pct=45.2,
        memory_utilization_pct=55.8,
        network_latency_ms=12.4,
        billing_rate_hourly_usd=1.25,
        log_message="Database telemetry snapshot"
    )
    result = orchestrator.route_telemetry(payload)
    # Checks for our new enterprise success pattern or processed fallback
    assert result["status"] in ["PROCESSED", "SUCCESS"]

def test_schema_boundary_validation():
    with pytest.raises(ValidationError):
        TelemetryPayload(
            component=SystemComponent.DATABASE,
            payload_type=TelemetryType.METRIC,
            cpu_utilization_pct=105.0,
            memory_utilization_pct=55.8,
            network_latency_ms=12.4,
            billing_rate_hourly_usd=1.25
        )
