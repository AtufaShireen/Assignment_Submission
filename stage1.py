from lxml import etree
import requests
import zipfile
# import boto3
# 
class DownloadFiles:
    '''
    Fetches file content from web, downloads zip file, extracts zip file content in the specified folder.
    '''
    def __init__(self,file_link,save_dir):
        self.file_link = file_link
        self.save_dir = save_dir

    def get_download_file(self):
        '''Fetches file content from web with first download link'''
        print(self.file_link)
        res = requests.get(self.file_link)
        # print(res.content.decode())
        doc = etree.fromstring(res.content)
        zip_link = doc.find('result').find('doc').find("str[@name='download_link']").text
        return zip_link

    @staticmethod
    def unzip_xml(save_dir:str)->None:
        '''Unzips downloaded file in save_dir'''
        with zipfile.ZipFile(f"{save_dir}/dlts.zip", 'r') as zip_ref:
            zip_ref.extractall(save_dir)

    def download_zip(self, chunk_size:int=128)->None:
        '''Downloads unzipped file in save_dir folder'''
        url = self.get_download_file()
        r = requests.get(url, stream=True)
        with open(f"{self.save_dir}/dlts.zip", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)
        self.unzip_xml(self.save_dir)
        return None



