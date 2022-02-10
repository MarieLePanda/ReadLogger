import logging
from logging.handlers import RotatingFileHandler
import os
import sys
from datetime import datetime
import json

def setLogging(programeName, level = "info") :
    """Configure the logger for the programme
    The parameter 'programeName' will write in the log file the name of the programme running
    The parameter 'level' set what kind of error you want log, possible values are : debug, info, warning, error, critical. The default value is info 
    Return 'logger' the logger to use in the programme.
    """
    formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")
    handler = logging.handlers.RotatingFileHandler("{}.log".format(programeName), mode="a", maxBytes= 1000000, backupCount= 10, encoding="utf-8")
    handler.setFormatter(formatter)
    logger = logging.getLogger(programeName)

    if level == "debug" : logger.setLevel(logging.DEBUG)
    if level == "info" : logger.setLevel(logging.INFO)
    if level == "warning" : logger.setLevel(logging.WARNING)
    if level == "error" : logger.setLevel(logging.ERROR)
    if level == "critical" : logger.setLevel(logging.CRITICAL)

    logger.addHandler(handler)
    return logger

def getConfig(configPath) :
    """Return configuration in JSON format 
    The parameter configPath is the relative or full path of the JSON file that contains the configuration
    """
    config = None
    try :
        configFile = open(configPath, "r")
        config = json.load(configFile)
    except :
        e = sys.exc_info()[0]
    finally :
        configFile.close()
    return config

def errorExit(errorMessage) :
    """Display error message and exit
    The parameter errorMessage will be replaced with the message you want to display after the error
    """
    
    sys.exit("{} : {} - Unknown Error".format(sys.argv[0], errorMessage))
