from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QScrollArea, QHBoxLayout, QFileDialog
import sys


def generate_fibonacci(n):
    if n <= 0:
        return []
    fib_series = [0, 1]
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]


class FibonacciApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Fibonacci Generator")
        self.setGeometry(100, 100, 600, 500)

        self.layout = QVBoxLayout()

        self.label = QLabel("Enter Range for Fibonacci Series:")
        self.layout.addWidget(self.label)

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Enter a positive integer")
        self.layout.addWidget(self.entry)

        button_layout = QHBoxLayout()

        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.on_generate)
        button_layout.addWidget(self.generate_btn)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_output)
        button_layout.addWidget(self.clear_btn)

        self.layout.addLayout(button_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.result_label = QLabel("", self)
        self.result_label.setWordWrap(True)
        self.scroll_area.setWidget(self.result_label)
        self.layout.addWidget(self.scroll_area)

        button_layout_2 = QHBoxLayout()

        self.save_btn = QPushButton("Save to File")
        self.save_btn.clicked.connect(self.save_to_file)
        button_layout_2.addWidget(self.save_btn)

        self.load_btn = QPushButton("Load from File")
        self.load_btn.clicked.connect(self.load_from_file)
        button_layout_2.addWidget(self.load_btn)

        self.layout.addLayout(button_layout_2)

        self.setLayout(self.layout)

    def on_generate(self):
        try:
            n = int(self.entry.text())
            if n <= 0:
                QMessageBox.critical(
                    self, "Error", "Please enter a positive integer")
                return

            fib_series = generate_fibonacci(n)
            self.result_label.setText(
                "Fibonacci Series:\n" + ', '.join(map(str, fib_series)))
        except ValueError:
            QMessageBox.critical(
                self, "Error", "Invalid input! Please enter a number.")

    def save_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "fibonacci_series.txt", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.result_label.text())
                QMessageBox.information(
                    self, "Success", "Fibonacci series saved successfully!")
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to save file: {str(e)}")

    def load_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.result_label.setText(file.read())
                QMessageBox.information(
                    self, "Success", "Fibonacci series loaded successfully!")
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load file: {str(e)}")

    def clear_output(self):
        self.result_label.setText("")
        self.entry.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FibonacciApp()
    window.show()
    sys.exit(app.exec())
