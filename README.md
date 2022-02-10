# ReadLogger

ReadLogger is a Python script to get per minute the number of times a URL was reached and a code return

## Installation

Download directly the script from this Git repository

```bash
git https://github.com/MarieLePanda/ReadLogger.git
cd ReadLogger
chmod +x *py
```

## Configure

ReadLogger works with a configuration file in the same directory, named "config.json. Before running the script you must edit the configuration file with the following value.

By default, the configuration file and the script work to monitor an Apache service, but it can be modified easily to integrate other products.

The configuration file has the following attribute than must be complete
- logDirectory, the directory where are the log files
- fileLogPattern, the pattern to detect the current log file to analyze
- fileLogZipPattern, the pattern to detect log files that can be zip due to a log rotation policy and must be analyzed.
- codes, the return codes that you want to analyze
- minutes, the last minutes you want to analyze
- CurrentDate, the date that will be the starting point for the analysis, if this attribute is empty the currentDate attribute will be replaced by the current machine time. Example of format "04/Feb/2022:14:31:15"

## Run

To run the script in normal mode
```Bash
python readLogger.py
```

To run the script in debug mode
```Bash
python readLogger.py debug
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)