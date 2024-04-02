import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor, QLinearGradient, QBrush

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.layout = QVBoxLayout()
        self.background_label = QLabel()
        self.layout.addWidget(self.background_label)
        self.data_panel = QWidget()
        self.data_panel_layout = QVBoxLayout()
        self.data_panel.setLayout(self.data_panel_layout)
        self.layout.addWidget(self.data_panel)
        self.task_list = QListWidget()
        self.data_panel_layout.addWidget(self.task_list)
        self.bottom_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.bottom_layout.addWidget(self.task_input)
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.bottom_layout.addWidget(self.add_button)
        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.bottom_layout.addWidget(self.delete_button)
        self.data_panel_layout.addLayout(self.bottom_layout)
        self.setLayout(self.layout)
        

        # 
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#87CEEB")) # Light blue
        gradient.setColorAt(1, QColor("#98FB98")) # Light green
        p = self.data_panel.palette()
        p.setBrush(self.backgroundRole(), QBrush(gradient))
        self.data_panel.setAutoFillBackground(True)
        self.data_panel.setPalette(p)
        
        self.load_tasks()
        
    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task.")
    
    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to delete.")
    
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for i in range(self.task_list.count()):
                f.write(self.task_list.item(i).text() + "\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    self.task_list.addItem(task.strip())
        except FileNotFoundError:
            pass

def main():
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()