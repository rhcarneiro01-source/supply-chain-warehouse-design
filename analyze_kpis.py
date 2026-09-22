"""Synthetic warehouse KPI comparison.

This script intentionally uses only Python's standard library so the
portfolio example can be executed without installing dependencies.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

DATA_FILE = Path(__file__).with_name("synthetic_kpis.csv")

METRICS = {
    "picking_time_min": ("Average picking time", "min", "lower"),
    "travel_distance_m": ("Internal travel distance", "m", "lower"),
    "orders_per_hour": ("Orders processed", "orders/h", "higher"),
    "order_accuracy_pct": ("Order accuracy", "%", "higher"),
    "dock_cycle_min": ("Dock cycle time", "min", "lower"),
}


def load_data(path: Path) -> dict[str, list[dict[str, float]]]:
    grouped: dict[str, list[dict[str, float]]] = defaultdict(list)
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            grouped[row["scenario"]].append(
                {metric: float(row[metric]) for metric in METRICS}
            )
    return grouped


def scenario_averages(rows: list[dict[str, float]]) -> dict[str, float]:
    return {metric: mean(row[metric] for row in rows) for metric in METRICS}


def improvement(baseline: float, proposed: float, direction: str) -> float:
    if baseline == 0:
        return 0.0
    if direction == "lower":
        return (baseline - proposed) / baseline * 100
    return (proposed - baseline) / baseline * 100


def main() -> None:
    data = load_data(DATA_FILE)
    baseline = scenario_averages(data["Baseline"])
    proposed = scenario_averages(data["Proposed"])

    print("Warehouse KPI Comparison — Synthetic Portfolio Scenario")
    print("=" * 62)
    print(f"{'Metric':30} {'Baseline':>10} {'Proposed':>10} {'Change':>9}")
    print("-" * 62)

    for metric, (label, unit, direction) in METRICS.items():
        b = baseline[metric]
        p = proposed[metric]
        delta = improvement(b, p, direction)
        print(f"{label:30} {b:9.2f} {p:9.2f} {delta:8.1f}%")

    print("\nNote: all values are synthetic and for portfolio demonstration only.")


if __name__ == "__main__":
    main()
