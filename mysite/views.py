import logging

from django.http import HttpResponse
from . import tasks

logger = logging.getLogger('views')

def test(request):
    logger.warn('Test log from view')

    tasks.test.delay()
    
    return HttpResponse('Ok')
