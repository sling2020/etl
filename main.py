import logging as log
from services.data_set_service import DataSetService

data_set = DataSetService('Films_3.xlsx')
info_data_set = {
    'film': {
        'int_columns': ['film_id', 'release_year', 'language_id', 'original_language_id', 'rental_duration', 'length', 'num_voted_users'],
        'float_columns': ['rental_rate', 'replacement_cost']
    },
    'inventory': {
        'int_columns': ['inventory_id', 'film_id', 'store_id'],
        'float_columns': []
    },
    'rental': {
        'int_columns': ['rental_id', 'inventory_id', 'customer_id', 'staff_id'],
        'float_columns': []
    },
    'customer': {
        'int_columns': ['customer_id', 'store_id', 'address_id', 'active'],
        'float_columns': [],
        # 'boolean_columns': ['active']
    },
    'store': {
        'int_columns': ['store_id', 'manager_staff_id', 'address_id'],
        'float_columns': []
    }
}
if data_set.data_frame_service != {}:
    for table_name in info_data_set.keys():
        current_table = info_data_set[table_name]
        data_set.process_integer_columns(
            table_name, current_table['int_columns'])
        data_set.process_float_columns(
            table_name, current_table['float_columns'])
    # TODO GUARDAR EN LA DB EL DATA SET
    # TODO SISTEMA DE LOGS
    # TODO EL DOCUMENTO
    # TODO JOINS PARA RESOLVER LAS PREGUNTAS
    # TODO SUBIR A GCP
