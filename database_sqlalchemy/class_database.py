from sqlalchemy import Column, INTEGER, Text, REAL, create_engine, DateTime
from sqlalchemy.orm.decl_api import declarative_base

# 创建一个基类
Base = declarative_base()


class ChemicalElement(Base):
    __tablename__ = 'chemical_element'
    atomic_num = Column(INTEGER, primary_key=True)
    element_type = Column(Text, nullable=True)
    element_symbol = Column(Text, unique=True, nullable=False)
    element_status = Column(Text, nullable=False)
    name = Column(Text, unique=True, nullable=False)
    atomic_mass = Column(REAL, nullable=False)
    electron_shells = Column(Text, nullable=False)
    fusing_point = Column(REAL, nullable=True)
    boiling_point = Column(REAL, nullable=True)
    energy_level = Column(INTEGER, nullable=False)
    electronegativity = Column(REAL, nullable=True)
    electronic_affinity = Column(REAL, nullable=True)
    encyclopedia_entry = Column(Text, nullable=True)
    year_of_discovery = Column(Text, nullable=True, default='unknown')

    @staticmethod
    def keys():
        keys_list = [
            'atomic_num',
            'element_type',
            'element_symbol',
            'element_status',
            'name',
            'atomic_mass',
            'electron_shells',
            'fusing_point',
            'boiling_point',
            'energy_level',
            'electronegativity',
            'electronic_affinity',
            'encyclopedia_entry',
            'year_of_discovery',
        ]
        return keys_list

    def __getitem__(self, item):
        return self.__getattribute__(item)


