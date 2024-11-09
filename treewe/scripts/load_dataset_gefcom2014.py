import os
import zipfile
import shutil
import pandas as pd

def extract_zip(file):
    # Unzip a file
    zip_ref = zipfile.ZipFile(file, 'r')
    folder = '/'.join(file.split('/')[:-1])
    zip_ref.extractall(folder)
    zip_ref.close()

def load_files(file_name, variables, site_number):
    dfs = []
    for i in range(1,site_number+1):
        file = file_name.format(i)
        df = pd.read_csv(file, index_col=1, parse_dates=True)
        df = df.pivot_table(index='TIMESTAMP', columns=['ZONEID'], values=variables, dropna=False)
        df.columns = df.columns.swaplevel(i=0, j=1)
        dfs.append(df)
    df_tasks = pd.concat(dfs, axis=1)

    return df_tasks

def load_wind_track():

    # Unzip files
    extract_zip('../data/gefcom2014/GEFCom2014 Data/GEFCom2014-W_V2.zip')
    extract_zip('../data/gefcom2014/GEFCom2014 Data/Wind/Task 15/Task15_W_Zone1_10.zip')
    extract_zip('../data/gefcom2014/GEFCom2014 Data/Wind/Task 15/TaskExpVars15_W_Zone1_10.zip')

    # Get all target data and explanatory variables except for last task
    df_task1_14 = load_files('../data/gefcom2014/GEFCom2014 Data/Wind/Task 15/Task15_W_Zone1_10/Task15_W_Zone{0}.csv', variables=['TARGETVAR', 'U10', 'V10', 'U100','V100'], site_number=10)

    # Get explanatory variables for last task
    df_exp15 = load_files('../data/gefcom2014/GEFCom2014 Data/Wind/Task 15/TaskExpVars15_W_Zone1_10/TaskExpVars15_W_Zone{0}.csv', ['U10', 'V10', 'U100','V100'], site_number=10)

    # Get target data for last task
    df_target15 = pd.read_csv('../data/gefcom2014/GEFCom2014 Data/Wind/Solution to Task 15/solution15_W.csv', index_col=1, parse_dates=True)
    df_target15 = df_target15.pivot_table(index='TIMESTAMP', columns=['ZONEID'], values=['TARGETVAR'], dropna=False)
    df_target15.columns = df_target15.columns.swaplevel(i=0, j=1)

    df_task15 = pd.merge(df_target15, df_exp15, on='TIMESTAMP')
    df = pd.concat([df_task1_14, df_task15], axis=0)
    df = df.rename(columns={'TARGETVAR': 'Power'}, level=1)

    site_names = ['Site'+str(i) for i in df.columns.levels[0]]
    df.columns = df.columns.set_levels(site_names, level=0)

    # Convert to standard indexing structure (ref_datetime, valid_datetime)
    df.index.name = 'valid_datetime'
    idx_ref_datetime = df.index.hour == 1
    df.loc[idx_ref_datetime, 'ref_datetime'] = df.index[idx_ref_datetime]
    df.loc[:, 'ref_datetime'] = df.loc[:, 'ref_datetime'].ffill()
    df = df.set_index('ref_datetime', append=True)
    df.index = df.index.reorder_levels(['ref_datetime', 'valid_datetime'])
    df = df.sort_index()

    # Remove hidden ref_datetime column from multiindex
    columns = [df.columns.levels[0][:-1].values, df.columns.levels[1][:-1].values]
    df.columns = pd.MultiIndex.from_product(columns)

    path = '../data/gefcom2014/gefcom2014-wind.csv'
    df.to_csv(path)
    print(f'Wind track data saved to: {path}')

def load_solar_track():

    # Unzip files
    extract_zip('../data/gefcom2014/GEFCom2014 Data/GEFCom2014-S_V2.zip')

    # Get all explanatory and target data for all tasks
    df = pd.read_csv('./Solar/Task 15/predictors15.csv', header=0, index_col=1, parse_dates=True)
    df = df.pivot_table(index='TIMESTAMP', columns=['ZONEID'], values=['POWER', 'VAR78', 'VAR79', 'VAR134', 'VAR157', 'VAR164', 'VAR165', 'VAR166', 'VAR167', 'VAR169', 'VAR175', 'VAR178', 'VAR228'], dropna=False)
    df.columns = df.columns.swaplevel(i=0, j=1)

    df = df.rename(columns={'POWER': 'Power'}, level=1)
    site_names = ['Site'+str(i) for i in df.columns.levels[0]]
    df.columns = df.columns.set_levels(site_names, level=0)

    # Convert to standard indexing structure (ref_datetime, valid_datetime)
    df.index.name = 'valid_datetime'
    idx_ref_datetime = df.index.hour == 1
    df.loc[idx_ref_datetime, 'ref_datetime'] = df.index[idx_ref_datetime]
    df.loc[:, 'ref_datetime'] = df.loc[:, 'ref_datetime'].ffill()
    df = df.set_index('ref_datetime', append=True)
    df.index = df.index.reorder_levels(['ref_datetime', 'valid_datetime'])
    df = df.sort_index()

    path = '../data/gefcom2014/gefcom2014-solar.csv'
    df.to_csv(path)
    print(f'Solar track data saved to: {path}.')

def load_load_track():

    # Unzip files
    extract_zip('../data/gefcom2014/GEFCom2014 Data/GEFCom2014-L_V2.zip')

    dfs = []
    for task in range(1,16):
        file = '../data/gefcom2014/GEFCom2014 Data/Load/Task {0}/L{0}-train.csv'.format(task)
        df = pd.read_csv(file, header=0)
        dfs.append(df)
    df = pd.concat(dfs)

    # The dates are ambiguous so need to hardcode them.
    df = df.drop(columns=['TIMESTAMP', 'ZONEID'])
    index = pd.date_range(start='2001-01-01 01:00', end='2011-12-01 00:00', freq='h')
    df.index = index
    df.index.name = 'datetime'

    df_task15 = pd.read_csv('../data/gefcom2014/GEFCom2014 Data/Load/Solution to Task 15/solution15_L_temperature.csv')
    df_task15.index = pd.to_datetime(df_task15['date'])+pd.to_timedelta(df_task15['hour'], unit='h')
    df_task15.index.name = 'datetime'
    df_task15 = df_task15.drop(columns=['date', 'hour'])
    df = pd.concat([df, df_task15])

    path = '../data/gefcom2014/gefcom2014-load.csv'
    df.to_csv(path)
    print(f'Load track data saved to: {path}.')

if __name__ == '__main__':
    zip_file = '../data/gefcom2014/1-s2.0-S0169207016000133-mmc1.zip'
    extract_zip(zip_file)
    shutil.move('../data/gefcom2014/GEFCom2014 Data/Provisional_Leaderboard_V2.xlsx', '../data/gefcom2014/Provisional_Leaderboard_V2.xlsx')
    load_wind_track()
    load_solar_track()
    load_load_track()
    shutil.rmtree('../data/gefcom2014/GEFCom2014 Data')
    os.remove(zip_file)
