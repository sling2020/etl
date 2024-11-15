import logging as log
import services.data_frames_builder as data_frames_builder


class DataFrameService:
    """    Data frame Service    """

    def __init__(self, file_path):
        self.data_frames = data_frames_builder.build_data_frames_xlsx(
            file_path)
        self.__generic_transform()

    def __generic_transform(self):
        """
        # Make a generic transform applying a strip() to all elements in RDD
        """

        for data_frame_name in self.data_frames:
            self.data_frames[data_frame_name].columns = self.data_frames[data_frame_name].columns.str.strip(
            )
            self.data_frames[data_frame_name].apply(lambda x: x.strip()
                                                    if isinstance(x, str) else x)

    def integer_column_transform(self, table_id, columns):
        """        Applies a transform to convert the columns to integer        """
        field_changed = 0
        for column in columns:
            data_frame_result = self.data_frames[table_id][column].apply(
                lambda x: ''.join(filter(str.isdigit, str(x))))
            # self.data_frames[table_id][column] = self.data_frames[table_id][column].apply(
            #     lambda x: ''.join(filter(str.isdigit, str(x))))
            field_changed += (
                self.data_frames[table_id][column] != data_frame_result).sum()
            self.data_frames[table_id][column] = data_frame_result
        return field_changed
    # def boolean_column_transform(self, table_id, columns):
    #     """        Applies a transform to convert the columns to boolean        """
    #     for column in columns:
    #         self.data_frames[table_id][column] = self.data_frames[table_id][column].apply(
    #             lambda x: int(''.join(filter(str.isdigit, str(x)))))

    def process_float_columns(self, table_id, columns):
        """        Applies a transform to convert the columns to float        """
        field_changed = 0

        def expresion(x):
            x_result = ''.join(c for c in str(x) if c.isdigit() or c == '.')
            firtPos = x_result.find('.')
            if firtPos == -1:
                return x_result + '.0'

            x_result = x_result[:firtPos + 1] + \
                x_result[firtPos + 1:].replace('.', '')
            return x_result
        for column in columns:
            data_frame_result = self.data_frames[table_id][column].apply(
                expresion)
            field_changed += (self.data_frames[table_id]
                              [column] != data_frame_result).sum()
            self.data_frames[table_id][column] = data_frame_result
        return field_changed

    def get_data_frames(self):
        """   Return Array with all Data Frames        """
        return self.data_frames

    def get_column_data_frame(self, table, columns):
        """   Return columns in a Data Frame table       """
        return self.data_frames[table][columns]
