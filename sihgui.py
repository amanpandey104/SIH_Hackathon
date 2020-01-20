# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/satyam/Desktop/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(807, 638)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 0, 91, 61))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 60, 141, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 170, 101, 61))
        self.label_2.setObjectName("label_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 230, 131, 111))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 410, 91, 41))
        self.label_3.setObjectName("label_3")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(110, 450, 131, 81))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.MainImage = QtWidgets.QLabel(Form)
        self.MainImage.setGeometry(QtCore.QRect(320, 160, 461, 351))
        self.pixmap = QtGui.QPixmap('1.jpg')
        self.MainImage.setPixmap(self.pixmap)
        #self.MainImage.setText("")
        self.MainImage.setObjectName("MainImage")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(470, 20, 241, 101))
        self.label_5.setStyleSheet("image: url(:/newPrefix/Downloads/8397.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(510, 10, 261, 111))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 530, 90, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.livefeed)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 530, 90, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Recon Subsea 2020 SIH"))
        self.label.setText(_translate("Form", "TEMPERATURE"))
        self.label_2.setText(_translate("Form", "ACIDITY"))
        self.label_3.setText(_translate("Form", "PRESSURE"))
        self.pushButton.setText(_translate("Form", "CAM1"))
        self.pushButton_2.setText(_translate("Form", "CAM2"))

        def x(self):
            global count
            cap = cv2.VideoCapture(0)
            while True:
                    ret,frame = cap.read()
                    '''cv2.imwrite('C:/python/camera0/frame%d.jpg' % count,frame)
                    self.label.setPixmap(QtGui.QPixmap('C:/python/camera0/frame%d.jpg' % count))
                    os.remove('C:/python/camera0/frame%d.jpg' % count)
                    count=count+1
                    time.sleep(.01)'''
                    cv2.imshow('frame0',frame)
                    k=cv2.waitKey(1)
                    if k==1:
                        break
            cv2.destroyAllWindows()
            cap.release()
    def showcam(self):
        t1 = threading.Thread(target = self.x)
        t1.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
