import logging as log
import pandas as pd


def build_data_frames_xlsx(file_path):
    """
    # Build all RDDS in file_path.xlsx without first sheet
    """
    data_frames = {}
    try:
        sheets = pd.ExcelFile(file_path).sheet_names
        for sheet in sheets[1:]:
            df = pd.read_excel(
                file_path, sheet_name=sheet, engine='openpyxl')
            data_frames[sheet] = df
    except Exception as e:
        log.error(f"Error in DataFrameBuilder: {e}")
    return data_frames
