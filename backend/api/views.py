import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    print(request.GET, "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    body = request.body
    try:
        data=json.loads(body)

    except:
        pass
    print(data)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    return JsonResponse(data)