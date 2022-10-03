from lxml import etree
class XmlTagParser:
    def __init__(self,path, write_path)->None:
        self.path = path
        self.write_path = write_path

    def clean_tree(self,source:str):
        '''Removes attributes from the content'''
        root = etree.parse(source)

        # Iterate through all XML elements
        for elem in root.getiterator():
            # Skip comments and processing instructions,
            # because they do not have names
            if not (
                isinstance(elem, etree._Comment)
                or isinstance(elem, etree._ProcessingInstruction)
            ):
                # Remove a namespace URI in the element's name
                elem.tag = etree.QName(elem).localname

        # Remove unused namespace declarations
        etree.cleanup_namespaces(root)
        return root
    
    def get_rootfinstrm(self)->iter:
        '''Fetches list of tags with FinInstrm containing all the required attributes'''
        tree = self.clean_tree(self.path)
        finstrm = tree.getroot()[1][0][0].findall('FinInstrm')
        return iter(finstrm)

        
    def get_finstrmatrrs(self)->None:
        finstrms = self.get_rootfinstrm()
        with open(self.write_path,'w+') as f:
            f.seek(0)
            f.write("FinInstrmGnlAttrbts.Id,FinInstrmGnlAttrbts.FullNm,FinInstrmGnlAttrbts.ClssfctnTp,FinInstrmGnlAttrbts.CmmdtyDerivInd,FinInstrmGnlAttrbts.NtnlCcy,Issr")
            while True:
                try:
                    attr = next(finstrms)
                    id = attr[0].find('FinInstrmGnlAttrbts').find('Id').text
                    fullname = attr[0].find('FinInstrmGnlAttrbts').find('FullNm').text
                    clftp = attr[0].find('FinInstrmGnlAttrbts').find('ClssfctnTp').text
                    cmdty = attr[0].find('FinInstrmGnlAttrbts').find('CmmdtyDerivInd').text
                    ntnl = attr[0].find('FinInstrmGnlAttrbts').find('NtnlCcy').text
                    issr = attr[0].find('Issr').text
                    f.write(f"{id},{fullname},{clftp},{cmdty},{ntnl},{issr}")
                except StopIteration:
                    break
        return None
        

