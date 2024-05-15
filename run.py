import sys

from PyQt5.QtWidgets import QApplication
from page.homePage import HomePage
"""
项目启动文件
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = HomePage()
    main_page.show()
    sys.exit(app.exec())
