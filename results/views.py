from django.shortcuts import render, get_object_or_404
from .models import Category, Result, Area




# views.py
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    # Calculate total points per area
    area_points = {}
    areas = Area.objects.all()
    for area in areas:
        points = 0
        for result in area.result_set.all():
            if result.position == 1:
                points += 5 if result.event.category.name != 'Group Items' else 12
            elif result.position == 2:
                points += 3 if result.event.category.name != 'Group Items' else 8
            elif result.position == 3:
                points += 1 if result.event.category.name != 'Group Items' else 5
        area_points[area.name] = points

    # Sort by points descending
    area_points = dict(sorted(area_points.items(), key=lambda x: x[1], reverse=True))

    categories = Category.objects.all()
    return render(request, 'results/home.html', {
        'area_points': area_points,
        'categories': categories
    })


from django.db.models import Q, Exists, OuterRef, Prefetch
from django.shortcuts import get_object_or_404, render
from results.models import Category, Result

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    # "Filled" = area chosen OR a winner name typed
    filled = Result.objects.filter(Q(area__isnull=False) | ~Q(name__exact=''))

    events = (
        category.events
        .annotate(has_results=Exists(filled.filter(event=OuterRef('pk'))))
        .filter(has_results=True)
        .order_by('date', 'name')
        .prefetch_related(
            Prefetch('results', queryset=filled.select_related('area').order_by('position'),
                     to_attr='filled_results')
        )
    )
    return render(request, 'results/category_detail.html', {'category': category, 'events': events})