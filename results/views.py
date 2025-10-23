from django.shortcuts import render, get_object_or_404
from .models import Category, Result, Area

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


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    events = category.events.all()
    results = Result.objects.filter(event__in=events)
    return render(request, 'results/category_detail.html', {
        'category': category,
        'events': events,
        'results': results
    })
