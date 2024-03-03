## One Billion Rows Challenge 

This repository represents Project 01 from the Data Engineering BOOTCAMP, where the objective is to compare different ways of reading one billion rows in Python. Upon cloning the original repository, the objective is to implement script modifications based on the concepts learned in previous bootcamp classes, such as type hints and functions.

From the original repository, a decorator function was implemented to measure the execution time of each script function responsible for reading the file. Minor structural adjustments, such as introducing a type hint in the path variable, were made to the scripts. Additionally, the Dask script was intentionally excluded, narrowing the comparison to Python (native structure), Pandas, Polars, and DuckDB.

### Results

Machine specifications:
* 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz  2.42 GHz
* 16G RAM

|           Enviroment    | Execution Time   |
|-------------------|------------------:|
| Python            |      2797.19 s    |
| Python + Pandas   |       396.06 s    |
| Python + Polars   |        38.16 s    |
| Python + Duckdb   |        33.43 s    |


### How To Run

How to execute this repository in a bash terminal using `pyenv` and `poetry`.

Before you begin, ensure that *measurements.txt* is inside `.gitignore`

1. Clone the repository:
```bash
git clone https://github.com/lealre/one-billion-rows-challenge.git
```
 2. Enter the folder:
 ```bash
 cd one-billion-rows-challenge
 ```

3. Set Python version using pyenv:
```bash
pyenv local 3.12.1
```

4. Set poetry to use Python 3.12.1:
```bash
poetry env use 3.12.1
``` 

5. Install dependencies and activate the virtual environment:
```bash
poetry install --no-root
```
```bash
poetry lock --no-update
```
```bash
poetry shell
```

6. Create the *measurements.txt* file (takes some time to create):
```bash
python src/create_measurements.py
```

7. Read the file using specific script:
```bash
python src/using_python.py 
```
```bash
python src/using_pandas.py 
```
```bash
python src/using_polars.py 
```
```bash
python src/using_duckdb.py 
```

--------------
THIS IS A CLONE FROM [THIS REPO](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python)! The scripts designed to read the file are not authored by me.
