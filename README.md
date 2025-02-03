# GlobalCraft

GlobalCraft is a Python program designed to efficiently manage and organize printing tasks on a Windows system. It aims to streamline the printing process and reduce wait times by handling print jobs in a queued manner.

## Features

- Lists all available printers on the system.
- Adds documents to a print queue.
- Automatically prints documents from the queue using the default printer.
- Runs as a background process to continuously manage print jobs.

## Requirements

- Windows Operating System
- Python 3.x
- `pywin32` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/globalcraft.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd globalcraft
   ```

3. Install the required Python package:
   ```bash
   pip install pywin32
   ```

## Usage

1. Run the program:
   ```bash
   python globalcraft.py
   ```

2. The program will list all available printers.

3. Documents can be added to the print queue by calling the `add_to_queue` method with the document path.

4. The program will automatically handle printing in the background.

## Example

```python
manager.add_to_queue("C:\\path\\to\\document1.docx")
manager.add_to_queue("C:\\path\\to\\document2.pdf")
```

The above example adds two documents to the print queue.

## Note

- Ensure that the default printer is set correctly on your system.
- Paths to documents should be absolute paths.
- The script must run with permissions to access printers and files.

## License

This project is licensed under the MIT License - see the LICENSE file for more details.