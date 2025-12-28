import simpy
import random
import config
from metrics import MetricsCollector
from process import car_generator
from monitoring import queue_monitor, utilization_monitor
from utils import identify_bottleneck, suggest_optimization
import csv
import os


def setup_simulation():
    """Initialize simulation environment and resources"""
    env = simpy.Environment()
    
    stations = {
        'cleaning': simpy.Resource(env, capacity=config.CLEANING_CAPACITY),
        'primer': simpy.Resource(env, capacity=config.PRIMER_CAPACITY),
        'painting': simpy.Resource(env, capacity=config.PAINTING_CAPACITY)
    }
    
    metrics = MetricsCollector()
    
    return env, stations, metrics


def run_single_simulation(run_number, save_log=False):
    """
    Run a single simulation instance.
    
    Args:
        run_number: Simulation run identifier
        save_log: Whether to save console output to file
    
    Returns:
        Dictionary with key metrics
    """
    print(f"STARTING RUN {run_number}")
    
    # Setup
    env, stations, metrics = setup_simulation()
    
    # Start processes
    env.process(car_generator(env, stations, metrics))
    env.process(queue_monitor(env, stations, metrics))
    env.process(utilization_monitor(env, stations, metrics))
    
    # Run simulation
    env.run(until=config.SIM_TIME)
    
    # Print results
    metrics.print_results()
    
    # Bottleneck analysis
    bottleneck = identify_bottleneck(metrics)
    suggest_optimization(bottleneck)
    
    # Return key metrics for aggregation
    return {
        'run_number': run_number,
        'completed_cars': metrics.completed_cars,
        'avg_system_time': metrics.get_average_system_time(),
        'cleaning_utilization': metrics.cleaning_metrics.get_utilization(config.SIM_TIME),
        'primer_utilization': metrics.primer_metrics.get_utilization(config.SIM_TIME),
        'paint_utilization': metrics.painting_metrics.get_utilization(config.SIM_TIME),
        'cleaning_max_queue': metrics.cleaning_metrics.max_queue_length,
        'primer_max_queue': metrics.primer_metrics.max_queue_length,
        'paint_max_queue': metrics.painting_metrics.max_queue_length,
        'alerts_triggered': metrics.alert_count,
        'bottleneck': bottleneck
    }


def run_multiple_simulations(num_runs=5):
    """
    Run simulation multiple times and aggregate results.
    
    Args:
        num_runs: Number of simulation runs
    """
    all_results = []
    
    for i in range(1, num_runs + 1):
        # Different random seed each run for variability
        random.seed(None)  # Use system time as seed
        
        # Run simulation
        result = run_single_simulation(i)
        all_results.append(result)
    
    # Save results to CSV
    save_results_to_csv(all_results)
    
    # Print aggregated statistics
    print_aggregated_results(all_results)


def save_results_to_csv(results):
    """Save all run results to CSV file"""
    # Create results directory if it doesn't exist
    os.makedirs('results', exist_ok=True)
    
    # Save to CSV
    filename = 'results/all_runs_summary.csv'
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"\nResults saved to: {filename}")


def print_aggregated_results(results):
    """Calculate and print mean and std dev across all runs"""
    import statistics
    
    print("AGGREGATED RESULTS ACROSS ALL RUNS")
    
    # Extract metrics
    completed_cars = [r['completed_cars'] for r in results]
    avg_system_times = [r['avg_system_time'] for r in results]
    cleaning_utils = [r['cleaning_utilization'] for r in results]
    primer_utils = [r['primer_utilization'] for r in results]
    paint_utils = [r['paint_utilization'] for r in results]
    
    print(f"Number of runs: {len(results)}\n")
    
    print(f"Completed Cars:")
    print(f"  Mean: {statistics.mean(completed_cars):.1f}")
    print(f"  Std Dev: {statistics.stdev(completed_cars):.2f}")
    print(f"  Range: {min(completed_cars)} - {max(completed_cars)}\n")
    
    print(f"Average System Time (minutes):")
    print(f"  Mean: {statistics.mean(avg_system_times):.1f}")
    print(f"  Std Dev: {statistics.stdev(avg_system_times):.2f}\n")
    
    print(f"Station Utilization:")
    print(f"  Cleaning: {statistics.mean(cleaning_utils):.1f}% (±{statistics.stdev(cleaning_utils):.1f}%)")
    print(f"  Primer: {statistics.mean(primer_utils):.1f}% (±{statistics.stdev(primer_utils):.1f}%)")
    print(f"  Paint: {statistics.mean(paint_utils):.1f}% (±{statistics.stdev(paint_utils):.1f}%)")
    
def main():
    """Main entry point"""
    print("Paint Shop Conveyor System Simulation")
    
    # Choice: Single run or multiple runs
    mode = input("Run mode? (1=Single run, 2=Multiple runs): ").strip()
    
    if mode == "1":
        # Single run with fixed seed for reproducibility
        random.seed(None)
        run_single_simulation(1)
    else:
        # Multiple runs for statistical analysis
        num_runs = int(input("How many runs? (recommended: 5-10): ").strip())
        run_multiple_simulations(num_runs)


if __name__ == "__main__":
    main()
