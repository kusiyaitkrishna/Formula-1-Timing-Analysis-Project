import sys
from statistics import mean
from collections import defaultdict
from tabulate import tabulate

# Load driver data into a dictionary for quick lookup
def load_driver_info(file_name):
    driver_info = {}
    with open(file_name, "r") as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(",")
                code, name, team = parts[1], parts[2], parts[3]
                driver_info[code] = {"name": name, "team": team}
    return driver_info

# Process the lap times file
def process_lap_times(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        if not lines:
            print("Error: File is empty.")
            return None, None

        race_name = lines[0].strip()
        lap_times = defaultdict(list)

        for line in lines[1:]:
            code, time = line[:3], float(line[3:])
            lap_times[code].append(time)

        return race_name, lap_times

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Generate the report
def generate_report(race_name, lap_times, driver_info):
    if not lap_times:
        print("No lap times available.")
        return

    overall_fastest_time = float('inf')
    overall_fastest_driver = None

    driver_summary = []
    for driver, times in lap_times.items():
        fastest_time = min(times)
        average_time = mean(times)

        if fastest_time < overall_fastest_time:
            overall_fastest_time = fastest_time
            overall_fastest_driver = driver

        driver_summary.append(
            [
                driver,
                driver_info.get(driver, {}).get("name", "Unknown"),
                driver_info.get(driver, {}).get("team", "Unknown"),
                f"{fastest_time:.3f}",
                f"{average_time:.3f}"
            ]
        )

    # Sort by fastest time in descending order
    driver_summary.sort(key=lambda x: float(x[3]), reverse=True)

    overall_average_time = mean([time for times in lap_times.values() for time in times])

    print(f"\nRace Name: {race_name}\n")
    print(f"Fastest Driver: {overall_fastest_driver} ({driver_info.get(overall_fastest_driver, {}).get('name', 'Unknown')}) with a time of {overall_fastest_time:.3f}\n")
    print(f"Overall Average Time: {overall_average_time:.3f}\n")

    print("Driver Performance Summary:\n")
    print(tabulate(driver_summary, headers=["Code", "Name", "Team", "Fastest Time", "Average Time"], tablefmt="grid"))

# Menu-driven interface
def menu():
    driver_info = None
    while True:
        print("\nFormula 1 Timing Analysis")
        print("1. Load Driver Information")
        print("2. Process Lap Times File")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            drivers_file = input("Enter the driver info file name: ")
            driver_info = load_driver_info(drivers_file)
            if driver_info:
                print("Driver information loaded successfully.")

        elif choice == "2":
            if not driver_info:
                print("Please load driver information first.")
                continue

            lap_times_file = input("Enter the lap times file name: ")
            race_name, lap_times = process_lap_times(lap_times_file)

            if race_name and lap_times:
                print("Lap times processed successfully.")
            else:
                print("Failed to process lap times.")

        elif choice == "3":
            if not driver_info or not lap_times:
                print("Please load driver information and process lap times first.")
                continue

            generate_report(race_name, lap_times, driver_info)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
