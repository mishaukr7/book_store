from .models import Book
from django.views.generic import ListView, CreateView, UpdateView
from .forms import BookForm
from django.urls import reverse
from django.shortcuts import redirect
from request.models import Request


class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'
    paginate_by = 6

    def get_ordering(self):
        ordering = self.request.GET.get('ordering')
        if ordering not in ['publish_date', '-publish_date']:
            ordering = '-publish_date'
        return ordering


class BookCreateView(CreateView):
    model = Book
    template_name = 'catalog/book_form.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('catalog:book_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:

            return redirect('catalog:book_list')
        return super(BookCreateView, self).dispatch(request,
            *args, **kwargs)


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/book_form.html'

    def get_success_url(self):
        return reverse('catalog:book_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:

            return redirect('catalog:book_list')
        return super(BookUpdateView, self).dispatch(request,
            *args, **kwargs)


class RequestListView(ListView):
    model = Request
    template_name = 'catalog/request_list.html'
    context_object_name = 'requests'
    queryset = Request.objects.all().order_by('-time')[:10]


