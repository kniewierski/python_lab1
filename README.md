# python_lab1
# Marketing Data

Howdy! You can utilize this repository in order to receive some analytical data regarding HTTP server logs from the following web server: https://s3.amazonaws.com/tcmg476/http_access_log

In order to access the data:
1. Clone this repository onto a Linux OS (I used Ubuntu 18.04 to create the files)
2. Run the file 'read_log.py' by using the following command

$ python3 read_log.py
3. That's it!

The log file will create new text files for each month represented by the log, which follow this naming convention: YY_MM-MonYY.txt (e.g. 94_10-Oct94.txt)


Please make sure to only run read_log.py once! If you need to run multiple times, delete the new text files so that they do not include repeated information, doubling the size of the file!

Enjoy!
