# DAA + ML Practical Exam Kit

## How to run

### DAA (C++)
1. Open the `DAA_CPP` folder in VS Code.
2. Open a `.cpp` file.
3. Compile in the terminal (with g++ installed): `g++ filename.cpp -o run`
4. Run: macOS/Linux `./run`; Windows `run.exe`.
5. For `07_matrix_multiplication_threads.cpp`, compile with `g++ 07_matrix_multiplication_threads.cpp -o run -pthread`.

### ML (Python)
1. Install Python 3 and VS Code Python extension.
2. Open `ML_Python` folder.
3. In terminal run: `python -m pip install pandas numpy matplotlib scikit-learn`
4. For the bank neural network, scikit-learn's `MLPClassifier` is used so it is lighter/easier to set up than TensorFlow.
5. Put the required CSV beside its Python script and run `python filename.py`.

## Dataset filenames expected
- Uber: `uber.csv` (must have fare_amount, pickup/drop latitude/longitude, passenger_count)
- Email spam: `emails.csv` (last column label; first column assumed ID and dropped)
- Bank churn: `Churn_Modelling.csv` (target `Exited`)
- Diabetes: `diabetes.csv` (target `Outcome`)
- Sales: `sales_data_sample.csv` (Latin-1 encoding handled)

Download datasets from the links in your lab manual. If the column names differ, update the filename/column names in the first few lines of the relevant script.

## Memory hooks
- Fibonacci: base case, then previous two values.
- Huffman: repeatedly combine the two smallest frequencies.
- Fractional knapsack: sort by value/weight, take as much as possible.
- 0/1 knapsack: DP table; each item is either taken or not.
- N-Queens: place row by row; check column and diagonals; backtrack.
- Quick sort: partition around pivot, sort both sides.
- Uber regression: clean -> distance -> split -> fit two models -> R2/RMSE.
- Spam/diabetes: X/y -> split -> scale -> fit -> predict -> metrics.
- Churn ANN: drop IDs -> encode categories -> split -> scale -> train neural network -> accuracy/confusion matrix.
- Sales clustering: scale -> elbow inertia -> KMeans -> cluster labels.

Important: results depend on the exact dataset and preprocessing. Do not memorise fabricated accuracy values; run the code and report the output you actually get.
