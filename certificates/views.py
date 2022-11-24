import os

from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from certificates.models import Certificate
from utils.pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


# from utils.pagination import make_pagination

def home(request):
    certificates = Certificate.objects.all().order_by('-id')
    print(certificates[0].cover.url)
    print("++++++++++++++++++++++++++++++++++++++")
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

