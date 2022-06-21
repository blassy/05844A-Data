
import pandas as pd
import os
import csv

importPath = r"E:\EastHartfordData\_data\Export"
destinationPath = r"E:\EastHartfordData\_data\Sensors"

directory = os.fsencode(importPath)

fileList = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileList.append(filename)
    
#    df = pd.read_csv(file,sep="\t",index_col=False,encoding='latin1')
fileList.sort()

print(fileList)

df = pd.DataFrame(fileList)
df.to_csv('fileNames.csv')

"""
all_files = glob.glob(os.importPath.join(importPath,"*.asc"))

sensorName = "Loc.2_SS_W_2 [µm/m]"
columnData = [sensorName]
print(all_files)


data = []
for f in all_files:
    df = (pd.read_csv(f,sep="\t",index_col=False,usecols=columnData,encoding='latin1'))
    data.append(df)
    print("File: "+f+" completed.")

full_data = pd.concat(data,ignore_index=True)
print(full_data.head())

full_data.to_csv(destinationPath+"\Loc.2_SS_W_2-Day28.csv")
"""