import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel, QCheckBox, QFrame, QAbstractItemView, QTableWidgetItem
from PyQt6.QtGui import QFont, QPixmap, QIcon, QColor
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtWidgets
from random import randint

TELEMETRY_TYPES_COLUMNS_NAMES = ["PaketNo", "Statü", "HataKodu", "Gönd Saati", "BAS1", "BAS2", "YÜK1",  "YÜK2", "İrtifa Fark", "İnişHızı", "Sıcaklık", "PilGer",
                                  "GPSLat", "GPSLong", "GPSAlt", "Pitch", "Roll", "Yaw", "RHRH", "IoTData", "TakımNo"]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(970)
        self.setFixedWidth(1880)
        self.move(20, 10)

        self.setWindowIcon(QIcon("Taslak\Logo-Icon.ico"))
        self.setStyleSheet("background-color: #10454F;")  # Arka plan rengini ayarla

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Turkish Defenders Ground Station Interface')

        self.InfoFrame = QFrame(self)
        self.InfoFrame.setGeometry(405, 20, 380, 70)
        self.InfoFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 10px;")

        # Progress bar oluştur
        self.progressBar = QtWidgets.QProgressBar(self.InfoFrame)
        self.progressBar.setGeometry(20, 10, 340, 20)
        self.progressBar.setProperty("value", 34)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(60)
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        self.progressBar.setTextVisible(False)

        # İlk label oluştur
        self.label1 = QLabel(self.InfoFrame)
        self.label1.setGeometry(20, 40, 120, 20)
        self.label1.setText("  Pil Yüzde: % 62")
        self.label1.setFont(QFont("Arial", 10))
        self.label1.setStyleSheet("background-color: #A3AB78;")

        # İkinci label oluştur
        kalanSure = " 15 Saat 32 Dakika"
        self.label2 = QLabel(self.InfoFrame)
        self.label2.setGeometry(160, 40, 205, 20)
        self.label2.setText("Kalan Süre: {}".format(kalanSure))
        self.label2.setFont(QFont("Arial", 10))
        self.label2.setStyleSheet("background-color: #A3AB78;")

        # ----------------------------------------------------------------------------------------------------------
        self.ConnectionFrame = QFrame(self)
        self.ConnectionFrame.setGeometry(55, 30, 310, 150)
        self.ConnectionFrame.setStyleSheet("background-color: #506266; border: 2px solid #506266; border-radius: 5px;")

        self.ManuelAyirmaKitlemeFrame = QFrame(self)
        self.ManuelAyirmaKitlemeFrame.setGeometry(55, 185, 310, 52)
        self.ManuelAyirmaKitlemeFrame.setStyleSheet("background-color: #506266; border: 2px solid #506266; border-radius: 5px;")

        self.MissionIrtifaFrame = QFrame(self)
        self.MissionIrtifaFrame.setGeometry(470, 100, 260, 95)
        self.MissionIrtifaFrame.setStyleSheet("background-color: #506266; border: 1px solid #506266; border-radius: 5px; padding: 5px;")

        self.IotTransferFrame = QFrame(self)
        self.IotTransferFrame.setGeometry(405, 210, 380, 50)
        self.IotTransferFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 10px;")

        self.logoCloseFrame = QFrame(self)
        self.logoCloseFrame.setGeometry(830, 15, 205, 200)
        self.logoCloseFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 10px;")

        self.GorevDurumuFrame = QFrame(self)
        self.GorevDurumuFrame.setGeometry(1070, 15, 200, 220)
        self.GorevDurumuFrame.setStyleSheet("background-color: #506266; border-radius: 5px; border: 1px solid #ccc;")

        self.ArayuzAlarmFrame = QFrame(self)
        self.ArayuzAlarmFrame.setGeometry(1300, 15, 220, 190)
        self.ArayuzAlarmFrame.setStyleSheet("background-color: #506266; border-radius: 5px; border: 1px solid #ccc;")

        self.MekanikFiltreFrame = QFrame(self)
        self.MekanikFiltreFrame.setGeometry(1590, 15, 250, 135)
        self.MekanikFiltreFrame.setStyleSheet("background-color: #506266; border-radius: 5px; border: 1px solid #ccc;")

        self.PlotFrame = QFrame(self)
        self.PlotFrame.setGeometry(20, 270, 1210, 420)
        self.PlotFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 5px;")

        self.eksenFrame = QFrame(self)
        self.eksenFrame.setGeometry(1260, 290, 270, 390)
        self.eksenFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 10px;")

        self.CameraFrame = QFrame(self)
        self.CameraFrame.setGeometry(1560, 180, 310, 460)
        self.CameraFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 5px;")

        self.TableFrame = QFrame(self)
        self.TableFrame.setGeometry(20, 710, 1510, 250)
        self.TableFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 5px;")
        
        self.mapFrame = QFrame(self)
        self.mapFrame.setGeometry(1560, 660, 310, 300)
        self.mapFrame.setStyleSheet("background-color: #506266; border: 2px solid #ccc; border-radius: 10px;")
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        LogoImage_PixMap = QPixmap("Taslak\logo.png")
        LogoImage_Label = QLabel(self.logoCloseFrame)
        LogoImage_Label.setPixmap(LogoImage_PixMap)
        LogoImage_Label.setGeometry(45, 20, 120, 112)
        
        print("logo " , LogoImage_PixMap.width() + 26, LogoImage_PixMap.height() + 20)
        
        CloseProgramButton = QPushButton('Programı Sonlandır', self.logoCloseFrame)
        CloseProgramButton.setGeometry(20, 155, 166, 32)
        CloseProgramButton.setFont(QFont("Times New Roman", 12))
        CloseProgramButton.setStyleSheet("""
            QPushButton {
                background-color: #ff4500; /* Koyu turuncu */
                border: 2px solid #ff4500;
                border-radius: 10px;
                color: white;
            }
            QPushButton:hover {
                background-color: #ff6347; /* Turuncu */
                border: 2px solid #ff6347;
            }
            QPushButton:pressed {
                background-color: #b22222; /* Koyu kırmızı */
                border: 2px solid #b22222;
            }
        """)
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        self.StartConnectionButton = QPushButton('Bağlantıyı Başlat', self.ConnectionFrame)
        self.StartConnectionButton.setGeometry(20, 15, 130, 32)
        self.StartConnectionButton.setFont(QFont("Times New Roman", 12))
        self.StartConnectionButton.setStyleSheet("background-color: #2ecc71; color: white; border-radius: 5px;")

        self.StopConnectionButton = QPushButton('Bağlantıyı Durdur', self.ConnectionFrame)
        self.StopConnectionButton.setGeometry(160, 15, 130, 32)
        self.StopConnectionButton.setFont(QFont("Times New Roman", 12))
        self.StopConnectionButton.setStyleSheet("background-color: #e74c3c; color: white; border-radius: 5px;")

        self.ComSelector = QComboBox(self.ConnectionFrame)
        self.ComSelector.setGeometry(20, 60, 130, 32)
        self.ComSelector.addItem("COM1")
        self.ComSelector.addItem("COM2")
        self.ComSelector.setFont(QFont("Times New Roman", 12))
        self.ComSelector.setStyleSheet("background-color: #818274; color: white; border-radius: 5px;")

        self.BaudSelector = QComboBox(self.ConnectionFrame)
        self.BaudSelector.setGeometry(160, 60, 130, 32)
        self.BaudSelector.addItem("9600")
        self.BaudSelector.addItem("115200")
        self.BaudSelector.setFont(QFont("Times New Roman", 12))
        self.BaudSelector.setStyleSheet("background-color: #818274; color: white; border-radius: 5px;")

        self.SdKartYazdirmaBaslatButton = QPushButton('SD Kayıt Başlat', self.ConnectionFrame)
        self.SdKartYazdirmaBaslatButton.setGeometry(20, 105, 130, 32)
        self.SdKartYazdirmaBaslatButton.setFont(QFont("Times New Roman", 12))
        self.SdKartYazdirmaBaslatButton.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px;")

        self.SdKartYazdirmaDurdurButton = QPushButton('SD Kayıt Durdur', self.ConnectionFrame)
        self.SdKartYazdirmaDurdurButton.setGeometry(160, 105, 130, 32)
        self.SdKartYazdirmaDurdurButton.setFont(QFont("Times New Roman", 12))
        self.SdKartYazdirmaDurdurButton.setStyleSheet("background-color: #e67e22; color: white; border-radius: 5px;")
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        self.ManuelAyirButton = QPushButton('Manuel Ayır', self.ManuelAyirmaKitlemeFrame)
        self.ManuelAyirButton.setGeometry(15, 10, 125, 32)
        self.ManuelAyirButton.setFont(QFont("Times New Roman", 12))
        self.ManuelAyirButton.setStyleSheet("background-color: green; border: none; border-radius: 5px; color: black;")

        self.ManuelKitleButton = QPushButton('Manuel Kitle', self.ManuelAyirmaKitlemeFrame)
        self.ManuelKitleButton.setGeometry(150, 10, 145, 32)
        self.ManuelKitleButton.setFont(QFont("Times New Roman", 12))
        self.ManuelKitleButton.setStyleSheet("background-color: red; border: none; border-radius: 5px; color: black;")
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        self.IotTransferBaslatButton = QPushButton('IoT Transfer Başlat', self.IotTransferFrame)
        self.IotTransferBaslatButton.setGeometry(10, 10, 160, 30)
        self.IotTransferBaslatButton.setFont(QFont("Times New Roman", 12))
        self.IotTransferBaslatButton.setStyleSheet("background-color: #7fbf7f; border: 2px solid #506266; border-radius: 5px;")

        self.IotTransferDurdurButton = QPushButton('IoT Transfer Durdur', self.IotTransferFrame)
        self.IotTransferDurdurButton.setGeometry(210, 10, 160, 30)
        self.IotTransferDurdurButton.setFont(QFont("Times New Roman", 12))
        self.IotTransferDurdurButton.setStyleSheet("background-color: #ff7f7f; border: 2px solid #506266; border-radius: 5px;")
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        self.MekanikFiltrelemeLabel = QLabel(self.MekanikFiltreFrame)
        self.MekanikFiltrelemeLabel.setGeometry(33, 10, 180, 30)
        self.MekanikFiltrelemeLabel.setFont(QFont('Arial', 15))
        self.MekanikFiltrelemeLabel.setText("Mekanik Filtreleme")
        self.MekanikFiltrelemeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        style3 = """
        QLabel {
            border-radius: 5px;
            border: 0px solid #ccc; /* Gri kenarlık */
            padding: 5px; /* Kenar boşluğu */
            color: #333; /* Koyu gri metin */
        }
        """
        self.MekanikFiltrelemeLabel.setStyleSheet(style3)

        self.FirstTimeSelector = QComboBox(self.MekanikFiltreFrame)
        self.FirstTimeSelector.setGeometry(10, 50, 50, 32)
        self.FirstTimeSelector.addItem("1")
        self.FirstTimeSelector.addItem("2")
        self.FirstTimeSelector.setFont(QFont("Times New Roman", 12))
        self.FirstTimeSelector.setStyleSheet("background-color: #818274;")

        self.FirstColorSelector = QComboBox(self.MekanikFiltreFrame)
        self.FirstColorSelector.setGeometry(65, 50, 50, 32)
        self.FirstColorSelector.addItem("R")
        self.FirstColorSelector.addItem("G")
        self.FirstColorSelector.setFont(QFont("Times New Roman", 12))
        self.FirstColorSelector.setStyleSheet("background-color: #818274;")

        self.SecondTimeSelector = QComboBox(self.MekanikFiltreFrame)
        self.SecondTimeSelector.setGeometry(135, 50, 50, 32)
        self.SecondTimeSelector.addItem("1")
        self.SecondTimeSelector.addItem("2")
        self.SecondTimeSelector.setFont(QFont("Times New Roman", 12))
        self.SecondTimeSelector.setStyleSheet("background-color: #818274;")

        self.SecondColorSelector = QComboBox(self.MekanikFiltreFrame)
        self.SecondColorSelector.setGeometry(190, 50, 50, 32)
        self.SecondColorSelector.addItem("R")
        self.SecondColorSelector.addItem("G")
        self.SecondColorSelector.setFont(QFont("Times New Roman", 12))
        self.SecondColorSelector.setStyleSheet("background-color: #818274;")

        self.MekanikFiltreKodGonder = QPushButton('Kodu Gönder', self.MekanikFiltreFrame)
        self.MekanikFiltreKodGonder.setGeometry(10, 90, 230, 32)
        self.MekanikFiltreKodGonder.setFont(QFont("Times New Roman", 12))

        style = """
        QPushButton {
            background-color: green; /* Açık gri arka plan */
            border: 0px solid #c0c0c0; /* Açık gri kenarlık */
            border-radius: 5px; /* Köşeleri yuvarlat */
            color: white; /* Turuncu metin */
        }
        QPushButton:hover {
            background-color: #c0c0c0; /* Hover rengi */
        }
        """
        self.MekanikFiltreKodGonder.setStyleSheet(style)
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        MissionTimeString = "Görev Zamanı: "
        self.MissionTimeLabel = QLabel(self.MissionIrtifaFrame)
        self.MissionTimeLabel.setGeometry(10, 10, 240, 30)
        self.MissionTimeLabel.setFont(QFont('Arial', 12))
        self.MissionTimeLabel.setText(MissionTimeString + "00:00:00")
        self.MissionTimeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.MissionTimeLabel.setStyleSheet("background-color: #A3AB78; border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        IrtifaFarkiString = "İrtifa Farkı: "
        self.IrtifaFarkiLabel = QLabel(self.MissionIrtifaFrame)
        self.IrtifaFarkiLabel.setGeometry(10, 55, 240, 30)
        self.IrtifaFarkiLabel.setFont(QFont('Arial', 12))
        self.IrtifaFarkiLabel.setText(IrtifaFarkiString + "00 m")
        self.IrtifaFarkiLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.IrtifaFarkiLabel.setStyleSheet("background-color: #A3AB78; border: 1px solid #ccc; border-radius: 5px; padding: 5px;")
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        x = 16
        self.progressBar = QtWidgets.QProgressBar(self.GorevDurumuFrame)
        self.progressBar.setGeometry(QtCore.QRect(12, 10, 180, 20))
        self.progressBar.setProperty("value", 34)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(x)
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        self.progressBar.setTextVisible(False)
    
        self.progressBarLabel = QLabel(self.GorevDurumuFrame)
        self.progressBarLabel.setGeometry(QtCore.QRect(80, 10, 50, 20))
        self.progressBarLabel.setText("% {}".format(x))
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.progressBarLabel.setVisible(True)
        self.progressBarLabel.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.progressBarLabel.setFont(QFont('Arial', 10))

        
        checkbox_positions = [(10, 40), (10, 70), (10, 100), (10, 130), (10, 160), (10, 190)]
        checkbox_texts = ['0 : Uçuşa Hazır', '1 : Yükselme', '2 : Model Uydu İniş', '3 : Ayrılma', '4 : Görev Yükü İniş', '5 : Kurtarma']
        for pos, text in zip(checkbox_positions, checkbox_texts):
            checkbox = QCheckBox(text, self.GorevDurumuFrame)
            checkbox.setGeometry(pos[0] + 10, pos[1], 160, 23)
            checkbox.setStyleSheet("font-size: 14px;")  # Font boyutu güncelleme
            checkbox.setFont(QFont("Arial", 12))  # Yazı tipi ve boyutu güncelleme
        # ----------------------------------------------------------------------------------------------------------
    
        # ----------------------------------------------------------------------------------------------------------
        self.dataTable = QtWidgets.QTableWidget(self.TableFrame)
        self.dataTable.setGeometry(QtCore.QRect(10, 10, 1450, 230))
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(21)
        self.dataTable.setRowCount(10)
        self.dataTable.setHorizontalHeaderLabels(
            TELEMETRY_TYPES_COLUMNS_NAMES)
        self.dataTable.setSortingEnabled(True)
        self.dataTable.setCornerButtonEnabled(False)
        #self.dataTable.setGridStyle(QHeaderView.GridStyle.SolidLine)
        self.dataTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.dataTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.dataTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.dataTable.setAlternatingRowColors(True)
        self.dataTable.setShowGrid(True)
        self.dataTable.setWordWrap(False)
        self.dataTable.setCornerButtonEnabled(False)
        self.dataTable.verticalHeader().hide()

        x = 13
        self.dataTable.setColumnWidth(0, 52 + x)  # paket no
        self.dataTable.setColumnWidth(1, 47 + x)  # statü
        self.dataTable.setColumnWidth(2, 65 + x)  # hata kodu
        self.dataTable.setColumnWidth(3, 107 + x)  # gönderme saati
        self.dataTable.setColumnWidth(4, 45 + x)  # basınc1
        self.dataTable.setColumnWidth(5, 45 + x)  # basınc2
        self.dataTable.setColumnWidth(6, 45 + x)  # yükseklik1
        self.dataTable.setColumnWidth(7, 45 + x)  # yükseklik2
        self.dataTable.setColumnWidth(8, 60 + x)  # irtifa farkı
        self.dataTable.setColumnWidth(9, 50 + x)  # iniş hızı
        self.dataTable.setColumnWidth(10, 50 + x)  # sıcaklık
        self.dataTable.setColumnWidth(11, 50 + x)  # pil gerilimi
        self.dataTable.setColumnWidth(12, 55 + x)  # gps1 latitude
        self.dataTable.setColumnWidth(13, 55 + x)  # gps1 longitude
        self.dataTable.setColumnWidth(14, 50 + x)  # gps1 altitude
        self.dataTable.setColumnWidth(15, 44 + x)  # pitch
        self.dataTable.setColumnWidth(16, 44 + x)  # Roll
        self.dataTable.setColumnWidth(17, 44 + x)  # yaw
        self.dataTable.setColumnWidth(18, 55 + x)  # rhrh
        self.dataTable.setColumnWidth(19, 55 + x)  # iot data
        self.dataTable.setColumnWidth(20, 90 + x)  # takım no

        for i in range(0, self.dataTable.rowCount()):
            self.dataTable.setRowHeight(i, 20)

        self.dataTable.selectRow(16)
        self.dataTable.setStyleSheet(
            "QTableWidget::item:selected {background-color: YellowGreen;}")
        
        fake_veriler = [
            [1, "Hazır", "00000", "2024-04-28 08:30:00", 1013.25, 1015.78, 500, 550, 50, 3.5, 25.6, 3.7, 41.1234, 29.9876, 200, 5.6, 2.3, 180, 78, "IoT_DATA_1", 345674],
            [2, "Hazır", "00000", "2024-04-28 09:15:00", 1011.89, 1014.20, 490, 545, 55, 4.2, 26.8, 3.6, 41.2345, 30.0987, 210, 6.2, 1.8, 175, 80, "IoT_DATA_2", 345674],
            [3, "Hazır", "00000", "2024-04-28 10:00:00", 1012.70, 1015.00, 510, 560, 50, 3.8, 25.2, 3.8, 41.3456, 30.2109, 220, 5.8, 2.5, 178, 75, "IoT_DATA_3", 345674],
            [4, "Hazır", "00000", "2024-04-28 10:45:00", 1011.35, 1014.80, 480, 540, 60, 4.5, 27.4, 3.5, 41.4567, 30.3221, 230, 6.4, 2.0, 172, 77, "IoT_DATA_4", 345674],
            [5, "Hazır", "00000", "2024-04-28 11:30:00", 1013.10, 1015.50, 495, 555, 40, 3.6, 25.9, 3.9, 41.5678, 30.4332, 240, 5.5, 2.8, 181, 79, "IoT_DATA_5", 345674],
            [6, "Hazır", "00000", "2024-04-28 12:15:00", 1010.95, 1013.40, 485, 535, 50, 4.0, 26.5, 3.7, 41.6789, 30.5443, 250, 6.0, 1.6, 177, 76, "IoT_DATA_6", 345674],
            [7, "Hazır", "00000", "2024-04-28 13:00:00", 1012.40, 1014.70, 515, 565, 50, 3.7, 25.1, 4.0, 41.7890, 30.6554, 260, 5.7, 2.3, 179, 81, "IoT_DATA_7", 345674],
            [8, "Hazır", "00000", "2024-04-28 13:45:00", 1011.15, 1013.60, 495, 550, 45, 4.3, 27.0, 3.6, 41.8901, 30.7665, 270, 6.3, 1.9, 173, 78, "IoT_DATA_8", 345674],
            [9, "Hazır", "00000", "2024-04-28 14:30:00", 1013.50, 1015.90, 505, 560, 45, 3.9, 25.5, 3.8, 41.9012, 30.8776, 280, 5.9, 2.6, 180, 74, "IoT_DATA_9", 345674],
            [10, "Hazır", "00000", "2024-04-28 15:15:00", 1010.75, 1013.20, 490, 545, 55, 4.6, 27.6, 3.5, 41.0123, 30.9887, 290, 6.5, 2.1, 175, 77, "IoT_DATA_10", 345674]
        ]
        # Tabloya fake verileri ekle
        for row, data in enumerate(fake_veriler):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                self.dataTable.setItem(row, col, item)

        # Tablo satır yüksekliklerini ayarla
        for i in range(0, self.dataTable.rowCount()):
            self.dataTable.setRowHeight(i, 20)

        self.dataTable.selectRow(9)

        self.clearTableButton = QPushButton('C', self.TableFrame)
        self.clearTableButton.setGeometry(1465, 10, 40, 230)
        self.clearTableButton.setFont(QFont("Times New Roman", 12))
        self.clearTableButton.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px;")
        # ----------------------------------------------------------------------------------------------------------
        
        # ----------------------------------------------------------------------------------------------------------
        self.ArayuzAlarmTitle = QLabel(self.ArayuzAlarmFrame)
        self.ArayuzAlarmTitle.setGeometry(24, 10, 180, 40)
        self.ArayuzAlarmTitle.setFont(QFont('Arial', 15))
        self.ArayuzAlarmTitle.setText("ARAS")
        self.ArayuzAlarmTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        style2 = """
        QLabel {
            border-radius: 5px;
            border: 0px solid #ccc; /* Gri kenarlık */
            padding: 5px; /* Kenar boşluğu */
            color: #333; /* Koyu gri metin */
        }
        """
        self.ArayuzAlarmTitle.setStyleSheet(style2)
        
        ArayuzAlarmString = "Hata Kodu: "
        self.ArayuzAlarmString = QLabel(self.ArayuzAlarmFrame)
        self.ArayuzAlarmString.setGeometry(24, 55, 170, 30)
        self.ArayuzAlarmString.setFont(QFont('Arial', 12))
        self.ArayuzAlarmString.setText(ArayuzAlarmString + "<" +"00000" + ">")
        self.ArayuzAlarmString.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        style1 = """
        QLabel {
            background-color: #A3AB78; /* Açık gri arka plan */
            border-radius: 5px;
            border: 1px solid #ccc; /* Gri kenarlık */
            padding: 5px; /* Kenar boşluğu */
            color: #333; /* Koyu gri metin */
        }
        """
        self.ArayuzAlarmString.setStyleSheet(style1)

        
        
        self.ArayuzAlarmTable = QtWidgets.QTableWidget(self.ArayuzAlarmFrame)
        self.ArayuzAlarmTable.setGeometry(QtCore.QRect(10, 110, 197, 62))
        # Labelların görünürlüğünü kapatma
        self.ArayuzAlarmTable.horizontalHeader().setVisible(False)
        self.ArayuzAlarmTable.verticalHeader().setVisible(False)
        self.ArayuzAlarmTable.setRowCount(2)  
        self.ArayuzAlarmTable.setColumnCount(5)  
        self.ArayuzAlarmTable.setColumnWidth(0, 30)  
        self.ArayuzAlarmTable.setColumnWidth(1, 30)  
        self.ArayuzAlarmTable.setColumnWidth(2, 30)  
        self.ArayuzAlarmTable.setColumnWidth(3, 30)  
        self.ArayuzAlarmTable.setColumnWidth(4, 30)  

        states = ["1", "2", "3", "4", "5"]
        for col, label in enumerate(states):
            item = QtWidgets.QTableWidgetItem(label)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFont(QFont("Arial", 12))  
            self.ArayuzAlarmTable.setItem(0, col, item)
            item.setBackground(QColor("#10454F"))

        for col, label in enumerate(states):
            item = QtWidgets.QTableWidgetItem("")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFont(QFont("Arial", 12))  
            self.ArayuzAlarmTable.setItem(1, col, item)
            if col % 2 == 0:  
                item.setBackground(QColor("red"))
            else:  
                item.setBackground(QColor("green"))
        # ----------------------------------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------------------------------
        MapImage_PixMap = QPixmap("Taslak/3.png")
        MapImage_Label = QLabel(self.mapFrame)
        MapImage_Label.setPixmap(MapImage_PixMap)
        MapImage_Label.setGeometry(15, 10, 283, 232)

        print(MapImage_PixMap.width() + 5, MapImage_PixMap.height() - 40) # 283 232

        latitudeLongitudeAltitudeSatsString = "Lat: 00.000000  Long: 00.000000  Alt: 000.0 m"
        latitudeLongitudeAltitudeSatsText = QLabel(self.mapFrame)
        latitudeLongitudeAltitudeSatsText.setGeometry(15, 283 - 34, 283, 40)
        latitudeLongitudeAltitudeSatsText.setFont(QFont('Arial', 10))
        latitudeLongitudeAltitudeSatsText.setText(latitudeLongitudeAltitudeSatsString)
        latitudeLongitudeAltitudeSatsText.setStyleSheet("background-color: #A3AB78")
        latitudeLongitudeAltitudeSatsText.show()
        # ----------------------------------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------------------------------
        AxisImage_PixMap = QPixmap("Taslak\eksen.png")
        AxisImage_Label = QLabel(self.eksenFrame)
        AxisImage_Label.setPixmap(AxisImage_PixMap)
        AxisImage_Label.setGeometry(25, 10, 222, 334)

        print("eksen : ", AxisImage_PixMap.width() + 40, AxisImage_PixMap.height()+ 150)

        pitchRollYawString = "   Pitch: 0°     Roll: 0°     Yaw: 0°"
        pitchRollYawText = QLabel(self.eksenFrame)
        pitchRollYawText.setGeometry(25, 350, 222, 30)
        pitchRollYawText.setFont(QFont('Arial', 11))
        pitchRollYawText.setText(pitchRollYawString)
        pitchRollYawText.setStyleSheet("background-color: #A3AB78")
        pitchRollYawText.show()
        # ----------------------------------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------------------------------
        # Kamera çerçevesi

        CameraImage_PixMap = QPixmap("Taslak/2.jpg")
        CameraImage_Label = QLabel(self.CameraFrame)
        CameraImage_Label.setPixmap(CameraImage_PixMap)
        CameraImage_Label.setGeometry(19, 10, 275, 305)

        button_y = 275 + 50

        # Kamera seç butonu
        self.KameraSecButton = QPushButton('Kamera Seç', self.CameraFrame)
        self.KameraSecButton.setGeometry(20, button_y, 275, 32)
        self.KameraSecButton.setFont(QFont("Times New Roman", 12))
        self.KameraSecButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Yeşil */
                border: 2px solid #4CAF50;
                border-radius: 10px;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049; /* Açık yeşil */
                border: 2px solid #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c; /* Daha koyu yeşil */
                border: 2px solid #388e3c;
            }
        """)

        button_y += 45

        # Kamera başlat butonu
        self.KameraBaslatButton = QPushButton('Kamera Başlat', self.CameraFrame)
        self.KameraBaslatButton.setGeometry(20, button_y, 125, 32)
        self.KameraBaslatButton.setFont(QFont("Times New Roman", 12))
        self.KameraBaslatButton.setStyleSheet("""
            QPushButton {
                background-color: #2196F3; /* Mavi */
                border: 2px solid #2196F3;
                border-radius: 10px;
                color: white;
            }
            QPushButton:hover {
                background-color: #1e87f0; /* Açık mavi */
                border: 2px solid #1e87f0;
            }
            QPushButton:pressed {
                background-color: #0b5bdd; /* Daha koyu mavi */
                border: 2px solid #0b5bdd;
            }
        """)

        # Kamera durdur butonu
        self.KameraDurdurButton = QPushButton('Kamera Durdur', self.CameraFrame)
        self.KameraDurdurButton.setGeometry(170, button_y, 125, 32)
        self.KameraDurdurButton.setFont(QFont("Times New Roman", 12))
        self.KameraDurdurButton.setStyleSheet("""
            QPushButton {
                background-color: #f44336; /* Kırmızı */
                border: 2px solid #f44336;
                border-radius: 10px;
                color: white;
            }
            QPushButton:hover {
                background-color: #d32f2f; /* Açık kırmızı */
                border: 2px solid #d32f2f;
            }
            QPushButton:pressed {
                background-color: #b71c1c; /* Daha koyu kırmızı */
                border: 2px solid #b71c1c;
            }
        """)

        button_y += 45

        # Kayıt başlat butonu
        self.KayitBaslatButton = QPushButton('Kayıt Başlat', self.CameraFrame)
        self.KayitBaslatButton.setGeometry(20, button_y, 125, 32)
        self.KayitBaslatButton.setFont(QFont("Times New Roman", 12))
        self.KayitBaslatButton.setStyleSheet("""
            QPushButton {
                background-color: #FFC107; /* Turuncu */
                border: 2px solid #FFC107;
                border-radius: 10px;
                color: white;
            }
            QPushButton:hover {
                background-color: #FFA000; /* Açık turuncu */
                border: 2px solid #FFA000;
            }
            QPushButton:pressed {
                background-color: #FF8F00; /* Daha koyu turuncu */
                border: 2px solid #FF8F00;
            }
        """)

        # Kayıt durdur butonu
        self.KayitDurdurButton = QPushButton('Kayıt Durdur', self.CameraFrame)
        self.KayitDurdurButton.setGeometry(170, button_y, 125, 32)
        self.KayitDurdurButton.setFont(QFont("Times New Roman", 12))
        self.KayitDurdurButton.setStyleSheet("""
            QPushButton {
                background-color: #9E9E9E; /* Gri */
                border: 2px solid #9E9E9E;
                border-radius: 10px;
                color: white;
            }
            QPushButton:hover {
                background-color: #757575; /* Açık gri */
                border: 2px solid #757575;
            }
            QPushButton:pressed {
                background-color: #424242; /* Daha koyu gri */
                border: 2px solid #424242;
            }
        """)
        # ----------------------------------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------------------------------
        self.basinc1plot = pg.PlotWidget(self)
        self.basinc1plot.setLabel('left', "Basınç 1", units='Pa')
        self.basinc1plot.setLabel('bottom', "Zaman", units='s')  
        self.basinc1plot.showGrid(x=True, y=True)
        self.xBasinc1 = list(range(10))  # 100 time points
        self.yBasinc1 = [randint(0, 100) for _ in range(10)]
        pen1 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_basinc1 = self.basinc1plot.plot(
            self.xBasinc1, self.yBasinc1, pen=pen1)

        self.basinc2plot = pg.PlotWidget(self)
        self.basinc2plot.setLabel('left', "Basınç 2", units='Pa')
        self.basinc2plot.setLabel('bottom', "Zaman", units='s')  
        self.basinc2plot.showGrid(x=True, y=True)
        self.xBasinc2 = list(range(10))  # 100 time points
        self.yBasinc2 = [randint(0, 100) for _ in range(10)]  
        pen2 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_basinc2 = self.basinc2plot.plot(
            self.xBasinc2, self.yBasinc2, pen=pen2)

        self.yukseklik1plot = pg.PlotWidget(self)
        self.yukseklik1plot.setLabel('left', "Yükseklik 1", units='m')
        self.yukseklik1plot.setLabel('bottom', "Zaman", units='s')  
        self.yukseklik1plot.showGrid(x=True, y=True)
        self.xYukseklik1 = list(range(10))  # 100 time points
        self.yYukseklik1 = [randint(0, 100) for _ in range(10)]  
        pen3 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_yukseklik1 = self.yukseklik1plot.plot(
            self.xYukseklik1, self.yYukseklik1, pen=pen3)

        self.yukseklik2plot = pg.PlotWidget(self)
        self.yukseklik2plot.setLabel('left', "Yükseklik 2", units='m')
        self.yukseklik2plot.setLabel('bottom', "Zaman", units='s')  
        self.yukseklik2plot.showGrid(x=True, y=True)
        self.xYukseklik2 = list(range(10))  # 100 time points
        self.yYukseklik2 = [randint(0, 100) for _ in range(10)]
        pen4 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_yukseklik2 = self.yukseklik2plot.plot(
            self.xYukseklik2, self.yYukseklik2, pen=pen4)

        self.inisHiziPlot = pg.PlotWidget(self)
        self.inisHiziPlot.setLabel('left', "İniş Hızı", units='m/s')
        self.inisHiziPlot.setLabel('bottom', "Zaman", units='s')  
        self.inisHiziPlot.showGrid(x=True, y=True)
        self.xBasinc = list(range(10))  # 100 time points
        self.yBasinc = [randint(0, 100) for _ in range(10)]  
        pen5 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_inisHizi = self.inisHiziPlot.plot(
            self.xBasinc, self.yBasinc, pen=pen5)

        self.sicaklikPlot = pg.PlotWidget(self)
        self.sicaklikPlot.setLabel('left', "Sıcaklık", units='°C')
        self.sicaklikPlot.setLabel('bottom', "Zaman", units='s')  
        self.sicaklikPlot.showGrid(x=True, y=True)
        self.xBasinc = list(range(10))  # 100 time points
        self.yBasinc = [randint(0, 100) for _ in range(10)] 
        pen6 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_sicaklik = self.sicaklikPlot.plot(
            self.xBasinc, self.yBasinc, pen=pen6)

        self.pilGerilimiPlot = pg.PlotWidget(self)
        self.pilGerilimiPlot.setLabel('left', "Pil Gerilimi", units='V')
        self.pilGerilimiPlot.setLabel('bottom', "Zaman", units='s')  
        self.pilGerilimiPlot.showGrid(x=True, y=True)
        self.xBasinc = list(range(10))  # 100 time points
        self.yBasinc = [randint(0, 100) for _ in range(10)]  
        pen7 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_pilGerilimi = self.pilGerilimiPlot.plot(
            self.xBasinc, self.yBasinc, pen=pen7)

        self.irtifaFarkiPlot = pg.PlotWidget(self)
        self.irtifaFarkiPlot.setLabel('left', "İrtifa Farkı", units='m')
        self.irtifaFarkiPlot.setLabel('bottom', "Zaman", units='s')  
        self.irtifaFarkiPlot.showGrid(x=True, y=True)
        self.xBasinc = list(range(10))  # 100 time points
        self.yBasinc = [randint(0, 100) for _ in range(10)]  
        pen8 = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_irtifaFarki = self.irtifaFarkiPlot.plot(
            self.xBasinc, self.yBasinc, pen=pen8)


        plots = [
            self.basinc1plot, self.basinc2plot, self.yukseklik1plot, 
            self.yukseklik2plot, self.inisHiziPlot, self.sicaklikPlot,
            self.pilGerilimiPlot, self.irtifaFarkiPlot
        ]

        for plot in plots:
            plot.setParent(self.PlotFrame)

        self.basinc1plot.setGeometry(20, 20, 270, 180)
        self.basinc2plot.setGeometry(320, 20, 270, 180)
        self.yukseklik1plot.setGeometry(620, 20, 270, 180)
        self.yukseklik2plot.setGeometry(920, 20, 270, 180)

        self.inisHiziPlot.setGeometry(20, 220, 270, 180)
        self.sicaklikPlot.setGeometry(320, 220, 270, 180)
        self.pilGerilimiPlot.setGeometry(620, 220, 270, 180)
        self.irtifaFarkiPlot.setGeometry(920, 220, 270, 180)
        # ----------------------------------------------------------------------------------------------------------
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())