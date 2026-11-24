from pyspark.sql.functions import *

class   Transform:
    
    
    def dropColumn(self,df,name):
        df = df.drop(*name)
        return df
    
    def renameColumn(self,df, oldName, newName):
        df = df.withColumnRenamed(oldName,newName)
        return df
    
    def dropDuplicates(self,df,args):
        if len(args) == 0:
            df = df.dropDuplicates()
        else:   
            df = df.dropDuplicates([*args])
        return df
