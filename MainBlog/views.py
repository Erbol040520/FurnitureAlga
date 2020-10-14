from django.shortcuts import render
from django.views.generic import DetailView
from .models import FurnitureCard
from .models import FurnitureCardTwo


def index(request):
    model = FurnitureCardTwo.objects.all()
    return render(request, 'MainBlog/index.html',{'model':model})


class FurnitureDetailView(DetailView):
    model = FurnitureCardTwo
    template_name = 'MainBlog/detail_view.html'
    context_object_name = 'post_el'
