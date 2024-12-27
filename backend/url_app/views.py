import traceback
import logging
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from url_app.services import URLSrv

log = logging.getLogger(__name__)

# Create your views here.

import logging

log = logging.getLogger(__name__)

@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(['POST','GET','PATCH','DELETE'])
def urlShortnerView(request):
    response_msg = ""    
    response_code = ""
    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        