###########################################
#                                         #
#                                         #
#             readLogger                  #
#             version 0.1                 #
#                                         #
###########################################

import sys
import codecs
import utilities
import os
from datetime import datetime
from datetime import timedelta

def dmy_to_ymd(date):
    """Return a datetime object with the format YYYY/MM/DD:HH:MM:SS 
    The parameter date is the date to transforme
    """
    return datetime.strptime(date, '%d/%b/%Y:%H:%M:%S')


def main() :
    """Script execution
    """
    #Create and configure the log file
    logLevel = sys.argv[1] if len(sys.argv) > 1 else "info"
    logger = utilities.setLogging("readLogger", logLevel)
    logger.debug("Logger created")


    #Get the configuration from the config.json file and check if the variable is empty
    logger.info("Get configuration")
    config = utilities.getConfig("config.json")
    #Check config result required
    logDirectory = config["Product"]["apache2"]["logDirectory"] if config["Product"]["apache2"]["logDirectory"]  else utilities.errorExit("logDirectory")
    logger.debug("logDirectory {}".format(logDirectory))
    fileLogPattern = config["Product"]["apache2"]["fileLogPattern"] if config["Product"]["apache2"]["fileLogPattern"]  else utilities.errorExit("fileLogPattern")
    logger.debug("fileLogPattern {}".format(fileLogPattern))
    codes = config["Product"]["apache2"]["codes"] if config["Product"]["apache2"]["codes"]  else utilities.errorExit("codes")
    logger.debug("codes {}".format(codes))
    minutesToCheck = config["minutes"] if config["minutes"]  else utilities.errorExit("minutes")
    logger.debug("minutesToCheck {}".format(minutesToCheck))
    currentDate = dmy_to_ymd(config["currentDate"]) if config["currentDate"]  else datetime.now()
    logger.debug("currentDate {}".format(currentDate))


    filesToRead = []
    URLs = {}


    #Get all log file to read
    for file in os.listdir(logDirectory) :
        if file.endswith(fileLogPattern) :
            logger.debug("Log file to read : {}".format(file))
            filesToRead.append(file)

            
    for file in filesToRead :
        #Open the file
        logger.info("Processing {} file".format(file))
        logger.debug("Opening {} file".format(file))
        logFile = codecs.open(logDirectory + file, "r", encoding="utf-8")

        #Read the file
        for line in logFile.readlines() :

            #Get and transform the date
            date = dmy_to_ymd(line.split()[3][1:]) 

            #analyse the last x minute(s)
            if currentDate - timedelta(minutes=minutesToCheck) < date :
                #Get url
                url = line.split()[6]
                #Get return code
                code = line.split()[8]

                #URL calculation
                if url in URLs:
                    URLs[url] =  URLs[url] + 1
                else :
                    URLs[url] = 1

                #Code calculation
                if code in codes:
                    codes[code] = codes[code] + 1
        
        #Close the file
        logFile.close()

                


    #Print and save result in log file
    print("URL stats for the last {} mintute(s)".format(minutesToCheck))
    logger.info("URL stats for the last {} mintute(s)".format(minutesToCheck))

    URLs = sorted(URLs.items(), key=lambda item: item[1])
    for url in URLs :
        print("URL: {} - Total {} - Per minute(s): {}".format(url[0], url[1], url[1]/minutesToCheck))
        logger.info("URL: {} - Total {} - Per minute(s): {}".format(url[0], url[1], url[1]/minutesToCheck))

    print("Code stats for the last {} mintute(s)".format(minutesToCheck))
    logger.info("Code stats for the last {} mintute(s)".format(minutesToCheck))

    codes = sorted(codes.items(), key=lambda item: item[1])
    for code in codes :
        print("URL: {} - Total {} - Per minute(s): {}".format(code[0], code[1], code[1]/minutesToCheck))
        logger.info("URL: {} - Total {} - Per minute(s): {}".format(code[0], code[1], code[1]/minutesToCheck))


#Main
main()