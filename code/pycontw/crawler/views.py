from collections import namedtuple, OrderedDict

import logging

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseBadRequest, Http404, HttpResponse

from django_q.tasks import async, result, Task
from django_q.models import OrmQ
from django_q.humanhash import humanize
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger = logging.getLogger(__name__)


@require_GET
def view_task(request, id):
    task = get_object_or_404(Task, id=id)
    result = task.result
    if task.func == 'crawler.tasks.crawler_job':
        if type(result) is type(OrderedDict()): 
            return render(request, 'crawler/tasks_detail.html', {
                #'ret': result['ret'],
                #'status': result['status'],
                #'version': result['version'],
                'result': result['crawler_job'],
            })
        else:
            return render(request, 'crawler/tasks_detail.html', {
                'result': result,
            })
    if task.func == 'crawler.tasks.job':
        print(result)
        if type(result) is type(OrderedDict()): 
            return render(request, 'crawler/tasks_detail.html', {
                #'ret': result['ret'],
                #'status': result['status'],
                #'version': result['version'],
                'result': result['crawler_job'],
            })
        else:
            return render(request, 'crawler/tasks_detail.html', {
                'result': result,
            })
    return Http404(
        'Given task of type %s does not have the result template '
        'to be rendered yet.'
        % task.func
    )


def crawler(request):
    # Select crawler in queue
    queue_crawler = OrmQ.objects.all().order_by('lock')

    # Select finidhed crawler
    complete_crawler = Task.objects.all().filter(
        func__exact='crawler.tasks.job',
    )
    return render(request, 'crawler/tasks_crawler.html', {
            'queue_crawler': queue_crawler,
            'complete_crawler': complete_crawler
    })