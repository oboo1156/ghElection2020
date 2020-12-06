from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from .models import Region,Comment
from .forms import CommentForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'abatoo/home.html'


class RegionListView(ListView):
    context_object_name = 'regions'
    model = Region
    template_name = 'abatoo/region.html'


class RegionDetailView(DetailView):
    context_object_name = 'region'
    model = Region
    template_name = 'abatoo/detail.html'


class CommentFormView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'abatoo/comment_add.html'
    success_url = reverse_lazy('abatoo:list')

    def form_valid(self, form):
        form.instance.region_id = self.kwargs['pk']
        return super().form_valid(form)