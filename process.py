"""Car processing logic through paint shop stations"""
import simpy
import random
import config

def car_process(env, car_id, stations, metrics):
    arrival_time = env.now
    print(f"[{env.now:6.1f}] Car {car_id} arrives at the system")
    
    # STATION 1: Cleaning
    yield env.process(process_station(
        env, car_id, "Cleaning",
        stations['cleaning'],
        metrics.cleaning_metrics,
        config.CLEANING_MIN,
        config.CLEANING_MAX
    ))
    
    # STATION 2: Primer Application
    yield env.process(process_station(
        env, car_id, "Primer",
        stations['primer'],
        metrics.primer_metrics,
        config.PRIMER_MIN,
        config.PRIMER_MAX
    ))
    
    # STATION 3: Painting
    yield env.process(process_station(
        env, car_id, "Paint",
        stations['painting'],
        metrics.painting_metrics,
        config.PAINTING_MIN,
        config.PAINTING_MAX
    ))
    
    # Car exits system
    exit_time = env.now
    metrics.record_car_completion(arrival_time, exit_time)
    print(f"[{env.now:6.1f}] Car {car_id} exits the system (Total time: {exit_time - arrival_time:.1f} min)")


def process_station(env, car_id, station_name, resource, station_metrics, min_time, max_time):

    # Record queue length before requesting resource
    queue_length = len(resource.queue)
    station_metrics.record_queue_length(queue_length)
    
    # Request resource (wait in queue if busy)
    queue_enter_time = env.now
    with resource.request() as request:
        yield request  # Wait until resource is available
        
        # Record waiting time
        wait_time = env.now - queue_enter_time
        station_metrics.record_wait_time(wait_time)
        
        # Start processing
        process_time = random.uniform(min_time, max_time)
        station_metrics.start_processing(env.now)
        print(f"[{env.now:6.1f}] Car {car_id} starts {station_name}")
        yield env.timeout(process_time)
        
        # Finish processing
        station_metrics.finish_processing(env.now)
        print(f"[{env.now:6.1f}] Car {car_id} finishes {station_name}")


def car_generator(env, stations, metrics):
    car_id = 0
    while True:
        # Create new car
        car_id += 1
        env.process(car_process(env, car_id, stations, metrics))
        
        # Wait for next car arrival
        next_arrival = random.uniform(config.ARRIVAL_MIN, config.ARRIVAL_MAX)
        yield env.timeout(next_arrival)
