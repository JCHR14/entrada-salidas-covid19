# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def setInfoPagination(data, page, lote=10):
    paginator = Paginator(data, lote)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    # Get the index of the current page
    index = data.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    totaldatos = len(data)
    return {
        'data': data,
        'page_range': page_range,
        'totaldatos': totaldatos
    }
