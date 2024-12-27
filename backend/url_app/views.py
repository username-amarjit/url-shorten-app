import json
import traceback
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from url_app.services import URLSrv

log = logging.getLogger(__name__)

# Create your views here.

import logging

log = logging.getLogger(__name__)

# @permission_classes((IsAuthenticated,))
@csrf_exempt
@api_view(['POST','GET','PATCH','DELETE'])
def url_shortner_view(request):
    response_msg = ""    
    response_code = ""
    
    user = request.user
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        data = json.loads(request.body)
        srv = URLSrv(user,data)
        data,msg,code = srv.create_record()
        
        return JsonResponse({"data":data,"response_msg":msg,"response_code":code})
    

    
# @permission_classes((IsAuthenticated,))
@csrf_exempt
@api_view(['GET'])
def redirect_view(request,path):
    response_msg = ""    
    response_code = ""
    
    user = request.user
    if request.method == 'GET':
        url_srv = URLSrv(request.user)
        long_url = url_srv.redirect_to_url(path)
        if long_url is not None:
            return HttpResponseRedirect(long_url)        
        else:
            return HttpResponse("<h2> Long URL not found</h2>")
    else:
        return JsonResponse({"data":[],"response_msg":"request method not allowed","response_code":"V_10"})
    
    
