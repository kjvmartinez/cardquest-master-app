from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.models import PokemonCard, Trainer, Collection
from cardquest.forms import TrainerForm, CollectionForm

from django.urls import reverse_lazy


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TrainerList, self).get_queryset(*args, **kwargs)
        return qs


class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')


class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')


class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collections.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(CollectionList, self).get_queryset(*args, **kwargs)
        return qs


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection-list')


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection-list')


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection-list')
