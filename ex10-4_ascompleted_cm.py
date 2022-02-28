from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from my_devices import network_devices
from ex10_my_functions import ssh_command

def main():
    
    start_time = datetime.now()
    max_threads = 5

    pool = ProcessPoolExecutor(max_threads)

    #Use context manager to cleanup the pool
    with ProcessPoolExecutor(max_threads) as pool:
        future_list = []
        for device in network_devices:
            future = pool.submit(ssh_command, device, "show version")
            future_list.append(future)

    #Process as completed
    for future in as_completed(future_list):
        print("=" * 25)
        print("Wohoo Router Result: " + future.result())
        end_time = datetime.now()
        print(f"Finished in {end_time - start_time}")
        print("\n\n")

if __name__ == "__main__":
    main()
