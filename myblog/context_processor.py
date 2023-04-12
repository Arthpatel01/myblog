from blog.models import Category


def common_context(request):
    context = {}
    context['categories'] = Category.objects.all()
    return context