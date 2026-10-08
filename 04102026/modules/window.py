from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QLabel
from modules.app import app 
from PyQt6.QtCore import Qt


main_window = QMainWindow()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW  = 800

# получаем обьект экрана
primary_screen = app.primaryScreen()
# получаем размеры экрана
screen_size = primary_screen.size()
# получаем ширину экрана
width_screen = screen_size.width()
# получаем высоту экрана
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

main_frame = QFrame(parent = main_window)
main_frame.setFixedSize(1024, 800)
main_frame.setStyleSheet("background-color:black")



main_layout = QVBoxLayout()
main_layout.setContentsMargins(0, 0, 0, 0)
main_layout.setSpacing(10)
main_frame.setLayout(main_layout)

label_1 = QLabel(text= "SPACE CONTROL", parent = main_frame)
label_1.setStyleSheet("color:white; font-size: 30px; font-weight: bold;")
label_1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
main_layout.addWidget(label_1, 1)

frame_2 = QFrame(parent = main_frame)
frame_2.setFixedSize(512, 250)
frame_2.setStyleSheet("background-color:gray")
main_layout.addWidget(frame_2, 2)

label_2 = QLabel(text= "SYSTEM ONLINE", parent = frame_2)
label_2.setStyleSheet("color:white; font-size: 25px;  font-weight: bold;")
#label_2.setAlignment(Qt.AlignmentFlag.AlignLeft)
#main_layout.addWidget(label_2, 2)



squares_layout = QHBoxLayout()

frame_red = QFrame(parent = main_frame)
frame_red.setFixedSize(130,100)
frame_red.setStyleSheet("background-color:red")

frame_blue = QFrame(parent = main_frame)
frame_blue.setFixedSize(130,100)
frame_blue.setStyleSheet("background-color:blue")

frame_green = QFrame(parent = main_frame)
frame_green.setFixedSize(130,100)
frame_green.setStyleSheet("background-color:green")

squares_layout.addWidget(frame_red)
squares_layout.addWidget(frame_blue)
squares_layout.addWidget(frame_green)
main_layout.addLayout(squares_layout)



frame_4 = QFrame(parent = main_frame)
frame_4.setFixedSize(512, 100)
frame_4.setStyleSheet("background-color:white")
main_layout.addWidget(frame_4, 4)

layout_frame4 = QHBoxLayout()
frame_4.setLayout(layout_frame4)
layout_frame4.setAlignment(Qt.AlignmentFlag.AlignTop)
layout_frame4.setContentsMargins(0, 0, 270, 0)

label_engine = QLabel(text= "ENGINE", parent = frame_4)
label_engine.setStyleSheet("color:black; font-size: 15px;")

label_radar = QLabel(text= "RADAR", parent = frame_4)
label_radar.setStyleSheet("color:black; font-size: 15px;")

label_navigation = QLabel(text= "NAVIGATION", parent = frame_4)
label_navigation.setStyleSheet("color:black; font-size: 15px;")

layout_frame4.addWidget(label_engine)
layout_frame4.addWidget(label_radar)
layout_frame4.addWidget(label_navigation)

