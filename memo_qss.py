# Оформлення
QSS = '''

QWidget#mainWindow, QWidget#cardWindow {
    background-color: #a9e8b5;
}

QWidget {
    font: 20px;
}

QPushButton { 
    background-color: #6b86f9; 
    border-width: 1px;
    border-radius: 10px;
    border-color: gray;
    font: 20px "Montserrat";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: #31dc6d;
    border-style: inset;
}
QGroupBox {
    color: gray;
    border-radius: 7px;
    border: 2px solid gray;
    margin-top: 2ex;
    background-color: #d3f7f6
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}

QRadioButton {
    font: bold 20px;
}
QRadioButton::indicator {
    width: 14px;
    height: 14px;
    border-radius: 7px;
}
QRadioButton::indicator::unchecked {
    border: 2px solid; 
    border-color: gray;
    background-color: white;
    border-radius: 7px;
}

QRadioButton::indicator:unchecked:hover {
    border-color: black;
    background-color: #ffffe2;
    border-radius: 7px;
}

QRadioButton::indicator::checked {
    border: 11px; 
    border-color: #ffbb88;
    background-color: #31dc6d;
    border-radius: 7px;
}

QLabel { 
    font: 20px "Montserrat";
}
'''

QSS_OK = '''
QPushButton { background-color: rgb(70, 150, 70); 
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 20px "Montserrat";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: gray;
    border-style: inset;
}
'''

QSS_TextCardQuestion = '''QLabel { 
    font: bold 26px "Montserrat";
}'''

QSS_TextResult = '''QLabel {
    font: italic 22px "Montserrat";
}'''

QSS_TextHeader = '''QLabel {
    font: 18px ;
}'''
