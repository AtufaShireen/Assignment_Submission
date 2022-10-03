from stage1 import DownloadFiles
from stage2 import XmlTagParser
from stage3 import AWSOps

import logging
import os
import glob

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

def main(f:str) -> None:
    '''Implements 
    Stage 1: Downloading Zip File and Extracting content
    Stage 2: Parsing required info from xml and converting to csv
    Stage 3: Uploading csv to AWS '''
    logging.info("Download started")
    x = DownloadFiles(f,'./temp')
    x.download_zip()
    logging.info("Download Zip and extracted files")
    
    file_name = glob.glob('./temp/*.xml')[0]
    logging.info("Generating CSV Files")
    x = XmlTagParser(file_name,'./temp/main.csv')
    x.get_finstrmatrrs()
    logging.info("CSV File generation completed!")

    logging.info("Uploading to AWS")
    x = AWSOps()
    x.upload_bucket('./temp/main.csv')
    logging.info("Upload Completed !")

    return None


if __name__=='__main__':
    file_link = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
    main(file_link)