# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""


import base64
import sys
import random
import os

tmp_global_obj = tmp_global_obj  # type:ignore
GetParams = GetParams  # type:ignore
SetVar = SetVar  # type:ignore
PrintException = PrintException  # type:ignore


base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'CloudShore' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from soapObject import SoapObject  # type:ignore

def encode_to_base64(path_file):
    """Convert file to base64."""
    try:
        with open(path_file, "rb") as file:
            base64_text = base64.b64encode(file.read())
            return base64_text
    except Exception as e:
        PrintException(e)
        return b""


def decode_to_base64(path_file, base64_text):
    """Decode a base64 string to file."""
    with open(path_file, "wb") as file:
        base64_text = base64_text.encode("utf-8", "ignore")
        file.write(base64.b64decode(base64_text))
        file.close()


global clientSoapObject
global mod_cloudshore_sessions

DEFAULT_SESSION = "default"
try:
    if not mod_cloudshore_sessions: #type:ignore
        mod_cloudshore_sessions = {DEFAULT_SESSION: {}}
except NameError:
    mod_cloudshore_sessions = {DEFAULT_SESSION: {}}

module = GetParams("module")
session = GetParams("session")
result = GetParams("result")
if not session:
    session = DEFAULT_SESSION

try:

    if module == "config":
        url = GetParams("url")
        service = GetParams("service")
        clientSoapObject = SoapObject(url + service + ".asmx?wsdl")
        mod_cloudshore_sessions[session] = {}
        mod_cloudshore_sessions[session]["clientSoapObject"] = clientSoapObject
        mod_cloudshore_sessions[session]["service_names"] = clientSoapObject.getServiceNames()

        SetVar(result, True)
        


    if module == "getMethods":
        SetVar("CloudShore_fake_var", {
            "serviceNames": mod_cloudshore_sessions[session]["service_names"],
        })

    if module == "execute_service":

        iframe = GetParams("iframe")
        operation = eval(iframe)["serviceName"]
        if "session" in eval(iframe):
            session = eval(iframe)["session"]
        if not session:
            session = DEFAULT_SESSION

        path_folder = GetParams("folder")
        result = GetParams("variable")

        clientSoapObject = mod_cloudshore_sessions[session]["clientSoapObject"] 
        operations = mod_cloudshore_sessions[session]["service_names"]

        if operation not in operations:
            raise Exception("Operation not exists")

        username = GetParams("username")
        password = GetParams("password")
        excelFileOutput = GetParams("excelFileOutput") or False
        excelFile = GetParams("excelFile")
        settingFile = GetParams("settingFile")

        # print("username:", excelFileOutput)
        variables = {
            "SapUsername": username,
            "SapPassword": password,
            "ExcelFileBase64": encode_to_base64(excelFile).decode("utf-8"),
            "SettingsFileBase64": encode_to_base64(settingFile).decode("utf-8"),
            "CodeSystemSource": "5"
        }

        resultSoap = clientSoapObject.serviceExe(operation, variables)
        tables = []
        try:
            resultSoap.Result
        except:
            raise Exception({"ThreadID": resultSoap.ThreadID , "ErrorMessage": resultSoap.ErrorMessage})

        for data in resultSoap.Result.Transaction:
            random_name = operation + \
                ''.join(chr(random.randrange(65, 90)) for i in range(10))

            if excelFileOutput:
                random_xlsx_name = random_name + ".xlsx"
                excel_path = os.path.join(path_folder, random_xlsx_name)
                decode_to_base64(excel_path, data.ExcelOutputFileBase64)

            random_log_name = random_name + ".log"
            log_path = os.path.join(path_folder, random_log_name)
            decode_to_base64(log_path, data.LogFileBase64)
            tables.append([{"schema": [str(s) for s in d.schema], "diffgram": [
                          str(dd) for dd in d.diffgram]} for d in data.Tables.DataTable])

        SetVar(result, tables)


except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    SetVar(result, False)
    PrintException()
    raise e
