from typing import List
from schemas import TelemetryPayload, SystemComponent
from datetime import datetime

def analyze_finops_anomaly(payloads: List[TelemetryPayload], threshold_usd: float = 50.0) -> List[dict]:
    violations = []
    for p in payloads:
        if p.billing_rate_hourly_usd > threshold_usd:
            violations.append({
                "component": p.component.value,
                "metric": "hourly_cost_usd",
                "observed": p.billing_rate_hourly_usd,
                "action": "SCALE_DOWN_REPLICAS_OR_SUSPEND"
            })
    return violations

def analyze_sre_health(payloads: List[TelemetryPayload], max_cpu_pct: float = 85.0, max_latency_ms: float = 200.0) -> List[dict]:
    alerts = []
    for p in payloads:
        if p.cpu_utilization_pct >= max_cpu_pct and p.network_latency_ms >= max_latency_ms:
            alerts.append({
                "component": p.component.value,
                "action": "RESTART_CONTAINER_POD_AND_ALLOCATE_MEMORY"
            })
    return alerts