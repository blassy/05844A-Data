import pandas as pd
import os
import glob

path = r"E:\EastHartfordData\QuickGraphs\28-Day"
all_files = glob.glob(os.path.join(path,"*.asc"))

print(all_files)
all_files.sort()


data = []
for f in all_files:
    df = (pd.read_csv(f,sep="\t",index_col=False,encoding='latin1'))
    data.append(df)
    print("File: "+f+" completed.")

full_data = pd.concat(data,ignore_index=True)
print(full_data.head())

for column in full_data:
    sensor = column.split(" [",1)[0]   
    print(sensor)
    print(column)
    
    tDF = full_data[[column]]
    print(tDF.head())

    tDF_path = path + "\\" + sensor + ".csv"
    tDF.to_csv(tDF_path)
    print(tDF_path + " completed.")
