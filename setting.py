# 数据库文件地址
# 如果需要修改数据库地址，请将 alembic.ini 中的 sqlalchemy.url 做一并修改
Sqlite_f = 'sqlite:///database_sqlalchemy/identifier.sqlite'
Sqlite_relative_f = 'sqlite:///identifier.sqlite'


elements_status_color = {
    '固体': '#000000',
    '气体': '#990000',
    '液体': '#0000dd',
    '未知': '#667766'
}
elements_type_color = {
    '碱金属': '#eace5d',
    '碱金属边框': '#ceb552',
    '碱土金属': '#f1f165',
    '碱土金属边框': '#d4d459',
    '镧系元素': '#e8d19c',
    '镧系元素边框': '#ccb889',
    '锕系元素': '#f5ccda',
    '锕系元素边框': '#d7b3bf',
    '过渡金属': '#fac5b7',
    '过渡金属边框': '#dcada1',
    '贫金属': '#acdfec',
    '贫金属边框': '#97c4cf',
    '类金属': '#9ee5d4',
    '类金属边框': '#8bc9ba',
    '活泼非金属': '#8ced8c',
    '活泼非金属边框': '#7bd07b',
    '稀有气体': '#e5bde5',
    '稀有气体边框': '#c9a6c9',
    'N/A': '#eeeeee',
    'N/A边框': '#d1d1d1',
}

fields_translation = {
    'atomic_num': '原子序数',
    'element_type': '元素类型',
    'element_symbol': '化学符号',
    'element_status': '元素物质状态',
    'name': '元素名称',
    'atomic_mass': '原子量',
    'electron_shells': '电子层',
    'fusing_point': '熔点',
    'boiling_point': '沸点',
    'energy_level': '能级',
    'electronegativity': '电负性',
    'electronic_affinity': '电子亲合能',
    'encyclopedia_entry': '百科词条',
    'year_of_discovery': '发现年份',
}

elements_button_style = """
text-align: left;
line-height: 0.5;
"""
elements_button_style_hover = """
border: 3px solid #2DBEFC;
font: 75 12pt "微软雅黑";
text-align: left;
"""
elements_switch_button_style = """
border: 3px solid #2DBEFC;
font: 75 12pt "微软雅黑";
"""



