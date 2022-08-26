



# Cloud Shore
  
Module to work with SAP Web Service of Cloud Shore  
  
![banner](imgs/Banner_CloudShore.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Setup
  
Configure the service to be used
|Parameters|Description|example|
| --- | --- | --- |
|URL|Hostname or IP of the service that hosts the application of the Digital Workers||
|Select the service|Digital Worker that you want to consume|Matt|
|Identifier (optional)|Identifier for the service connected|default|
|Assign result to the variable|Variable where the result will be stored|result|

### Execute service
  
Consume service selected in the previous command
|Parameters|Description|example|
| --- | --- | --- |
|Select the method that you want to use|Component of the Digital worker to execute||
|Variable name where the result will be saved|Variable where the result will be stored|variable|
|SAP Username|SAP Username|Username|
|SAP Password||Password|
|Excel file output||true|
|Select excel file||excelFile.xlsx|
|Select setting file||SettingFile.xlsx|
|Folder where the files will be saved||/path/to/folder|
