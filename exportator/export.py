from io import BytesIO
from docx2pdf import convert
#from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

import os.path
from shutil import copyfile
import sys
import subprocess
import re

def from_template(template_string, output_string):
 #   target_file = BytesIO()

    template = DocxTemplate(template_string)
    context = {
    	'employee':
    	{
    		'first_name':'ghita',
    		'second_name':'zidaru',
    		'duty':'dulgher',
    		'type':'intreaga',
    		'date_hire':'12/12/1212',
    		'date_fire':'12/12/1212',

    	}
    }  # gets the context used to render the document

    #img_size = Cm(7)  # sets the size of the image
    #sign = InlineImage(template, signature, img_size)
    #context['signature'] = sign  # adds the InlineImage object to the context

#    target_file = BytesIO()
    template.render(context)
    template.save(output_string)

#    return target_file

def convert_to(folder, source, timeout=None):
    args = ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        return filename.group(1)

import os
print(os.path.abspath('adeverinta_angajat.docx'))

from_template('adeverinta_angajat.docx', 'adeverinta_angajat-generat.docx')


convert_to('.', 'adeverinta_angajat-generat.docx')