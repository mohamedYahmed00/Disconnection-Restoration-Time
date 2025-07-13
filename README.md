# CSV Outbound Restore Script

This Python script helps you process a CSV file containing inbound and outbound data, identifying when outbound traffic falls below a threshold and when it is restored. It uses a simple GUI to select your CSV file and outputs dates when outbound drops below 1000, as well as when it is restored.

## Features

- Prompts you to select a CSV file using a graphical file picker.
- Reads and processes only the `Date`, `Inbound`, and `Outbound` columns.
- Replaces missing values and outbound values below 1000 with zero.
- Prints dates where outbound is zero and when it is restored.
- Clears the terminal before running for a clean output.

## Prerequisites

- Python 3.x
- Required Python packages:
  - pandas
  - tkinter (usually included with Python)
  - os (standard library)

## Installation

1. Clone this repository or download the script.
2. Install the required package (if not already installed):

    ```bash
    pip install pandas
    ```

## Usage

1. Run the script:

    ```bash
    python csv_restore_outbound.py
    ```

2. A file picker dialog will appear. Select your CSV file.
3. The script will print output to the terminal, showing dates where outbound drops to zero and when it is restored.

### Example Input CSV

```csv
Date,Inbound,Outbound
2025-07-01,1200,1500
2025-07-02,1100,900
2025-07-03,1300,0
2025-07-04,1250,1200
```

### Example Output

```
- 2025-07-02
- Restored 2025-07-04
```

## Notes

- Make sure your CSV includes the columns: `Date`, `Inbound`, and `Outbound`.
- Outbound values below 1000 are treated as zero.
- The script is cross-platform and should work on Windows, Mac, and Linux.

## License

MIT License
