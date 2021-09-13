from PySide6.QtWidgets import QMessageBox


class ConfirmDialog(QMessageBox):
    def __init__(self, windowTitle):
        super().__init__()

        self.setWindowTitle(windowTitle)
        self.setText('Are you sure?')
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def exec(self):
        return super().exec() == QMessageBox.Ok
