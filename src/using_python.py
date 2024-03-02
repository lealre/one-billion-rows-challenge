from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # progress bar
from pathlib import Path
from src.timing_decorator import measure_time

NUMBER_OF_ROWS = 1_000_000_000

@measure_time
def python_csv_module(csv_path: Path) -> dict:
    # using positive and negative infinity to compare
    minimums = defaultdict(lambda: float('inf'))
    maxims = defaultdict(lambda: float('-inf'))
    sums = defaultdict(float)
    measurements = Counter()

    with open(csv_path, 'r') as file:
        _reader = reader(file, delimiter=';')
        for row in tqdm(_reader, total=NUMBER_OF_ROWS, desc="Processing"):
            station_name, temperature = str(row[0]), float(row[1])
            measurements.update([station_name])
            minimums[station_name] = min(minimums[station_name], temperature)
            maxims[station_name] = max(maxims[station_name], temperature)
            sums[station_name] += temperature

    print("Data is loaded. Calculating statistics...")

    results = {}
    for station, measurements_quantity in measurements.items():
        mean_temp = sums[station] / measurements_quantity
        results[station] = (minimums[station], mean_temp, maxims[station])

    print("Statistics calculated. Ordering data...")

    sorted_results = dict(sorted(results.items()))

    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":

    csv_path: Path = "data/measurements.txt"

    print("Starting file processing.")

    resultados = python_csv_module(csv_path)

    for station, metrics in resultados.items():
        print(station, metrics, sep=': ')