"""Real-time monitoring and alert system"""
import simpy
import config

def queue_monitor(env, stations, metrics):
    # Monitors queue lengths and triggers alerts when threshold exceeded.
    station_list = [
        ("Cleaning", stations['cleaning']),
        ("Primer", stations['primer']),
        ("Paint", stations['painting'])
    ]
    
    # Track previous queue lengths to avoid duplicate alerts
    previous_alerts = {"Cleaning": False, "Primer": False, "Paint": False}
    
    while True:
        for station_name, resource in station_list:
            queue_length = len(resource.queue)
            
            # Alert only when crossing threshold (not every minute)
            if queue_length > config.QUEUE_ALERT_THRESHOLD and not previous_alerts[station_name]:
                print(f"\nALERT: Queue at {station_name} has {queue_length} cars waiting at time {env.now:.1f}\n")
                metrics.alert_count += 1
                previous_alerts[station_name] = True
            elif queue_length <= config.QUEUE_ALERT_THRESHOLD:
                previous_alerts[station_name] = False
        
        yield env.timeout(5)  # Check every 5 minutes instead of 1


def utilization_monitor(env, stations, metrics):
    # Periodically samples resource utilization.
    while True:
        yield env.timeout(10)
