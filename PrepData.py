import pandas as pd
import os

importPath = "E:\EastHartfordData\_data\Export"
destinationPath = "E:\EastHartfordData\_data\Sensors"

directory = os.listdir(os.fsdecode(importPath))

fileList = []
fileTime = []
sampleRate = 150

for file in directory:
    fileList.append(file)
    fileName = importPath + "\\" + file    
    
    tempDF = pd.read_csv(fileName,sep="\t",encoding='latin1')
    fileLength = len(tempDF.index)
        
    timeLength = fileLength / sampleRate
    fileTime.append(timeLength)
    
    print(fileName + " added with size = " + str(timeLength) + " seconds.")
    
df = pd.DataFrame(zip(fileTime,fileList), columns = ['Length (s)','File Name'])
df.sort_values('File Name')
print(df.head())

df.to_csv('fileNames.csv', index=False)
