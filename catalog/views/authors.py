from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from ..models import Author


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.can_mark_returned'
    model = Author
    success_url = reverse_lazy('authors')
