# Online Hash Algorithms

This project implements various online hash algorithms, including MD5, SHA-256, and MurmurHash3. It provides a user interface to get input data and display the computed hash values. Additionally, it includes performance analysis to measure the execution time of different hash algorithms.

## Prerequisites

- Python 3.x
- Required Python packages listed in `requirements.txt`

## Installation

1. Install the required packages:
pip install -r requirements.txt

## Usage

To run the project, execute the following command:
python src/main.py

This will start the user interface. You can enter input data, and the program will display the computed hash values using different algorithms. To exit the program, enter `exit`.

After exiting the user interface, the program will perform a performance analysis on a sample input data and display the execution time for each hash algorithm.

## Testing

The project includes unit tests for each hash algorithm implementation. To run the tests, execute the following command:

python -m unittest tests/test_md5.py
python -m unittest tests/test_sha256.py
python -m unittest tests/test_murmur3.py

This will run all the test cases in the `tests` directory.

## Project Structure
online-hash-algorithms/
├── src/
│   ├── hash_algorithms/
│   │   ├── md5.py
│   │   ├── sha256.py
│   │   └── murmur3.py
│   ├── user_interface.py
│   ├── performance_analysis.py
│   └── main.py
├── tests/
│   ├── test_md5.py
│   ├── test_sha256.py
│   └── test_murmur3.py
├── README.md
└── requirements.txt

- `src/hash_algorithms/`: Contains the implementations of different hash algorithms
- `src/user_interface.py`: Handles user input and displays computed hash values
- `src/performance_analysis.py`: Measures and analyzes the execution time of hash algorithms
- `src/main.py`: The main entry point of the program
- `tests/`: Contains unit tests for each hash algorithm implementation
- `README.md`: This file
- `requirements.txt`: List of required Python packages

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
