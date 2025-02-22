from PyQt5 import QtCore

class SideMenuAnimation:
    def __init__(self, sideframe, toggle_button, main_window):

        self.sideframe = sideframe
        self.toggle_button = toggle_button
        self.main_window = main_window


        self.animation = QtCore.QPropertyAnimation(self.sideframe, b"geometry")
        self.animation.setDuration(300)  

        self.toggle_button.enterEvent = self.extendSideMenu
        self.toggle_button.leaveEvent = self.collapseSideMenu

    def extendSideMenu(self, event):
        start_rect = self.sideframe.geometry()
        end_rect = QtCore.QRect(0, 50, 150, self.main_window.height() - 50)  
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.start()

    def collapseSideMenu(self, event):
        start_rect = self.sideframe.geometry()
        end_rect = QtCore.QRect(0, 50, 50, self.main_window.height() - 50)  
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.start()