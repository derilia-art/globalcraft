import win32print
import win32api
from threading import Thread
from queue import Queue
import time

class PrinterManager:
    def __init__(self):
        self.queue = Queue()
        self.default_printer = win32print.GetDefaultPrinter()

    def list_printers(self):
        printers = [printer[2] for printer in win32print.EnumPrinters(2)]
        return printers

    def add_to_queue(self, document_path):
        print(f"Adding {document_path} to the queue.")
        self.queue.put(document_path)

    def print_document(self):
        while True:
            if not self.queue.empty():
                document_path = self.queue.get()
                print(f"Printing {document_path} on {self.default_printer}.")
                win32api.ShellExecute(
                    0,
                    "print",
                    document_path,
                    f'"/D:{self.default_printer}"',
                    ".",
                    0
                )
                self.queue.task_done()
            else:
                time.sleep(1)

    def start_printing(self):
        print_thread = Thread(target=self.print_document)
        print_thread.daemon = True
        print_thread.start()
        print("Printing process started.")

if __name__ == "__main__":
    manager = PrinterManager()
    print("Available Printers:")
    for printer in manager.list_printers():
        print(f"- {printer}")

    manager.start_printing()
    
    # Example usage
    manager.add_to_queue("C:\\path\\to\\document1.docx")
    manager.add_to_queue("C:\\path\\to\\document2.pdf")
    
    # Keeping the main thread alive
    while True:
        time.sleep(10)