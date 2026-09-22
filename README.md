# Supply Chain Warehouse Design

**Warehouse layout and operational-flow case study focused on productivity, safety, inventory turnover and scalability.**

[Versão em Português](README.pt-BR.md)

![Warehouse layout](assets/warehouse-layout.png)

## Overview

This portfolio project presents a conceptual warehouse design organized around product velocity and a clear material flow from receiving to shipping. The proposed layout separates slow-, medium- and fast-moving inventory, places high-turnover items closer to picking and shipping, and creates dedicated preparation, packing and sorting areas.

The repository also includes a small **synthetic KPI analysis** to demonstrate how the proposed design could be evaluated with operational data. The dataset is illustrative and contains no confidential or company data.

## Business problem

Traditional warehouse layouts can create unnecessary travel, intersecting flows, picking delays and poor use of high-value space. This project explores a layout that aims to:

- reduce internal travel distance;
- improve picking productivity;
- separate inbound and outbound flows;
- organize inventory according to turnover;
- improve operational safety;
- support future expansion;
- create a structure ready for WMS-driven operations.

## Proposed material flow

```text
Receiving
   ↓
Storage (slow / main)
   ↓
Fast-moving area
   ↓
Picking / Preparation
   ↓
Packing
   ↓
Sorting
   ↓
Shipping
```

## Main warehouse areas

| Area | Purpose |
|---|---|
| Receiving | Check-in, identification and system registration |
| Slow-moving storage | Lower-turnover items positioned farther from shipping |
| Main storage | Medium-turnover inventory with balanced accessibility |
| Fast-moving area | High-turnover items close to picking and shipping |
| Picking / Preparation | Order separation and staging |
| Packing | Standardized order packing |
| Sorting | Final organization by route, destination or carrier |
| Shipping | Final check, loading and dispatch |
| Docks | Inbound and outbound vehicle interface |

## Design principles applied

- Product-velocity-based slotting
- ABC-oriented storage logic
- Unidirectional material flow
- Reduced flow intersections
- Shorter picking paths
- Dedicated staging and packing zones
- Safe forklift and pedestrian circulation
- Modular expansion capability
- WMS and barcode/RFID readiness

## Expected operational benefits

- Lower travel time inside the warehouse
- Higher picking productivity
- Better order accuracy
- Reduced congestion and flow crossing
- Improved use of storage space
- Safer movement of people and equipment
- Easier process standardization
- Better scalability for future growth

## Analytical extension

The folder [`analysis/`](analysis/) contains a synthetic baseline-versus-proposed scenario. It demonstrates how a warehouse redesign could be measured using KPIs such as:

- average picking time;
- internal travel distance;
- orders processed per hour;
- order accuracy;
- dock cycle time.

Run the analysis with:

```bash
python analysis/analyze_kpis.py
```

No external Python packages are required.

## Repository structure

```text
supply-chain-warehouse-design/
├── README.md
├── README.pt-BR.md
├── LICENSE
├── .gitignore
├── assets/
│   ├── warehouse-layout.png
│   └── project-overview.png
├── docs/
│   ├── case-study.md
│   └── case-study.pt-BR.md
└── analysis/
    ├── README.md
    ├── synthetic_kpis.csv
    └── analyze_kpis.py
```

## Skills demonstrated

`Supply Chain Management` · `Warehouse Design` · `Inventory Management` · `Picking Optimization` · `Process Improvement` · `Operational Analytics` · `KPI Design` · `Python` · `Problem Solving`

## Portfolio note

This repository is an independent portfolio adaptation of a warehouse-layout learning project. The KPI dataset is synthetic and was created only to demonstrate analytical reasoning. No confidential operational data is included.

## Author

**Renan Henrique Carneiro**  
Data Science · Supply Chain Analytics · Python · SQL · Artificial Intelligence · Software Engineering
