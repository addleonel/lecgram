
import datetime
from django.http import HttpResponse, JsonResponse, FileResponse

def first_view(request):
    """
    This is my first view in Django
    """
    # print(dir(request))
    return HttpResponse('<h1>HELLO EVERYONE HERE IS {time}</h1>'.format(
        time=datetime.datetime.now().strftime('%Y %b %dth, %H:%M')
    ), content_type='text/plain')

def get_request_attributes(request):
    """
    HttpRequest object and its attributes
    for more info(Django 3.1):
    https://docs.djangoproject.com/en/3.1/ref/request-response/#httprequest-objects
    """
    # This is not a JSON serializable
    # because the values are objects of type LimitedStream 
    request_attributes= {
        'GET': request.GET, # QueryDict object
        'FILES': request.FILES,
        'COOKIES': request.COOKIES,
        #'META': request.META,
        'POST': request.POST, # QueryDict object
        'method': request.method,
        'body': request.body,
        'path': request.path,
        'path_info': request.path_info,
        'scheme': request.scheme,
        'encoding': request.encoding,
        'content_type': request.content_type,
        'content_params': request.content_params,
        #'headers': request.headers,
        'user': request.user,
        # methods
        'host': request.get_host(),
        'port': request.get_port(),
        'full_path': request.get_full_path(),
        'build_absolute_uri': request.build_absolute_uri(),
        'is_secure': request.is_secure(),
    }
    response = HttpResponse()
    for key, value in request_attributes.items():
        response.write(f'<p>key={key}, value={value}, type={type(value)}</p>')
    
    response.set_cookie('NAME', 'Nicola Tesla')
    response.set_cookie('MESSAGE', 'I\'m trying to code right now')
    return response


def get_excel_file(request):
    response = HttpResponse('This is my messgae', content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="my_message.xls"'

    return response


def get_json_format(request):
    """
    This is to returning a JSON format
    """
    
    # This is a JSON serializable
    my_data = {
        'name': 'Leonel',
        'age': 22,
        'email': 'example23@gmail.com',
        'password': 'QWEWrerws#$%&qwettrt==#()\\/23332eer',
        'city': 'Huanuco',
        'country': 'Peru',
        'avatar': 'https://avatar.example.com/photo=3434hbcdhbdss',
        'bio': 'I think My best is coming'
    }

    prime_numbers = [2, 3, 5, 7, 11]
    return JsonResponse(prime_numbers, safe=False)

def get_files(request):
    response = FileResponse(open('lecgram/settings.py', 'rb'))
    return response