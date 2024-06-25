import tempfile
from .mod_create_html import create_html as ch
import os
import pandas as pd
from django.conf import settings

def website_creation(college, file1, template, type):
    file1 = file1
    college = college

    def content_creation(file2, type):
        file2.seek(0)
        if type.endswith('csv'):
            df = pd.read_csv(file2)
        elif type.endswith('xlsx'):
            df = pd.read_excel(file2)

        if not df.empty:
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
        else:
            raise ValueError("DataFrame is empty or columns are missing.")

    def file_creation(root_directory, template, dict1):
        for root, dirs, files in os.walk(root_directory):
            if not dirs:
                dir_name = os.path.basename(root)
                temp_dir = tempfile.mkdtemp()
                temp_file = os.path.join(temp_dir, dir_name + '.html')
                ch(template, dir_name, temp_file, dict1)

    try:
        dict1 = content_creation(file1, type)
        file_creation(tempfile.mkdtemp(), template, dict1)  # Use temporary directory
        return "Files are created successfully in a temporary directory"

    except Exception as e:
        return f"Error: {str(e)}"
