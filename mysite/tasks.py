import logging

from celery import shared_task

logger = logging.getLogger('celery_worker')

@shared_task
def test():
    logger.warn('Test from worker')
    
    return True