# parisianpollution

#Presentation

This is a little script working under Linux OS which gathers the current pollution level in Paris.

It send a get request to the AirParif API. It returns a Json build with the followings elements :
- Date
- Global pollution level
- no2 pollution level
- o3 pollution level
- pm10 pollution level

The script will save this data in a file using this pattern : date;global;n02;o3;pm10

The file name is made like this : YY-MM-pollutionrecord.

If the script is daily executed, each pollution level for a day will be written in a line.
A new file will be created each month, according to the file name pattern. 

#Configuration

On line 22, ou can change the directory where this file is stored. The default configuration in "/tmp"

On line 27 you can change the file name's pattern

From line 33 to 35, you can change the pattern used to save data
