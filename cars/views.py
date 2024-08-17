from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.models import Car
from cars.forms import CarModelForm


class IndexRedirectView(RedirectView):
    permanent = False
    url = reverse_lazy('cars_list')


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        search = self.request.GET.get('search')
        query_all_cars = super().get_queryset().order_by('model')
        cars = query_all_cars.filter(
            Q(model__icontains=search) | Q(brand__name__icontains=search)
        ) if search else query_all_cars
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')