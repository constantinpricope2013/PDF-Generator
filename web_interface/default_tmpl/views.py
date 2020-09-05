from django.shortcuts import render
from .forms import DeafaultTemplateForm
from .models import Default_Templates

#from templated_docs import fill_template
#from templated_docs.http import FileResponse

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
        form = DeafaultTemplateForm(data=request.POST)
        if form.is_valid():
            doctype = form.cleaned_data['format']

            employee_id = form.data['employee']
            default_tmpl_id = form.data['default_tmpl']

            employee = Employees.objects.get(pk=employee_id)
            default_tmpl = Default_Templates.objects.get(pk=default_tmpl_id)

            #filename = fill_template(default_tmpl_id.template_path, employee, output_format=doctype)
    else:
        form = DeafaultTemplateForm()

    template_name = "default_tmpl/default_tmpl-home.html"
    context = {
        'form': form,
        'employee': employee,
        'default_tmpl': default_tmpl,
    }
    return render(request, template_name, context)