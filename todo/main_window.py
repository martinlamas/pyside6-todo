from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMenu,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QWidget
)
from todo.confirm_dialog import ConfirmDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Todo List')
        self.setWindowIcon(QIcon('icon.png'))
        self.setMinimumSize(600, 400)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.buildMenuBar()
        self.buildWindowContent()

    def buildMenuBar(self):
        menuBar = QMenuBar()

        fileMenu = QMenu('&File')
        fileMenu.addAction('&Close').triggered.connect(self.close)

        helpMenu = QMenu('&Help')
        helpMenu.addAction('&About').triggered.connect(self.about)

        menuBar.addMenu(fileMenu)
        menuBar.addMenu(helpMenu)

        self.layout.setMenuBar(menuBar)

    def about(self):
        aboutMsgBox = QMessageBox()
        aboutMsgBox.setWindowTitle('Todo List')
        aboutMsgBox.setText('Todo List v0.0.1')
        aboutMsgBox.exec()

    def buildWindowContent(self):
        self.layout.addWidget(QLabel('Enter task:'), 0, 0)

        self.taskEdit = QTextEdit()
        self.taskEdit.textChanged.connect(self.taskChanged)
        self.layout.addWidget(self.taskEdit, 1, 0)

        self.addTaskButton = QPushButton('Add task')
        self.addTaskButton.setDisabled(True)
        self.addTaskButton.clicked.connect(self.addTask)
        self.layout.addWidget(self.addTaskButton, 2, 0)

        self.deleteTaskButton = QPushButton('Delete task')
        self.deleteTaskButton.setDisabled(True)
        self.deleteTaskButton.clicked.connect(self.deleteTask)
        self.layout.addWidget(self.deleteTaskButton, 3, 0)

        self.deleteAllTasksButton = QPushButton('Delete all tasks')
        self.deleteAllTasksButton.clicked.connect(self.deleteAllTasks)
        self.layout.addWidget(self.deleteAllTasksButton, 4, 0)

        self.layout.addWidget(QLabel('Task list:'), 0, 1)

        self.taskList = QListWidget()
        self.taskList.currentItemChanged.connect(
            self.taskListCurrentItemChanged)
        self.layout.addWidget(self.taskList, 1, 1, 4, 1)

    def addTask(self):
        task = self.taskEdit.toPlainText().strip()

        if task:
            taskItem = QListWidgetItem()
            taskItem.setFlags(
                Qt.ItemIsEnabled |
                Qt.ItemIsUserCheckable |
                Qt.ItemIsSelectable
            )
            taskItem.setCheckState(Qt.Unchecked)
            taskItem.setText(task)

            self.taskList.addItem(taskItem)
            self.taskEdit.clear()

    def deleteTask(self):
        self.taskList.takeItem(self.taskList.row(self.taskList.currentItem()))

    def deleteAllTasks(self):
        confirmDialog = ConfirmDialog('Delete all tasks')

        if confirmDialog.exec():
            self.taskList.clear()

    def taskChanged(self):
        self.addTaskButton.setDisabled(not self.taskEdit.toPlainText().strip())

    def taskListCurrentItemChanged(self, current):
        self.deleteTaskButton.setDisabled(current is None)
