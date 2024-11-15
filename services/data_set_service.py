import logging as log
from data_frame_service import DataFrameService


class DataSetService():

    def __init__(self, file_path):
        self.data_frame_service = DataFrameService(f"resources/{file_path}")

        if self.data_frame_service.get_data_frames() == {}:
            print("Can't create a DataSetService with a data set emply")

    def process_integer_columns(self, table_id, columns):
        if table_id != '' and columns != []:
            if (self.get_data_frame_service().get_data_frames() != {}):
                self.data_frame_service.integer_column_transform(
                    table_id, columns)
            else:
                log.error(f"Can't process columns[{columns} in table[{
                          table_id} because data frame is emply")

    def process_float_columns(self, table_id, columns):
        if table_id != '' and columns != []:
            if (self.get_data_frame_service().get_data_frames() != {}):
                self.data_frame_service.process_float_columns(
                    table_id, columns)
            else:
                log.error(f"Can't process columns[{columns} in table[{
                          table_id} because data frame is emply")

    def get_data_frame_service(self):
        return self.data_frame_service
