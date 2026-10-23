from datetime import datetime, UTC
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TelemetryType(str, Enum):
    METRIC = "METRIC"
    LOG = "LOG"
    TRACE = "TRACE"


class SystemComponent(str, Enum):
    COMPUTE = "K8S_POD"
    DATABASE = "POSTGRES"
    GATEWAY = "API_ROUTER"


class TelemetryPayload(BaseModel):
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="UTC time of event emission"
    )
    component: SystemComponent = Field(
        ..., description="Target architectural infrastructure sub-component"
    )
    payload_type: TelemetryType = Field(
        ..., description="Telemetry schema discriminator classification"
    )
    cpu_utilization_pct: float = Field(
        ..., ge=0.0, le=100.0, description="CPU usage ratio validation"
    )
    memory_utilization_pct: float = Field(
        ..., ge=0.0, le=100.0, description="Memory consumption boundary"
    )
    network_latency_ms: float = Field(
        ..., ge=0.0, description="System transaction round-trip delta time"
    )
    billing_rate_hourly_usd: float = Field(
        ..., ge=0.0, description="Real-time localized cluster running cost"
    )
    log_message: Optional[str] = Field(
        None, max_length=1024, description="Sanitized debug context snapshot"
    )

    model_config = ConfigDict(frozen=True)
