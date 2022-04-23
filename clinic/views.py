from django.views.generic import ListView
from .models import *


class IndexView(ListView):
    model = Clinic
    template_name = 'clinic/index.html'
    context_object_name = 'clinics'


class CategoryView(ListView):
    model = Clinic
    template_name = 'clinic/index.html'
    context_object_name = 'clinics'

    def get_queryset(self):
        return super().get_queryset().filter(directions__id=int(self.kwargs.get('pk')))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        try:
            context['direction'] = Direction.objects.get(id=self.kwargs.get('pk'))
        except (Direction.DoesNotExist, Direction.MultipleObjectsReturned):
            pass
        return context
