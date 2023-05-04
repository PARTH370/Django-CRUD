import re
from .logger import app_logger
def validation_inputs(input, regex=None, max_len=0, max_length_flag=0):
    flag = 0

    if input == None:
        # if input is None than return False
        return False

    elif regex:
        if re.fullmatch(regex, input) and len(str(input).strip()) > 0:
            # if data is match with  our regex criteria
            pass
        else:
            # if data is not match with our regex criteria
            flag = 1

    if max_length_flag == 0:
        # if length flag is zero
        if max_len != 0:
            if len(str(input)) == max_len:
                pass
            else:
                flag = 1
    else:
        # if length flag is not zero, then chack max length argument criteria
        if max_len != 0:
            if len(str(input)) <= max_len:
                pass
            else:
                flag = 1

    if flag == 1:
        # if flag is 1, then return False
        return False
    else:
        # if flag is 
        return True
def getResponse(status: bool, message: str, data_key="", body=None, data_key2="", body2=None):
    obj = {}
    obj["status"] = status
    obj["msg"] = message
    
    if data_key:
        obj[data_key] = body
    if data_key2:
        obj[data_key2] = body2
   
    app_logger.info(f"{obj}")
    return obj
def get_exception_Responses(status: bool, message: str, data_key="", body=None, data_key2="", body2=None):
    obj = {}
    obj["status"] = status
    obj["msg"] = message
    
    if data_key:
        obj[data_key] = body
    if data_key2:
        obj[data_key2] = body2
    app_logger.trace(f"{obj}")
    return obj