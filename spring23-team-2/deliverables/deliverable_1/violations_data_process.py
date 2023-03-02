import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
# read csv data from building and violations file.
def fetch_building_violations():
    df = pd.read_csv("../../data/tmpc1fh5mf6.csv", low_memory=False)
    return df


# read csv data: landlord assessment. Which contains the corelation between landlord and the building(address).
def fetch_landlord_assessment():
    df = pd.read_csv("../../data/fy2022pa-4.csv", low_memory=False)
    return df


# ------------------------------------------------------------------------------------------------------------------------
def get_violation_by_building():
    vio_df = fetch_building_violations()

    # get violation address.
    vio_new_df = vio_df[['case_no', 'status_dttm', 'status', 'violation_sthigh', 'violation_street', 'violation_suffix',
                         'violation_stno', 'violation_city', 'violation_zip']]
    vio_new_df = vio_new_df.astype(object).replace(np.nan, '')

    # count the violation by house(address).
    vio_new_df['ST_NAME'] = vio_new_df['violation_stno'].astype(str) + " " + vio_new_df['violation_sthigh'].astype(str) + " " + vio_new_df['violation_street'].astype(
        str) + " " + vio_new_df['violation_suffix']
    vio_count_df = vio_new_df.groupby(['ST_NAME', 'violation_city', 'violation_zip'], as_index=False)['case_no'].size().reset_index(name='violation_counts')\
        .sort_values("violation_counts", ascending=False)

    print(vio_count_df.head(20))
    # print(vio_count_df.columns)
    return vio_count_df


def get_violation_by_landlord():
    vio_df = get_violation_by_building()
    land_df = fetch_landlord_assessment()

    #get building's landlord info
    land_new_df = land_df[['PID', 'ST_NUM', 'ST_NAME', 'CITY', 'ZIPCODE', 'OWNER']]
    land_new_df = land_new_df.astype(object).replace(np.nan, '')

    #count the violation by landlords
    land_new_df['ADDRESS'] = land_new_df['ST_NUM'].astype(str) + " " + land_new_df['ST_NAME']
    # print(land_new_df.head(10))
    vio_land_df = pd.merge(vio_df, land_new_df, how='left', left_on=['ST_NAME'], right_on=['ADDRESS'])
    violand_count_df = vio_land_df.groupby(['OWNER'], as_index=False)['PID'].size().reset_index(name='violation_counts') \
        .sort_values("violation_counts", ascending=False)

    # print(vio_land_df.head(20))
    print(violand_count_df)
    plt.figure(figsize=[8, 4])
    plt.title('Landlords violation info')
    plt.subplot().bar(list(violand_count_df['OWNER'].unique()), violand_count_df['violation_counts'])
    plt.xticks(rotation=90)
    plt.show()



if __name__ == '__main__':
    get_violation_by_landlord()



