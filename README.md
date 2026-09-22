# Synthetic KPI Analysis

This folder contains a small, fully synthetic scenario designed to demonstrate how warehouse-layout decisions can be evaluated using operational KPIs.

## Dataset

`synthetic_kpis.csv` compares two scenarios:

- `Baseline` — illustrative current-state operation;
- `Proposed` — illustrative operation after the redesigned layout.

The values are not real company data and should not be interpreted as validated business results.

## Metrics

- `picking_time_min` — average picking time per order;
- `travel_distance_m` — average internal travel distance per order;
- `orders_per_hour` — average processed orders per hour;
- `order_accuracy_pct` — order accuracy percentage;
- `dock_cycle_min` — average dock cycle time.

## Run

```bash
python analyze_kpis.py
```

The script uses only the Python standard library.
