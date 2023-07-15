import pandas as pd
from zipfile import ZipFile

DATA_DIR = '../data/'
LSOA_DIR = 'lsoa_csvs/'

def show_data_dir(zipfiles):
    for zname in zipfiles:
        with ZipFile(zname, 'r') as zip:
            zip.printdir()
            print()

def extract_file_from_zip(zname, fname):
    with ZipFile(zname, 'r') as zip:
        zip.extract(fname, DATA_DIR)

def extract_all_from_zip(zname, path=None):
    with ZipFile(zname, 'r') as zip:
        zip.extractall(path=path)

def load_dfs(fname):
    dfs = {}
    with ZipFile(fname, 'r') as zip:
        for zip_info in zip.filelist:
            filename = zip_info.filename[:-4]
            dfs[filename] = pd.read_csv(DATA_DIR + LSOA_DIR + filename + '.csv')
    return dfs

def load_sheets(fname):
    valid_sheets = ['Mid-2020 Persons', 'Median Age']
    sheets_to_dfs = {}
    with pd.ExcelFile(fname) as xls:
        for sheet_name in xls.sheet_names:
            if sheet_name in valid_sheets:
                sheets_to_dfs[sheet_name] = xls.parse(sheet_name, skiprows=3, header=1)
    
    return sheets_to_dfs