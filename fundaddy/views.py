from django.http import HttpResponse


def test_kids(request):
    html = "<html><body>Congratulations for accepting <b>Pawan Dubey</b> as you papa.</body></html>"
    return HttpResponse(html)
