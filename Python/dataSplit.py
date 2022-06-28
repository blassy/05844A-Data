'''
This script is intended to take large sensor data files that have been converted to ascii files. These can be .txt, .asc, .csv, etc.
A reference file must be supplied containing the ordered names of all of the files in the directory. This can be done intially when saving
or converting the data, or manually with a tool such as BulkRenameUtility. The reference file must be a .csv with at least 3 columns: 
    TimeStart: the datetime value for when the data in the file starts. 
    TimeEnd: the datetime value for when the data in the file ends.
    File Name: the full name of the file in the directory, including extension.
Once the reference file is read in, the script iterates through each line and opens the file. It then iterates through each column in the
file, applies a timestamp to each line as the index, then saves the timestamp and single column as a new .pqt in an associated folder.

'''
import pandas as pd
import os

startPath = r"E:\EastHartfordData\_data\Export" #File path for the ascii files containing all sensor data in a time range (eg, 30 minutes)
finalPath = r"E:\EastHartfordData\_data\Sensors" #File path for split up sensors to be sent to. 

referenceFile = pd.read_csv(r"C:\Users\blj17002\OneDrive - University of Connecticut\Documents\github\05844A-Data\Data\sortedFileLengths.csv")

for index, row in referenceFile.iterrows():
    #Get the full path of the file being worked on, as well as the first 5 characters (the ordering number of the file, eg: 0001_, 0002_,)
    fileName = startPath +"\\" + row['File Name']
    fileNumber = row['File Name'][0:5]

    #Extracts the start and end time from the reference file.
    dtStart = pd.to_datetime(row['TimeStart'])
    dtEnd = pd.to_datetime(row['TimeEnd'])
    
    #Opens the actual file as a dataframe, gets the number of rows (period) and builds a datetimeindex with all of the timestamps. 
    openFile = pd.read_csv(r"%s" % fileName,sep='\t',index_col=False,encoding='latin1')
    period = len(openFile.index)
    dateList = pd.date_range(start=dtStart,end=dtEnd,periods=period)
    dateList = dateList.to_frame(index=False,name='DateTime')

    #Iterate through the columns (sensors) and prepare export path info.
    for column in openFile:
        sensor = column.split(" [",1)[0]
        path = finalPath + "\\" + sensor
        
        #Create new dataframe using the datetimeindex as the index and the sensor data.
        tDF = dateList.join(openFile[[column]].copy())       
        
        #Check if folder exists for sensor, if not create it. 
        path_isExist = os.path.exists(path)
        if not path_isExist:
            os.makedirs(path)
            print(path + " has been created.")

        #Print data to parquet for column and timestamps.
        tDF_path = path + "\\" + fileNumber + sensor + ".parquet"
        tDF.to_parquet(tDF_path)
        print(tDF_path + " completed.")
    print(fileName + " completed.")
