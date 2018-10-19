import json

class DatabaseManager(object):
    
    dictRoot = dict()

    def __init__(self, strFile=None):
        print("initialised")
        self.dictRoot['pages'] = {}

        if strFile != None:
            with open(strFile, 'r') as f:
                self.dictRoot = json.load(f)

    def createPage(self,intPageNo):
        strPageName = "page_" + '{}'.format(intPageNo)
        dictTmpPage = dict()
        dictTmpPage[strPageName] = dict() 
        #self.dictRoot["pages"] = []
        arrPages = self.dictRoot["pages"]
        arrPages.append(dictTmpPage)
        return strPageName

    def addRecordToCurrentPage(self,strField,strRect,strPage):
        dictTmpPage = self.dictRoot["pages"][strPage]
        dictTmpPage[strField] = strRect
