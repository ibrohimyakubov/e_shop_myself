from .models import Category


def category_rendered(request):
    context = {
        'categories': Category.objects.all(),
    }
    return context
