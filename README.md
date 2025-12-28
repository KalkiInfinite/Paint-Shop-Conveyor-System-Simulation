# Paint Shop Conveyor System Simulation

## Overview
Discrete event simulation of an automotive paint shop using SimPy. Models 3 sequential stations (Cleaning, Primer, Painting) to analyze throughput and identify bottlenecks.

## Installation
pip install simpy

## Project Files
- main.py: Simulation runner (single/multiple runs)
- config.py: Configuration parameters
- process.py: Car journey through stations
- monitoring.py: Queue monitoring and alerts
- metrics.py: Metrics collection and display
- utils.py: Bottleneck analysis

## Running the Simulation

Single Run (testing):
python main.py
Enter: 1

Multiple Runs (recommended for results):
python main.py
Enter: 2
Enter: 5

## Output 1: Baseline Configuration (PAINTING_CAPACITY = 1)

Single Run Result:
Run 1:

=== Paint Shop Simulation Results (480 minutes) ===
Total cars completed: 12
Average system time per car: 211.0 minutes

Station 1 (Cleaning):
- Utilization: 99.9%
- Max queue: 20 cars
- Avg wait time: 102.9 minutes

Station 2 (Primer):
- Utilization: 60.5%
- Max queue: 0 cars
- Avg wait time: 0.0 minutes

Station 3 (Painting):
- Utilization: 86.8%
- Max queue: 11 cars
- Avg wait time: 98.1 minutes

Alerts triggered: 4 times

Bottleneck Analysis:
Primary bottleneck: Cleaning station
Utilization: 99.9%
Max queue: 20 cars

Optimization Suggestions:
- Add a second painting machine (increase capacity to 2)
- Reduce cleaning time through process improvement

Run 2:

=== Paint Shop Simulation Results (480 minutes) ===
Total cars completed: 12
Average system time per car: 223.6 minutes

Station 1 (Cleaning):
- Utilization: 99.3%
- Max queue: 19 cars
- Avg wait time: 104.9 minutes

Station 2 (Primer):
- Utilization: 67.5%
- Max queue: 0 cars
- Avg wait time: 0.1 minutes

Station 3 (Painting):
- Utilization: 87.8%
- Max queue: 11 cars
- Avg wait time: 103.1 minutes

Alerts triggered: 3 times

Bottleneck Analysis:
Primary bottleneck: Cleaning station
Utilization: 99.3%
Max queue: 19 cars

Multiple Runs (20 runs):

Results saved to: results/all_runs_summary.csv
AGGREGATED RESULTS ACROSS ALL RUNS
Number of runs: 20

Completed Cars:
  Mean: 11.8
  Std Dev: 0.41
  Range: 11 - 12

Average System Time (minutes):
  Mean: 220.3
  Std Dev: 5.68

Station Utilization:
  Cleaning: 98.4% (±1.0%)
  Primer: 65.6% (±3.9%)
  Paint: 86.8% (±2.3%)

Analysis: Severe bottleneck at Cleaning station (98% utilization)

A complete log table of the execution:
This is for the Run 1 of the Single Run Result displayed first in the output above:

STARTING RUN 1  
[   0.0] Car 1 arrives at the system  
[  10.0] Car 2 arrives at the system  
[  15.1] Car 1 finishes Cleaning  
[  19.9] Car 3 arrives at the system  
[  29.2] Car 4 arrives at the system  
[  32.2] Car 2 finishes Cleaning  
[  40.7] Car 5 arrives at the system  
[  41.7] Car 1 finishes Primer  
[  49.1] Car 3 finishes Cleaning  
[  49.2] Car 6 arrives at the system  
[  59.9] Car 2 finishes Primer  
[  60.1] Car 7 arrives at the system  
[  68.2] Car 4 finishes Cleaning  
[  70.6] Car 8 arrives at the system  
[  77.4] Car 1 finishes Paint  
[  77.4] Car 1 exits the system (Total time: 77.4 min)  
[  79.5] Car 9 arrives at the system  
ALERT: Queue at Cleaning has 4 cars waiting at time 80.0  
[  80.3] Car 3 finishes Primer  
[  83.8] Car 5 finishes Cleaning  
[  88.7] Car 10 arrives at the system  
ALERT: Queue at Cleaning has 4 cars waiting at time 90.0  
[  97.1] Car 4 finishes Primer  
[  98.2] Car 11 arrives at the system  
[ 100.4] Car 6 finishes Cleaning  
[ 107.5] Car 12 arrives at the system  
[ 109.5] Car 2 finishes Paint  
[ 109.5] Car 2 exits the system (Total time: 99.4 min)  
[ 113.0] Car 5 finishes Primer  
[ 116.7] Car 13 arrives at the system  
[ 119.1] Car 7 finishes Cleaning  
[ 126.1] Car 6 finishes Primer  
[ 127.6] Car 14 arrives at the system  
[ 137.9] Car 8 finishes Cleaning  
[ 138.7] Car 15 arrives at the system  
[ 140.7] Car 3 finishes Paint  
[ 140.7] Car 3 exits the system (Total time: 120.8 min)  
[ 148.3] Car 16 arrives at the system  
[ 152.2] Car 7 finishes Primer  
[ 156.9] Car 9 finishes Cleaning  
[ 159.8] Car 17 arrives at the system  
[ 167.3] Car 8 finishes Primer  
[ 169.8] Car 18 arrives at the system  
ALERT: Queue at Paint has 4 cars waiting at time 170.0  
[ 174.2] Car 4 finishes Paint  
[ 174.2] Car 4 exits the system (Total time: 145.0 min)  
[ 175.0] Car 10 finishes Cleaning  
[ 181.6] Car 19 arrives at the system  
[ 189.5] Car 9 finishes Primer  
ALERT: Queue at Paint has 4 cars waiting at time 190.0  
[ 192.2] Car 11 finishes Cleaning  
[ 193.4] Car 20 arrives at the system  
[ 201.6] Car 21 arrives at the system  
[ 203.3] Car 10 finishes Primer  
[ 211.2] Car 12 finishes Cleaning  
[ 212.2] Car 22 arrives at the system  
[ 213.2] Car 5 finishes Paint  
[ 213.2] Car 5 exits the system (Total time: 172.5 min)  
[ 220.9] Car 23 arrives at the system  
[ 220.9] Car 11 finishes Primer  
[ 227.5] Car 13 finishes Cleaning  
[ 229.0] Car 24 arrives at the system  
[ 238.1] Car 25 arrives at the system  
[ 238.2] Car 12 finishes Primer  
[ 246.2] Car 14 finishes Cleaning  
[ 247.6] Car 26 arrives at the system  
[ 253.2] Car 6 finishes Paint  
[ 253.2] Car 6 exits the system (Total time: 204.0 min)  
[ 259.4] Car 27 arrives at the system  
[ 261.4] Car 13 finishes Primer  
[ 262.6] Car 15 finishes Cleaning  
[ 267.6] Car 28 arrives at the system  
[ 276.5] Car 29 arrives at the system  
[ 278.5] Car 14 finishes Primer  
[ 282.0] Car 16 finishes Cleaning  
[ 284.0] Car 7 finishes Paint  
[ 284.0] Car 7 exits the system (Total time: 223.8 min)  
[ 288.1] Car 30 arrives at the system  
[ 296.2] Car 15 finishes Primer  
[ 298.3] Car 31 arrives at the system  
[ 301.1] Car 17 finishes Cleaning  
[ 309.7] Car 32 arrives at the system  
[ 310.7] Car 16 finishes Primer  
[ 314.2] Car 8 finishes Paint  
[ 314.2] Car 8 exits the system (Total time: 243.6 min)  
[ 321.0] Car 18 finishes Cleaning  
[ 321.7] Car 33 arrives at the system  
[ 328.5] Car 17 finishes Primer  
[ 332.7] Car 34 arrives at the system  
[ 336.7] Car 19 finishes Cleaning  
[ 344.5] Car 35 arrives at the system  
[ 346.5] Car 18 finishes Primer  
[ 351.3] Car 9 finishes Paint  
[ 351.3] Car 9 exits the system (Total time: 271.8 min)  
[ 355.0] Car 36 arrives at the system  
[ 355.6] Car 20 finishes Cleaning  
[ 365.2] Car 37 arrives at the system  
[ 367.8] Car 19 finishes Primer  
[ 371.0] Car 21 finishes Cleaning  
[ 376.2] Car 38 arrives at the system  
[ 383.6] Car 20 finishes Primer  
[ 385.9] Car 39 arrives at the system  
[ 386.3] Car 22 finishes Cleaning  
[ 388.8] Car 10 finishes Paint  
[ 388.8] Car 10 exits the system (Total time: 300.1 min)  
[ 395.1] Car 40 arrives at the system  
[ 404.5] Car 21 finishes Primer  
[ 405.2] Car 41 arrives at the system  
[ 406.2] Car 23 finishes Cleaning  
[ 415.0] Car 42 arrives at the system  
[ 417.0] Car 22 finishes Primer  
[ 420.2] Car 11 finishes Paint  
[ 420.2] Car 11 exits the system (Total time: 322.1 min)  
[ 423.6] Car 43 arrives at the system  
[ 424.4] Car 24 finishes Cleaning  
[ 435.0] Car 44 arrives at the system  
[ 437.7] Car 23 finishes Primer  
[ 443.0] Car 25 finishes Cleaning  
[ 445.6] Car 45 arrives at the system  
[ 449.7] Car 24 finishes Primer  
[ 456.8] Car 46 arrives at the system  
[ 458.5] Car 12 finishes Paint  
[ 458.5] Car 12 exits the system (Total time: 350.9 min)  
[ 462.3] Car 26 finishes Cleaning  
[ 465.5] Car 47 arrives at the system  
[ 470.3] Car 25 finishes Primer  
[ 475.9] Car 48 arrives at the system  
[ 479.5] Car 27 finishes Cleaning  


## Output 2: Optimized Configuration (PAINTING_CAPACITY = 2)

This is an example of if we increased a painting machine


=== Paint Shop Simulation Results (480 minutes) ===
Total cars completed: 23
Average system time per car: 169.1 minutes

Station 1 (Cleaning):
- Utilization: 96.5%
- Max queue: 19 cars
- Avg wait time: 97.0 minutes

Station 2 (Primer):
- Utilization: 65.3%
- Max queue: 0 cars
- Avg wait time: 0.1 minutes

Station 3 (Painting):
- Utilization: 80.3%
- Max queue: 1 cars
- Avg wait time: 8.5 minutes

Alerts triggered: 2 times

Bottleneck Analysis:
Primary bottleneck: Cleaning station
Utilization: 96.5%
Max queue: 19 cars


Analysis: Bottleneck eliminated, throughput doubled


## Before vs After Comparison

| Metric | Baseline (1 Painter) | Optimized (2 Painters) | Change |
|--------|---------------------|------------------------|--------|
| Throughput | 12 cars | 23 cars | +92% |
| System Time | 211.0 min | 169.1 min | -20% |
| Cleaning Utilization | 99.9% | 96.5% | Still bottleneck |
| Painting Utilization | 86.8% | 80.3% | Reduced |
| Max Painting Queue | 11 cars | 1 car | -91% |
| Max Cleaning Queue | 20 cars | 19 cars | -5% |
| Alerts Triggered | 4 times | 2 times | -50% |

## Key Parameters (config.py)

SIM_TIME = 480 minutes (8-hour shift)  
Car arrivals: 8-12 minutes (uniform)  
Cleaning: 15-20 minutes, capacity 1    
Primer: 25-35 minutes, capacity 2  
Painting: 30-40 minutes, capacity 1  
Alert threshold: 3 cars in queue

## Real-Time Monitoring Example


[8.5] Car 1 arrives at the system  
[8.5] Car 1 starts Cleaning (will take 17.3 min)  
[25.8] Car 1 finishes Cleaning  
[25.8] Car 1 starts Primer (will take 29.2 min)  
ALERT: Queue at Cleaning has 4 cars waiting at time 70.0  
[55.0] Car 1 finishes Primer  
[55.0] Car 1 starts Paint (will take 35.7 min)  
[90.7] Car 1 finishes Paint  
[90.7] Car 1 exits the system (Total time: 82.2 min)  

## Understanding Metrics

Utilization: Percentage of time station is busy. High (>90%) = bottleneck
Queue Length: Number of cars waiting. Max shows peak congestion
Wait Time: Time in queue before processing. Excludes processing time
System Time: Total time from arrival to exit. Includes all waits + processing

## Troubleshooting

Only 11-12 cars: Expected! Cleaning bottleneck by design. Test with CLEANING_CAPACITY = 2
Terminal overflow: Reduce prints in process.py or save to file
No CSV file: Run Option 2 (multiple runs) - creates results/ folder automatically

## Author
Piyush Tyagi

## License
Educational project for simulation coursework
