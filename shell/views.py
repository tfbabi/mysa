from django.http import HttpResponseRedirect

# Create your views here.

def stream_response(request):
    return HttpResponseRedirect("http://192.168.6.79:9527")








