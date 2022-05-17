from PyQt5.QtCore import QThread, pyqtSignal


class Time(QThread):
    time_signal = pyqtSignal(int)

    def __init__(self, args):
        QThread.__init__(self)
        self.args = args

    def run(self):
        cnt = 30
        while True:
            if self.args.gui.flagreset == True:
                cnt = 30
                self.args.gui.flagreset = False
            cnt -= 1
            while True:
                if self.args.gui.flagstop == 2 or self.args.gui.flagstop == 0:
                    break
            if cnt >= 0:
                self.time_signal.emit(cnt)
            QThread.sleep(1)
