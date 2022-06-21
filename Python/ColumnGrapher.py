import pandas as pd
import os
import glob

path = r"C:\Users\blj17002\OneDrive - University of Connecticut\_UConn\Graduate Research\Phase 3\East Hartford Bridge\Data\Lexi\28-day"
all_files = glob.glob(os.path.join(path,"*.asc"))

columnData = ["Loc.2_SS_W_2 [µm/m]"]

print(all_files)

#file time is the period between saves for the data, minutes
file_time = 30
#collection rate is the frequency of data signals, Hz
collection_rate = 150

"""
n_rows = collection_rate*file_time*60
skip = np.arange(n_rows)
skip = np.delete(skip,np.arange(0,n_rows,collection_rate*60))
"""

data = []
for f in all_files:
    df = (pd.read_csv(f,sep="\t",index_col=False,usecols=columnData,encoding='latin1'))
    data.append(df)
    print("File: "+f+" completed.")

full_data = pd.concat(data,ignore_index=True)
print(full_data.head())

full_data.to_csv(path+"\Loc.2_SS_W_2-Day28.csv")