from class_database import ChemicalElement
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import setting


class ConnectSqlite(object):
    def __init__(self):
        db_f = setting.Sqlite_relative_f \
            if __name__ == '__main__' else setting.Sqlite_f
        self.__session = sessionmaker(bind=create_engine(db_f))()

    def get_element_data_by_name(self, name):
        element = \
            self.__session.query(ChemicalElement).filter(
                ChemicalElement.name == name).all()
        element = element[0] if element else None
        self.__session.close()
        return element

    def get_element_data_by_type(self, element_type):
        elements = self.__session.query(ChemicalElement).filter(
            ChemicalElement.element_type == element_type).all()
        self.__session.close()
        return elements

    def add_element_data(self, element_data: dict):
        chemical_element = ChemicalElement(**element_data)
        self.__session.add(chemical_element)
        self.__session.commit()
        self.__session.close()

    def add_all_element_data(self, element_data_list: [dict]):
        element_data_obj_list = []
        for element_data in element_data_list:
            element_data_obj_list.append(ChemicalElement(**element_data))
        self.__session.add_all(element_data_obj_list)
        self.__session.commit()
        self.__session.close()

    def get_all_elements(self):
        return self.__session.query(ChemicalElement).all()


if __name__ == '__main__':
    connect_sqlite = ConnectSqlite()

    # res = connect_sqlite.get_element_data_by_name('氢')
    # print(res.name)
    # res = connect_sqlite.get_element_data_by_name('好')
    # print(res)

    all_elements = connect_sqlite.get_all_elements()
    for element in all_elements:
        print(dict(element))
