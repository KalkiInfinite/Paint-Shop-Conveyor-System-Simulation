"""Metrics collection and calculation"""
class MetricsCollector:
    # Collects and calculates simulation metrics
    def __init__(self):
        self.completed_cars = 0
        self.system_times = []
        
        self.cleaning_metrics = StationMetrics("Cleaning")
        self.primer_metrics = StationMetrics("Primer")
        self.painting_metrics = StationMetrics("Paint")
        
        self.alert_count = 0
    
    # Record when a car completes the system
    def record_car_completion(self, arrival_time, exit_time):
        self.completed_cars += 1
        system_time = exit_time - arrival_time
        self.system_times.append(system_time)
    
    # Calculate average time cars spend in system
    def get_average_system_time(self):
        if not self.system_times:
            return 0
        return sum(self.system_times) / len(self.system_times)
    
    # Print formatted simulation results
    def print_results(self):
        print(f"\n=== Paint Shop Simulation Results ({config.SIM_TIME} minutes) ===")
        print(f"Total cars completed: {self.completed_cars}")
        print(f"Average system time per car: {self.get_average_system_time():.1f} minutes")
        print()
        
        print("Station 1 (Cleaning):")
        print(f"- Utilization: {self.cleaning_metrics.get_utilization(config.SIM_TIME):.1f}%")
        print(f"- Max queue: {self.cleaning_metrics.max_queue_length} cars")
        print(f"- Avg wait time: {self.cleaning_metrics.get_average_wait_time():.1f} minutes")
        print()
        
        print("Station 2 (Primer):")
        print(f"- Utilization: {self.primer_metrics.get_utilization(config.SIM_TIME):.1f}%")
        print(f"- Max queue: {self.primer_metrics.max_queue_length} cars")
        print(f"- Avg wait time: {self.primer_metrics.get_average_wait_time():.1f} minutes")
        print()
        
        print("Station 3 (Painting):")
        print(f"- Utilization: {self.painting_metrics.get_utilization(config.SIM_TIME):.1f}%")
        print(f"- Max queue: {self.painting_metrics.max_queue_length} cars")
        print(f"- Avg wait time: {self.painting_metrics.get_average_wait_time():.1f} minutes")
        print()
        
        print(f"Alerts triggered: {self.alert_count} times")



class StationMetrics:
    # Tracks metrics for a single station
    
    def __init__(self, name):
        self.name = name
        self.wait_times = []
        self.max_queue_length = 0
        self.busy_time = 0
        self.last_start_time = None
    
    # Update max queue length if needed
    def record_queue_length(self, length):
        if length > self.max_queue_length:
            self.max_queue_length = length
    
    # Record time a car waited in queue
    def record_wait_time(self, wait_time):
        self.wait_times.append(wait_time)
    
    # Mark station as busy
    def start_processing(self, time):
        self.last_start_time = time
    
    # Mark station as free and update busy time
    def finish_processing(self, time):
        if self.last_start_time is not None:
            self.busy_time += (time - self.last_start_time)
    
    # Calculate station utilization percentage
    def get_utilization(self, total_time):
        if total_time == 0:
            return 0
        return (self.busy_time / total_time) * 100
    
    # Calculate average waiting time
    def get_average_wait_time(self):
        if not self.wait_times:
            return 0
        return sum(self.wait_times) / len(self.wait_times)

import config