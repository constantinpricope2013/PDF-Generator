from django.shortcuts import render
from django.conf import settings
from .forms import DeafaultTemplateForm
from .models import Default_Templates
from io import BytesIO

from django.http import HttpResponse
#from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

#Change path to parent directory for aneasier acces to files
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from employee.models import Employees


def default_tmpl_home(request):
    employee = Employees.objects.all()
    default_tmpl = Default_Templates.objects.all()

    if request.method == 'POST':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        form = DeafaultTemplateForm(data=request.POST)
        if form.is_valid():
            doctype = form.cleaned_data['format']

            employee_id = form.data['employee']
            default_tmpl_id = form.data['default_tmpl']

            employee = Employees.objects.get(pk=employee_id)
            default_tmpl = Default_Templates.objects.get(pk=default_tmpl_id)

            context_data = {
                'employee': employee,
            }

            docx_title = 'adeverinta_' + employee.last_name + '_' + employee.first_name + '.docx'

            template = DocxTemplate(settings.BASE_DIR + default_tmpl.template_path)

            template.render(context_data)

            #template.save('adeverinta_angajat-generat.docx')
            #response.write(template)
            #return response
            f = BytesIO()
            template.save(f)
            length = f.tell()
            f.seek(0)
            response = HttpResponse(
                f.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            response['Content-Disposition'] = 'attachment; filename=' + docx_title
            response['Content-Length'] = length
            return response
    else:
        form = DeafaultTemplateForm()

    template_name = "default_tmpl/default_tmpl-home.html"
    context = {
        'form': form,
        'employee': employee,
        'default_tmpl': default_tmpl,
    }
    return render(request, template_name, context)