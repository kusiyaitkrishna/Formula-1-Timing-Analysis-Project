# Formula 1 Timing Analysis Project

The **Formula 1 Timing Analysis Project** is a Python-based application that helps analyze lap time data from Formula 1 races. With its menu-driven interface, users can load driver details, process lap times, and generate detailed reports on driver performances.

This project aims to provide a practical demonstration of data parsing, processing, and presentation techniques, making it an excellent tool for learning and Formula 1 enthusiasts.

## Features

1. **Load Driver Information**:
   - Reads driver details such as name, team, and code from a file.
2. **Process Lap Times File**:
   - Parses a file containing lap times for drivers during a race.
3. **Generate Report**:
   - Displays:
     - Race name.
     - Fastest driver and their time.
     - Overall average lap time.
     - Summary table of drivers with their fastest and average lap times, sorted by performance.
4. **Menu-Driven Interface**:
   - Interactive menu for seamless navigation and operation.

## Requirements

- Python 3.6+
- Libraries:
  - `tabulate` (for table formatting)

Install the required library using:
```bash
pip install tabulate
```

## Input Files

### Driver Information File (`f1_drivers.txt`):
- Format: `ID,Code,Name,Team`
- Example:
  ```
  1,VER,Max Verstappen,Red Bull Racing
  2,SAR,Logan Sargeant,Williams
  3,RIC,Daniel Ricciardo,RB
  ```

### Lap Times File (`lap_timesX.txt`):
- Format:
  - First line: Race location
  - Subsequent lines: Driver code followed by lap time (in seconds).
- Example:
  ```
  Dewsbury
  SAI111.875
  STR103.844
  MAG117.792
  ```

## How to Run

1. Clone this repository:
   ```bash
   https://github.com/kusiyaitkrishna/Formula-1-Timing-Analysis-Project.git
   cd Formula-1-Timing-Analysis-Project
   ```

2. Run the program:
   ```bash
   python f1_timings_board.py
   ```

3. Follow the menu to:
   - Load driver information.
   - Process lap times.
   - Generate reports.

## Example Usage

### Input:
- `f1_drivers.txt`:
  ```
  1,VER,Max Verstappen,Red Bull Racing
  2,SAR,Logan Sargeant,Williams
  ```
- `lap_times1.txt`:
  ```
  Dewsbury
  VER100.211
  SAR105.628
  ```

### Output:
```plaintext
Race Name: Dewsbury

Fastest Driver: VER (Max Verstappen) with a time of 100.211

Overall Average Time: 102.920

Driver Performance Summary:
+------+-------------------+------------------+---------------+--------------+
| Code | Name              | Team             | Fastest Time  | Average Time |
+------+-------------------+------------------+---------------+--------------+
| VER  | Max Verstappen    | Red Bull Racing | 100.211       | 100.211      |
| SAR  | Logan Sargeant    | Williams         | 105.628       | 105.628      |
+------+-------------------+------------------+---------------+--------------+
```

## Repository Structure

- `f1_timings_board.py`: Main program file.
- `f1_drivers.txt`: Sample driver information file.
- `lap_timesX.txt`: Sample lap timing files.
- `README.md`: Project documentation.

## Contributing

Feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

