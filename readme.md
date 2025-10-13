
```markdown
# Turing Machine Simulator with Multiprocessing and Threading Test

This repository contains a Python-based Turing Machine Simulator for 4-bit binary addition, integrated with a graphical user interface (GUI) using `tkinter`. Additionally, it includes a performance comparison test between multiprocessing and threading, demonstrating their execution times for a random number generation task.

## Features
- **Turing Machine Simulator**: Simulates a 4-bit binary addition using a Turing Machine with step-by-step visualization.
- **GUI Interface**: Interactive GUI to input binary numbers and step through the simulation.
- **Performance Test**: Compares multiprocessing and threading performance with configurable process/thread counts (5, 10, 50).
- **Cross-Platform**: Works on any system with Python and required dependencies.

## Prerequisites
- Python 3.x
- Required Python packages:
  - `tkinter` (usually included with Python)
  - `multiprocessing`
  - `threading`
  - `time`
  - `random`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/turing-machine-simulator.git
   cd turing-machine-simulator
   ```
2. Ensure Python is installed. Verify with:
   ```bash
   python --version
   ```
3. No additional package installation is required as all dependencies are standard Python libraries.

## Usage
1. Run the script:
   ```bash
   python turing_machine_simulator.py
   ```
2. **GUI Interaction**:
   - Enter two 4-bit binary numbers separated by `#` (e.g., `1101#1011`) in the input field.
   - Click "Start Simulation" to begin.
   - Use "Next Step" to advance through the simulation steps.
   - The tape, head position, state, carry, and log are displayed.
3. **Terminal Output**:
   - After closing the GUI, the script runs performance tests with 5, 10, and 50 processes/threads.
   - Results show completion status, execution times, and a summary comparing multiprocessing and threading.

## Sample Terminal Output
```
Multiprocessing Test - 5 processes completed:
  Process 0 (PID: 12345) finished.
  Process 1 (PID: 12346) finished.
  Process 2 (PID: 12347) finished.
  Process 3 (PID: 12348) finished.
  Process 4 (PID: 12349) finished.
Total Multiprocessing Time: 0.62 seconds

Threading Test - 5 threads completed:
  Thread 0 finished.
  Thread 1 finished.
  Thread 2 finished.
  Thread 3 finished.
  Thread 4 finished.
Total Threading Time: 1.15 seconds
Summary: Multiprocessing was faster by 0.53 seconds.

... (similar output for 10 and 50 processes/threads)
```

## File Structure
- `turing_machine_simulator.py`: Main Python script containing the simulator, GUI, and performance test.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Description of changes"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the need to demonstrate Turing Machine operations and parallel processing concepts.
- Built using standard Python libraries for accessibility.

## Contact
For questions or suggestions, please open an issue or contact the maintainer at [muhammadanshal4@gmail.com](mailto:muhammadanshal4@gmail.com).

*Last updated: 08:08 PM PKT, Monday, October 13, 2025*
```

