from io import StringIO
#from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def from_template(template):
    target_file = StringIO()

    template = DocxTemplate(template)
    context = {
    	employee:
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

    target_file = StringIO()
    template.render(context)
    template.save(target_file)

    return target_file

import os
print(os.path.abspath('Model-adeverinta-angajator.docx'))


from_template('Model-adeverinta-angajator.docx')