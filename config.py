"""Configuration parameters for paint shop simulation"""
# Simulation time
SIM_TIME = 480  # minutes (8 hours shift)

# Car arrival times (uniform distribution)
ARRIVAL_MIN = 8
ARRIVAL_MAX = 12

# Station processing times (uniform distribution)
CLEANING_MIN = 15
CLEANING_MAX = 20

PRIMER_MIN = 25
PRIMER_MAX = 35

PAINTING_MIN = 30
PAINTING_MAX = 40

# Station capacities
CLEANING_CAPACITY = 1
PRIMER_CAPACITY = 2  # Can process 2 cars in parallel
PAINTING_CAPACITY = 1

# Alert threshold
QUEUE_ALERT_THRESHOLD = 3  # Trigger alert when queue > 3 cars
