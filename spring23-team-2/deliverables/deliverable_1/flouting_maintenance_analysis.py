import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
# read csv data from residential maintenance complaint info file.
def fetch_maintenance_complaint_info():
    df = pd.read_csv("/Users/maolongdan/ds-councilor-breadon-bad-landlords2/spring23-team-2/data/81a7b022-f8fc-4da5-80e4-b160058ca207.csv", low_memory=False)
    return df

#get the landlords' info who flouting the maintenance requirement
def get_landlordsinfo_by_maintenance():
    land_df = fetch_maintenance_complaint_info()
    land_new_df = land_df[['case_enquiry_id', 'closed_dt', 'ontime', 'case_status', 'case_title', 'location']]
    land_new_df = land_new_df[land_new_df['ontime']== "OVERDUE"]
    # land_new_df = land_new_df[land_new_df['case_status'] == "Closed"]
    land_count_df = land_new_df.groupby(['location'], as_index=False)['case_enquiry_id'].size().reset_index(name='violation_counts') \
        .sort_values("violation_counts", ascending=False)
    print(land_count_df)
    plt.figure(figsize=[8, 4])
    plt.title('Landlords info by maintenance')
    plt.subplot().bar(list(land_new_df['location'].unique()), land_new_df['location'].value_counts())
    plt.xticks(rotation=90)
    plt.show()



if __name__ == '__main__':
    get_landlordsinfo_by_maintenance()