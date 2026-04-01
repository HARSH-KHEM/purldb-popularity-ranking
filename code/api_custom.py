"""
PageRank-based package popularity ranking for PURLdb.
Part of GSoC proposal prototype.
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from packagedb.models import Package


class PageSizePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 20
    page_size_query_param = "page_size"


@api_view(["GET"])
def top_packages(request):
    limit = min(int(request.GET.get("limit", 10)), 50)

    packages = Package.objects.exclude(rank_score=None)\
        .order_by("-rank_score")[:limit]

    data = [
        {
            "package_url": p.package_url,
            "rank_score": round(p.rank_score, 4)
        }
        for p in packages
    ]

    return Response({
        "count": len(data),
        "results": data
    })
