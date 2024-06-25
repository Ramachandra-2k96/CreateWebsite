# file1.py
from .mod_create_html import create_html as ch
import pandas as pd
from io import BytesIO
import zipfile

def website_creation(college, file1, template, type):
    """Function to create website content dynamically."""

    def content_creation(file2, type):
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

    def Directory_creation(college, dict1):
        # Simulating directory creation (not needed in-memory)
        pass

    def file_creation(root_directory, template, dict1):
        # Simulating file creation (not needed in-memory)
        pass

    # Call functions
    dict1 = content_creation(file1, type)
    Directory_creation(college, dict1)
    
    # Create in-memory ZIP file
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for year, usn, subject in zip(dict1['years'], dict1['usn'], dict1['subjects']):
            filename = f"{college}/{year}/{subject}/{usn}.html"
            df = pd.DataFrame(dict1)
            index = df.loc[df['usn'] == usn].index[0]
            name = dict1['names'][index]
            email = dict1['email'][index]
            branch = dict1['subjects'][index]
            m_number = dict1['mobile_number'][index].astype(str)
            template.seek(0)
            photo=dict1['photo'][index]
            info1 = template.read().decode('ascii')
            info1 = info1.replace('$NAME',name)
            info1 = info1.replace('$BRANCH',branch)
            info1 = info1.replace('$EMAIL',email)
            info1 = info1.replace('$PHONE',m_number)
            info1 = info1.replace('$PHOTO',photo)
            zip_file.writestr(filename, info1)
    zip_buffer.seek(0)
    return zip_buffer

