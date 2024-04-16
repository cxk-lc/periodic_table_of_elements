from PySide2.QtCore import QStringListModel, QSize, Qt

from database_sqlalchemy.connect_sqlite import ConnectSqlite
from functools import partial
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QSpacerItem, QSizePolicy, QPushButton

from setting import elements_status_color, elements_type_color, \
    fields_translation, elements_button_style, elements_button_style_hover, \
    elements_switch_button_style
from ui.main_ui import Ui_MainWindow
from ui.elements_info_ui import Ui_ElementsInfoForm


class ElementsInfoWindow(QWidget, Ui_ElementsInfoForm):
    """
    info 窗口
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class PeriodicTableElementsMainWindow(QMainWindow):
    """
    主窗口
    """

    def __init__(self):
        super().__init__()

        # 窗口界面实例化
        self.ui = Ui_MainWindow()
        self.ui_elements_info = ElementsInfoWindow()

        # 初始化界面
        self.ui.setupUi(self)

        # 按钮颜色、样式
        self.elements_status_color = elements_status_color
        self.elements_type_color = elements_type_color
        self.elements_button_style = elements_button_style

        # 初始化按钮信息
        self.connect_sqlite = ConnectSqlite()
        self.all_elements = self.connect_sqlite.get_all_elements()
        self.Las_and_Acs_periodic = {
            '镧系元素': None,
            '锕系元素': None,
        }
        self.Las_and_Acs_buttons = {
            '镧系元素': [],
            '锕系元素': [],
        }
        self.Las_and_Acs_type = ['镧系元素', '锕系元素']
        self.Las_and_Acs_switch_buttons = {
            '镧系元素': None,
            '锕系元素': None,
        }
        self.create_all_elements_button()
        self.elements_button = self.get_all_elements_button()
        self.fill_elements_button()
        self.init_button_info()

        # 列表视图模型
        self.list_view_model = QStringListModel()
        self.selected_info = ''

        # 创建粘贴板
        self.clipboard = app.clipboard()

        # 点击事件
        self.clicked_event()

    def traversal_actinicles_lanthanide_show_switch(self):
        pass

    def get_all_elements_button(self):
        # 获取所有的按钮对象
        elements_button = []
        for attribute in self.ui.__dict__.values():
            try:
                attribute_name = attribute.objectName()
            except AttributeError:
                continue
            if 'pushButton' in attribute_name:
                elements_button.append(attribute)
        return elements_button

    def clicked_event(self):
        for button in self.elements_button:
            # 点击按钮打开info窗口
            button.clicked.connect(
                partial(self.query_elements_info, button.property('name')))

        # 复制在info窗口中选中的内容到粘贴板
        self.ui_elements_info.copy_selected_info.clicked.connect(
            self.copy_selected)

        # 点击 镧系/锕系 元素开关时，显示/隐藏 所有 镧系/锕系 元素
        for Las_Acs in self.Las_and_Acs_type:
            self.Las_and_Acs_switch_buttons.get(Las_Acs).clicked.connect(
                partial(self.Las_and_Acs_switch, Las_Acs)
            )

    def Las_and_Acs_switch(self, Las_Acs):
        for button in self.Las_and_Acs_buttons.get(Las_Acs):
            if button.isHidden():
                self.Las_and_Acs_periodic.get(Las_Acs).show()
                button.show()
            else:
                self.Las_and_Acs_periodic.get(Las_Acs).hide()
                button.hide()

    def on_selection_changed(self, selected):
        # 获取在info页面选中的内容
        index = selected.indexes()[0].row()
        self.selected_info = \
            self.list_view_model.data(self.list_view_model.index(index, 0))

    def copy_selected(self):
        # 发送到粘贴板
        self.clipboard.setText(self.selected_info)
        self.selected_info = ''

    def create_all_elements_button(self):
        for element in self.all_elements:
            self.main_elements_button(element)
        for LasOrAcs in self.Las_and_Acs_type:
            self.create_periodic_Las_and_Acs_label(LasOrAcs)
            self.create_Las_and_Acs_switch_buttons(LasOrAcs)
        self.create_Las_and_Acs_spacer()

    def create_Las_and_Acs_spacer(self):
        self.ui.hSpacerLas = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                         QSizePolicy.Minimum)
        self.ui.hSpacerAcs = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                         QSizePolicy.Minimum)

    def create_periodic_Las_and_Acs_label(self, element_type):
        label_text = {
            '镧系元素': '_6_1',
            '锕系元素': '_7_1',
        }
        periodic_num = {
            '镧系元素': '6',
            '锕系元素': '7',
        }
        ui = self.ui
        obj_name = 'periodic' + label_text.get(element_type)
        label_size = 'QSize(15, 80)'

        exec(f'ui.{obj_name}=QLabel(ui.nature_tab)')
        exec(f'ui.{obj_name}.setObjectName("{obj_name}")')
        exec(f'ui.{obj_name}.setMinimumSize({label_size})')
        exec(f'ui.{obj_name}.setMaximumSize({label_size})')
        exec(f'ui.{obj_name}.setText("{periodic_num.get(element_type)}")')
        exec(f'ui.{obj_name}.setAlignment(Qt.AlignCenter)')
        exec(f'ui.{obj_name}.hide()')
        exec(f'self.Las_and_Acs_periodic["{element_type}"]=ui.{obj_name}')

    def main_elements_button(self, element):
        ui = self.ui
        element_symbol = element.element_symbol
        name = element.name
        element_type = element.element_type
        button_size = 'QSize(70, 80)'
        exec(f'ui.pushButton_{element_symbol}=QPushButton(ui.nature_tab)')
        obj_name = 'pushButton_' + element_symbol
        exec(f'ui.{obj_name}.setObjectName("{obj_name}")')
        exec(f'ui.{obj_name}.setMinimumSize({button_size})')
        exec(f'ui.{obj_name}.setMaximumSize({button_size})')
        exec(f'ui.{obj_name}.setProperty("name", "{name}")')
        if element_type in self.Las_and_Acs_type:
            exec(f'ui.{obj_name}.setProperty("type", "{element_type}")')
            exec(f'ui.{obj_name}.hide()')
            exec(
                f'self.Las_and_Acs_buttons.get(element_type).append(ui.{obj_name})')

    def fill_elements_button(self):
        # 将各元素按钮填充到 gridLayout 布局中
        row_num = self.ui.gridLayout.rowCount()
        col_num = self.ui.gridLayout.columnCount()
        self.fill_main_buttons(row_num, col_num)

        self.ui.gridLayout.addItem(self.ui.hSpacerLas, row_num, 1, 1, 3)
        self.ui.gridLayout.addItem(self.ui.hSpacerAcs, row_num + 1, 1, 1, 3)
        self.ui.gridLayout.addWidget(self.Las_and_Acs_periodic.get('镧系元素'),
                                     row_num, 0, 1, 1)
        self.ui.gridLayout.addWidget(self.Las_and_Acs_periodic.get('锕系元素'),
                                     row_num + 1, 0, 1, 1)
        self.fill_Las_and_Acs(row_num, col_num, '镧系元素')
        self.fill_Las_and_Acs(row_num + 1, col_num, '锕系元素')

    def fill_Las_and_Acs(self, row_num, col_num, element_type):
        elements = self.connect_sqlite.get_element_data_by_type(element_type)
        count = 0
        for col in range(4, col_num):
            for button in self.Las_and_Acs_buttons.get(element_type):
                if button.property('name') == elements[count].name:
                    self.ui.gridLayout.addWidget(button, row_num, col, 1, 1)
                    # button.show()
            count += 1

    def fill_main_buttons(self, row_num, col_num):
        elements = self.query_all_elements_from_db()
        count = 0
        for row in range(2, row_num):
            for col in range(1, col_num):
                if row == 2 and col in range(2, 18):
                    continue
                if row in [3, 4] and col in range(3, 13):
                    continue
                if row == 7 and col == 3:
                    self.ui.gridLayout.addWidget(self.ui.pushButton_Las,
                                                 row, col, 1, 1)
                    count += 15
                    continue
                if row == 8 and col == 3:
                    self.ui.gridLayout.addWidget(self.ui.pushButton_Acs,
                                                 row, col, 1, 1)
                    count += 15
                    continue
                for button in self.elements_button:
                    if button.property('name') == elements[count].name:
                        self.ui.gridLayout.addWidget(button, row, col, 1, 1)
                count += 1

    def create_Las_and_Acs_switch_buttons(self, LasOrAcs: str):
        # 创建镧系元素和锕系元素显示开关
        e_type = {
            '镧系元素': 'Las',
            '锕系元素': 'Acs'
        }
        element_range = {
            '镧系元素': '57~71',
            '锕系元素': '89~103'
        }
        ui = self.ui
        obj_name = f'pushButton_{e_type.get(LasOrAcs)}'
        e_range = element_range.get(LasOrAcs)

        exec(f'ui.{obj_name}=QPushButton(ui.nature_tab)')
        exec(f'ui.{obj_name}.setObjectName("{obj_name}")')
        exec(f'ui.{obj_name}.setMinimumSize(QSize(70, 80))')
        exec(f'ui.{obj_name}.setMaximumSize(QSize(70, 80))')
        exec(f'ui.{obj_name}.setProperty("name", "{LasOrAcs}")')
        exec(f'ui.{obj_name}.setProperty("range", "{e_range}")')
        exec(f'ui.{obj_name}.setText("{LasOrAcs}")')
        exec(f'self.Las_and_Acs_switch_buttons["{LasOrAcs}"]=ui.{obj_name}')

    def init_button_info(self):
        # 初始化按钮的显示的文本内容以及显示样式
        for button in self.elements_button:
            button_name = button.property('name')
            if button_name == '镧系元素' or button_name == '锕系元素':
                atomic_num_range = button.property('range')
                button.setText(f'{atomic_num_range}\n{button_name}')
                style = f'text-align: center; ' \
                        f'color: {self.elements_status_color.get("固体")};' \
                        f'background-color: {self.elements_type_color.get(button_name)};' \
                        f'border:1px solid {self.elements_type_color.get(button_name + "边框")};'
                color_style = f'QPushButton{{{style}}}'
                color_style_hover = f'QPushButton:hover{{{elements_switch_button_style}}}'
                button.setStyleSheet(color_style + color_style_hover)
                button.clicked.connect(
                    self.traversal_actinicles_lanthanide_show_switch)
                continue

            # 从数据库中获取元素数据
            element = self.query_elements_info_from_db_by_name(button_name)

            if element:
                button_info = f'{element.atomic_num}\n' \
                              f'{element.element_symbol}\n{element.name}\n' \
                              f'{element.atomic_mass}'
                button.setText(button_info)
                status_color = self.elements_status_color.get(
                    element.element_status)
                type_color = self.elements_type_color.get(element.element_type)
                border_style = f'color: {status_color};' \
                               f'background-color: {type_color};' \
                               f'border: 2px solid {self.elements_type_color.get(element.element_type + "边框")};'
                color_style = f'QPushButton{{{self.elements_button_style + border_style}}}'

                color_style_hover = f'QPushButton:hover{{{elements_button_style_hover}}}'

                color_style += color_style_hover
                button.setStyleSheet(color_style)

    def query_elements_info(self, name):
        self.ui_elements_info.close()
        if name == '镧系元素' or name == '锕系元素':
            return
        self.ui_elements_info.show()
        element = dict(self.query_elements_info_from_db_by_name(name))
        # 将数据库中查询到的元素数据以键值对的形式显示
        info_list = []
        for k, v in element.items():
            info_list.append(f'{fields_translation.get(k)}: {v}')
        self.list_view_model.setStringList(info_list)
        self.ui_elements_info.elements_info_view.setModel(self.list_view_model)

        # 设置info页面元素数据的点击事件
        self.ui_elements_info.elements_info_view.selectionModel(). \
            selectionChanged.connect(self.on_selection_changed)

    def query_elements_info_from_db_by_name(self, name):
        return self.connect_sqlite.get_element_data_by_name(name)

    def query_elements_info_from_db_by_type(self, element_type):
        return self.connect_sqlite.get_element_data_by_type(element_type)

    def query_all_elements_from_db(self):
        return self.connect_sqlite.get_all_elements()


if __name__ == '__main__':
    app = QApplication([])
    main_window = PeriodicTableElementsMainWindow()
    main_window.show()
    app.exec_()
