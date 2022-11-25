import os

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render, get_list_or_404

from certificates.models import Certificate
from utils.pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


# from utils.pagination import make_pagination

def home(request):
    certificates = Certificate.objects.all().order_by('-id')
    page_obj, pagination_range = make_pagination(request, certificates, PER_PAGE)

    return render(request, 'certificates/pages/home.html', context={
        'certificates': page_obj,
        'pagination_range': pagination_range
    })


def certificate(request, id):
    certificate = get_object_or_404(Certificate, pk=id)

    return render(request, 'certificates/pages/certificate-view.html', context={
        'certificate': certificate,
        'is_detail_page': True,
    })


def category(request, category_id):
    certificates = get_list_or_404(
        Certificate.objects.filter(
            category__id=category_id,
        ).order_by('-id')
    )
    page_obj, pagination_range = make_pagination(request, certificates, PER_PAGE)

    return render(request, 'certificates/pages/category.html', context={
        'certificates': page_obj,
        'pagination_range': pagination_range,
        'title': f'{certificates[0].category.name} - Category | '
    })


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    certificates = Certificate.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        )
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, certificates, PER_PAGE)

    return render(request, 'certificates/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'certificates': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })
