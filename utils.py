"""
Utility functions for paint shop simulation analysis
"""

import config


def identify_bottleneck(metrics):
    """
    Identify the bottleneck station based on utilization.
    
    Args:
        metrics: MetricsCollector instance containing all station metrics
    
    Returns:
        String with bottleneck station name
    """
    stations = [
        ("Cleaning", metrics.cleaning_metrics),
        ("Primer", metrics.primer_metrics),
        ("Paint", metrics.painting_metrics)
    ]
    
    bottleneck = max(stations, key=lambda x: x[1].get_utilization(config.SIM_TIME))
    station_name = bottleneck[0]
    station_metrics = bottleneck[1]
    
    print(f"\nBottleneck Analysis:")
    print(f"Primary bottleneck: {station_name} station")
    print(f"Utilization: {station_metrics.get_utilization(config.SIM_TIME):.1f}%")
    print(f"Max queue: {station_metrics.max_queue_length} cars")
    
    return station_name


def suggest_optimization(bottleneck_name):
    """
    Provide optimization recommendations based on bottleneck.
    
    Args:
        bottleneck_name: Name of the bottleneck station
    """
    print(f"\nOptimization Suggestions:")
    
    if bottleneck_name == "Cleaning":
        print("- Add a second cleaning machine (increase capacity to 2)")
        print("- Reduce cleaning time through process improvement")
        
    elif bottleneck_name == "Primer":
        print("- Add a third primer machine (increase capacity to 3)")
        print("- Optimize primer application process to reduce time")
        
    elif bottleneck_name == "Paint":
        print("- Add a second painting machine (increase capacity to 2)")
        print("- Use faster-drying paint to reduce cycle time")


def analyze_queue_patterns(metrics):
    """
    Analyze queue behavior patterns across all stations.
    
    Args:
        metrics: MetricsCollector instance
    
    Returns:
        Dictionary with queue analysis
    """
    stations = {
        "Cleaning": metrics.cleaning_metrics,
        "Primer": metrics.primer_metrics,
        "Paint": metrics.painting_metrics
    }
    
    print(f"\nQueue Pattern Analysis:")
    
    analysis = {}
    
    for name, station in stations.items():
        max_queue = station.max_queue_length
        avg_wait = station.get_average_wait_time()
        
        if max_queue <= 2:
            severity = "Low"
        elif max_queue <= 4:
            severity = "Moderate"
        else:
            severity = "High"
        
        analysis[name] = {
            'max_queue': max_queue,
            'avg_wait': avg_wait,
            'severity': severity
        }
        
        print(f"{name}: Max queue {max_queue} cars, Avg wait {avg_wait:.1f} min, Severity: {severity}")
    
    return analysis


def calculate_system_efficiency(metrics):
    """
    Calculate overall system efficiency.
    
    Args:
        metrics: MetricsCollector instance
    
    Returns:
        Dictionary with efficiency metrics
    """
    cleaning_time_avg = (config.CLEANING_MIN + config.CLEANING_MAX) / 2
    painting_time_avg = (config.PAINTING_MIN + config.PAINTING_MAX) / 2
    
    theoretical_cycle_time = max(cleaning_time_avg, painting_time_avg)
    theoretical_max_cars = config.SIM_TIME / theoretical_cycle_time
    
    actual_cars = metrics.completed_cars
    efficiency = (actual_cars / theoretical_max_cars) * 100
    
    print(f"\nSystem Efficiency:")
    print(f"Theoretical max: {theoretical_max_cars:.1f} cars")
    print(f"Actual: {actual_cars} cars")
    print(f"Efficiency: {efficiency:.1f}%")
    
    return {
        'theoretical_max': theoretical_max_cars,
        'actual': actual_cars,
        'efficiency': efficiency
    }


def compare_station_utilizations(metrics):
    """
    Compare station utilizations.
    
    Args:
        metrics: MetricsCollector instance
    """
    print(f"\nStation Utilization Comparison:")
    
    stations_data = [
        ("Cleaning", config.CLEANING_CAPACITY, metrics.cleaning_metrics),
        ("Primer", config.PRIMER_CAPACITY, metrics.primer_metrics),
        ("Paint", config.PAINTING_CAPACITY, metrics.painting_metrics)
    ]
    
    for name, capacity, station in stations_data:
        util = station.get_utilization(config.SIM_TIME)
        print(f"{name}: Capacity {capacity}, Utilization {util:.1f}%")


def generate_what_if_scenarios():
    """
    Suggest what-if scenarios for testing.
    """
    print(f"\nSuggested What-If Scenarios:")
    print("1. Increase cleaning capacity from 1 to 2")
    print("2. Add third primer machine (capacity 2 to 3)")
    print("3. Reduce cleaning time to 10-15 minutes")
    print("4. Increase arrival interval to 10-14 minutes")
    print("5. Add second paint station (capacity 1 to 2)")


def run_full_analysis(metrics):
    """
    Run all analysis functions.
    
    Args:
        metrics: MetricsCollector instance
    """
    bottleneck = identify_bottleneck(metrics)
    suggest_optimization(bottleneck)
    analyze_queue_patterns(metrics)
    calculate_system_efficiency(metrics)
    compare_station_utilizations(metrics)
    generate_what_if_scenarios()
