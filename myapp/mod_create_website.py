from .mod_create_html import create_html as ch
import os
import pandas as pd
from django.conf import settings
def website_creation(college,file1,template,type):
    file1 = file1
    college =college
    """ The below function is for reading and saving the file content """


    def content_creation(file2,type):
        # Assuming file2 is a file-like object
        file2.seek(0)
        if type.endswith('csv'):
            df = pd.read_csv(file2)
        elif type.endswith('xlsx'):
            df = pd.read_excel(file2)
        # Assuming the DataFrame columns are in a specific order
        years = df.iloc[:, 0]
        subjects = df.iloc[:, 1]
        usn = df.iloc[:, 2]
        names = df.iloc[:, 3]
        email = df.iloc[:, 4]
        mobile_number = df.iloc[:, 5]
        photos = df.iloc[:, 6]

        dict1 = {
            'years': years,
            'usn': usn,
            'subjects': subjects,
            'names': names,
            'email': email,
            'mobile_number': mobile_number,
            'photo': photos,
        }
        return dict1
    
    
    """The below function is to create the directory structure """
    def Directory_creation(college,dict1):
        import os
        for year, usn, subject in zip(dict1['years'], dict1['usn'], dict1['subjects']):
            os.makedirs(os.path.join(settings.MEDIA_ROOT,college+'/'+str(year)+'/'+subject+'/'+usn),exist_ok =True)

    """This below function will help to create files inside a folder """
    def file_creation(root_directory,template,dict1):
        
        for root, dirs, files in os.walk(root_directory):
            if not dirs:
                dir_name = os.path.basename(root)
                string=os.path.join(root, dir_name + '.html')
                ch(template,dir_name,string,dict1)
    
    #call all the functions here for making it easy to use for User
    dict1= content_creation(file1,type)
    Directory_creation(college,dict1)
    file_creation(os.path.join(settings.MEDIA_ROOT,college),template,dict1)             
    return "Directory and Files are created successfully"