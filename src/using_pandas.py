import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm  
from pathlib import Path
from src.timing_decorator import measure_time

CONCURRENCY = cpu_count()

number_of_rows: int = 1_000_000_000  
chunksize: int = 50_000_000 
 
def process_chunk(chunk: pd.DataFrame) -> pd.DataFrame:
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

@measure_time
def pandas_df(csv_path: Path, number_of_rows: int, chunksize: int = chunksize) -> pd.DataFrame:
    total_chunks = number_of_rows // chunksize + (1 if number_of_rows % chunksize else 0)
    results = []

    with pd.read_csv(csv_path, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:

        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processing"):
                # Process in parallel each chunk
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    csv_path: Path = "data/measurements.txt" 

    print("Starting file processing.")
    df = pandas_df(csv_path, number_of_rows, chunksize)

    print(df.head())
