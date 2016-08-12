from django.views.generic import DetailView, ListView, RedirectView, UpdateView, DetailView

from .models import Resume


class ResumeListView(ListView):
    model = Resume


class ResumeDetailView(DetailView):
    model = Resume

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = context['resume'].person
        return context
