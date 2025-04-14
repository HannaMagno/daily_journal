from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import JournalEntry
from .forms import JournalEntryForm

class EntryListView(ListView):
    model = JournalEntry
    template_name = 'entries/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 5

    def get_queryset(self):
        return JournalEntry.objects.all().order_by('-date_posted')

class EntryDetailView(DetailView):
    model = JournalEntry
    template_name = 'entries/entry_detail.html'

class EntryCreateView(CreateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = 'entries/entry_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

class EntryUpdateView(UpdateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = 'entries/entry_form.html'

class EntryDeleteView(DeleteView):
    model = JournalEntry
    template_name = 'entries/entry_confirm_delete.html'
    success_url = reverse_lazy('entry-list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

def entry_search(request):
    query = request.GET.get('q')
    if query:
        entries = JournalEntry.objects.filter(
            title__icontains=query
        ) | JournalEntry.objects.filter(
            content__icontains=query
        ) | JournalEntry.objects.filter(
            tags__icontains=query
        )
    else:
        entries = JournalEntry.objects.none()
    return render(request, 'entries/entry_search.html', {'entries': entries, 'query': query})

def home(request):
    context = {
        'total_entries': JournalEntry.objects.count(),
        'latest_entry': JournalEntry.objects.first(),
    }
    return render(request, 'entries/home.html', context)