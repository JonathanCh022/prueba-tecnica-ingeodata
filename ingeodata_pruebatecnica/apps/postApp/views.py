from django.http import HttpResponseRedirect
from ingeodata_pruebatecnica.apps.postApp.form import UserForm
from ingeodata_pruebatecnica.apps.postApp.models import User
from django.views import View

# Create your views here.


class MyFormView(View):
    form_class = UserForm
    template_name = 'form_template.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                form.save()
            finally:
                pass
            return HttpResponseRedirect('/show')