## Data Engineer Steel Eye Submission
1. run python main.py to perform perform downloading, extracting csv content , stores all intermediary files in temp folder and then uploading to S3.

## Break Down of code

Stage 1:
Downloading Zip File and Extracting content

Stage 2:
Parsing required info from xml and converting to csv

Stage 3:
Uploading csv to AWS

Main.py
Runs all the stages with logs