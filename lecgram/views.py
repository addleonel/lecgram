
import datetime
from django.http import HttpResponse, JsonResponse

def first_view(request):
    """
    This is my first view in Django
    """
    # print(dir(request))
    return HttpResponse('<h1>HELLO EVERYONE HERE IS {time}</h1>'.format(
        time=datetime.datetime.now().strftime('%Y %b %dth, %H:%M')
    ))

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
    return JsonResponse(my_data)