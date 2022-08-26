



# Cloud Shore
  
Módulo para trabajar con SAP Web Service de Cloud Shore
  
![banner](imgs/Banner_CloudShore.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Configuración
  
Configure el servicio que se utilizará
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url|Hostname o IP del servicio que aloja la aplicación de los Digital Workers||
|Seleccione el servicio|Digital Worker que se desea consumir|Matt|
|Identificador (Opcional)|Identificador para servicio conectado|default|
|Asignar resultado a la variable|Variable donde se almacenará el resultado|result|

### Ejecutar servicio
  
Consume el servicio seleccionado en el comando anterior
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione el método que desea usar|Componente del Digital worker a ejecutar||
|Nombre de la variable donde se guardará el resultado|Variable donde se almacenará el resultado|variable|
|Usuario SAP|Usuario SAP|Usuario|
|Contraseña SAP||Contraseña|
|Generar archivo Excel||true|
|Seleccione archivo excel||excelFile.xlsx|
|Seleccionar archivo de configuración||SettingFile.xlsx|
|Carpeta donde guardar los archivos de resultantes||/path/to/folder|
