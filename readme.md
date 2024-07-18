# Espresso Percolation Optimizer Based on Percolation Theory

This Python script is designed to help you determine the optimal grind size for brewing espresso by leveraging concepts from percolation theory. It allows you to input trial data from different grind sizes and outputs the optimal grind size based on extraction yield and uniform water percolation.

## Suggested Listening

"Don't need no hateration, holleration
In this dancery
Let's get it perculatin' while you're waiting
So just dance for me"
- [Mary J. Blige](https://open.spotify.com/track/3aw9iWUQ3VrPQltgwvN9Xu?si=9a2f66bf7e974aba)


## Requirements

- Python 3.x
- NumPy library

## Installation

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install NumPy**: You can install the NumPy library using pip:
   ```sh
   pip install numpy
   ```

## Usage

### Step 1: Perform Trials

1. **Brew Espresso**: Perform a series of espresso brewing trials with different grind sizes. For each trial, measure and record the following data:
   - Grind size (in microns)
   - Flow rate (in ml/s)
   - Extraction time (in seconds)
   - Yield (in ml)
   - TDS (Total Dissolved Solids, in %)

2. **Record Data**: Note down the data for each trial.

### Step 2: Modify the Script

1. **Download the Script**: Save the Python script `espresso_optimizer.py` provided below to your local machine.

2. **Enter Trial Data**: Modify the `trials` list in the script to include your recorded trial data.

### Step 3: Run the Script

1. **Navigate to Script Location**: Open your terminal or command prompt and navigate to the directory where you saved the script.

2. **Run the Script**: Execute the script using the following command:
   ```sh
   python espresso_optimizer.py
   ```

### Step 4: View Results

The script will output the optimal grind size and whether it achieves uniform percolation.