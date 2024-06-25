# file2.py
from django.http import HttpResponse
import shutil
import os
import time
from .mod_create_website import website_creation as wc
from .mod_string_es import strings as es
from .mod_string_de import strings as de
from .mod_string_en import strings as en
from .mod_string_kn import strings as kn
from .mod_string_hi import strings as hi

def create_main(lang, name, uploaded_file, template, type):
    # Determine string values based on language
    if lang == "Deutsch":
        s1, s2, s3, s4, s5, s6, s7 = de()
    elif lang == "Española":
        s1, s2, s3, s4, s5, s6, s7 = es()
    elif lang == 'Kannada':
        s1, s2, s3, s4, s5, s6, s7 = kn()
    elif lang == 'Hindi':
        s1, s2, s3, s4, s5, s6, s7 = hi()
    else:
        s1, s2, s3, s4, s5, s6, s7 = en()

    # Generate unique output name
    output_name = f'WebsiteCreation_{name}_{time.strftime("%Y%m%d_%H%M%S")}.zip'

    # Create website content in-memory
    zip_buffer = wc(name, uploaded_file, template, type)

    # Prepare HTTP response with the in-memory ZIP file
    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{output_name}"'

    return response, f"{output_name} {s4}", f"{output_name} {s1}"
