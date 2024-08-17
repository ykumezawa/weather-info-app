from django.http import HttpResponse
from django.views.generic import TemplateView

#HttpResponseとはdjangoが準備をしているクラス
def helloworldfunction(request):
    returnedobject = HttpResponse('helloworld')
    return returnedobject

def someview(request):
    print(path(__file__).resolve().parent)
    return HttpResponse('')


class HelloWorldClass(TemplateView):
    template_name = 'hello.html'

