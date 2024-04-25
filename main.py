import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QTableView, QHeaderView, QLabel
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem, QPixmap
import pyqtgraph as pg
from PyQt6.QtCore import Qt, QTime, QTimer, QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(900)
        self.setFixedWidth(1720)
        self.move(100, 50)  # Pencereyi (100, 50) konumunda başlatır

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Turkish Defenders Ground Station Interface')

        # Bağlantı elemanları
        self.StartConnectionButton = QPushButton('Bağlan', self)
        self.StartConnectionButton.setGeometry(70, 25, 130, 32)
        self.StartConnectionButton.setFont(QFont("Times New Roman", 12))

        self.StopConnectionButton = QPushButton('Bağlantıyı Durdur', self)
        self.StopConnectionButton.setGeometry(210, 25, 130, 32)
        self.StopConnectionButton.setFont(QFont("Times New Roman", 12))

        self.SdKartYazdirmaBaslatButton = QPushButton('SD Kayıt Başlat', self)
        self.SdKartYazdirmaBaslatButton.setGeometry(55, 115, 145, 32)
        self.SdKartYazdirmaBaslatButton.setFont(QFont("Times New Roman", 12))

        self.SdKartYazdirmaDurdurButton = QPushButton('SD Kayıt Durdur', self)
        self.SdKartYazdirmaDurdurButton.setGeometry(210, 115, 145, 32)
        self.SdKartYazdirmaDurdurButton.setFont(QFont("Times New Roman", 12))

        self.clearTableButton = QPushButton('Temizle', self)
        self.clearTableButton.setGeometry(1330, 850, 70, 32)
        self.clearTableButton.setFont(QFont("Times New Roman", 12))

        self.IotTransferBaslatButton = QPushButton('IoT Transfer Başlat', self)
        self.IotTransferBaslatButton.setGeometry(400, 115, 180, 32)
        self.IotTransferBaslatButton.setFont(QFont("Times New Roman", 12))

        self.IotTransferBaslatButton = QPushButton('IoT Transfer Durdur', self)
        self.IotTransferBaslatButton.setGeometry(600, 115, 180, 32)
        self.IotTransferBaslatButton.setFont(QFont("Times New Roman", 12))

        self.MekanikFiltreKodGonder = QPushButton('Kodu Gönder', self)
        self.MekanikFiltreKodGonder.setGeometry(1530, 90, 130, 32)
        self.MekanikFiltreKodGonder.setFont(QFont("Times New Roman", 12))

        # Selector
        self.ComSelector = QComboBox(self)
        self.ComSelector.setGeometry(70, 70, 130, 32)
        self.ComSelector.addItem("COM1")
        self.ComSelector.addItem("COM2")
        self.ComSelector.setFont(QFont("Times New Roman", 12))

        self.BaudSelector = QComboBox(self)
        self.BaudSelector.setGeometry(210, 70, 130, 32)
        self.BaudSelector.addItem("9600")
        self.BaudSelector.addItem("115200")
        self.BaudSelector.setFont(QFont("Times New Roman", 12))

        self.FirstTimeSelector = QComboBox(self)
        self.FirstTimeSelector.setGeometry(1520, 50, 40, 32)
        self.FirstTimeSelector.addItem("1")
        self.FirstTimeSelector.addItem("2")
        self.FirstTimeSelector.setFont(QFont("Times New Roman", 12))

        self.FirstColorSelector = QComboBox(self)
        self.FirstColorSelector.setGeometry(1560, 50, 40, 32)
        self.FirstColorSelector.addItem("R")
        self.FirstColorSelector.addItem("G")
        self.FirstColorSelector.setFont(QFont("Times New Roman", 12))

        self.SecondTimeSelector = QComboBox(self)
        self.SecondTimeSelector.setGeometry(1600, 50, 40, 32)
        self.SecondTimeSelector.addItem("1")
        self.SecondTimeSelector.addItem("2")
        self.SecondTimeSelector.setFont(QFont("Times New Roman", 12))

        self.SecondColorSelector = QComboBox(self)
        self.SecondColorSelector.setGeometry(1640, 50, 40, 32)
        self.SecondColorSelector.addItem("R")
        self.SecondColorSelector.addItem("G")
        self.SecondColorSelector.setFont(QFont("Times New Roman", 12))
        

        # Label
        MissionTimeString = "Mission Time: "
        self.MissionTimeLabel = QLabel(self)
        self.MissionTimeLabel.setGeometry(470, 25, 260, 30)
        self.MissionTimeLabel.setFont(QFont('Arial', 12))
        self.MissionTimeLabel.setText(MissionTimeString + "00:00:00")
        self.MissionTimeLabel.setStyleSheet("background-color: white")

        IrtifaFarkiString = "İrtifa Farkı: "
        self.IrtifaFarkiLabel = QLabel(self)
        self.IrtifaFarkiLabel.setGeometry(510, 70, 180, 30)
        self.IrtifaFarkiLabel.setFont(QFont('Arial', 12))
        self.IrtifaFarkiLabel.setText(IrtifaFarkiString + "00 m")
        self.IrtifaFarkiLabel.setStyleSheet("background-color: white")

        MekanikFiltrelemeString = "Mekanik Filtreleme"
        self.MekanikFiltrelemeLabel = QLabel(self)
        self.MekanikFiltrelemeLabel.setGeometry(1515, 10, 180, 30)
        self.MekanikFiltrelemeLabel.setFont(QFont('Arial', 12))
        self.MekanikFiltrelemeLabel.setText(MekanikFiltrelemeString)
        self.MekanikFiltrelemeLabel.setStyleSheet("background-color: white")

        # Tablo
        self.dataTable = QTableView(self)
        self.dataTable.setGeometry(20, 650, 1300, 230)
        self.setup_table()

        # Resimler
        LogoImage_PixMap = QPixmap("Taslak\Logo-Image.png")
        LogoImage_Label = QLabel(self)
        LogoImage_Label.setPixmap(LogoImage_PixMap)
        LogoImage_Label.setGeometry(850, 20, LogoImage_PixMap.width(), LogoImage_PixMap.height())

        MapImage_PixMap = QPixmap("Taslak/Map-Image.png")
        MapImage_Label = QLabel(self)
        MapImage_Label.setPixmap(MapImage_PixMap)
        MapImage_Label.setGeometry(1420, 580, MapImage_PixMap.width()-30, MapImage_PixMap.height()-30)

        AxisImage_PixMap = QPixmap("Taslak\Eksen-Image.png")
        AxisImage_Label = QLabel(self)
        AxisImage_Label.setPixmap(AxisImage_PixMap)
        AxisImage_Label.setGeometry(1000, 0, AxisImage_PixMap.width(), AxisImage_PixMap.height())

        CameraImage_PixMap = QPixmap("Taslak\Camera-Image.png")
        CameraImage_Label = QLabel(self)
        CameraImage_Label.setPixmap(CameraImage_PixMap)
        CameraImage_Label.setGeometry(1440, 200, CameraImage_PixMap.width(), CameraImage_PixMap.height())

        # Plot
        self.AltitudePlot = pg.PlotWidget(self)
        self.AltitudePlot.setGeometry(50, 240, 270, 180)

        self.asd = pg.PlotWidget(self)
        self.asd.setGeometry(350, 240, 270, 180)

        self.qwe = pg.PlotWidget(self)
        self.qwe.setGeometry(650, 240, 270, 180)

        self.ghj = pg.PlotWidget(self)
        self.ghj.setGeometry(950, 240, 270, 180)

        self.xcv = pg.PlotWidget(self)
        self.xcv.setGeometry(50, 450, 270, 180)

        self.ghf = pg.PlotWidget(self)
        self.ghf.setGeometry(350, 450, 270, 180)

        self.bnm = pg.PlotWidget(self)
        self.bnm.setGeometry(650, 450, 270, 180)

        self.dfg = pg.PlotWidget(self)
        self.dfg.setGeometry(950, 450, 270, 180)
        

    def setup_table(self):
        model = QStandardItemModel(7, 22)
        model.setHorizontalHeaderLabels([f"Kolon {i}" for i in range(1, 23)])
        model.setVerticalHeaderLabels([f"Satır {i}" for i in range(1, 8)])

        self.dataTable.setModel(model)
        self.dataTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
