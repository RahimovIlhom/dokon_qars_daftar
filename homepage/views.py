import operator
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Qarzdorlar, Qarzdor
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView

class HomePageView(TemplateView):
    template_name = 'home.html'

def qarzdorlarView(request):
    qarzdorlar = Qarzdorlar.objects.all()
    ordered = sorted(qarzdorlar, key=operator.attrgetter('name'))
    return render(request, 'qarzdorlar.html', {
        'qarzdorlar': ordered
    })

def qarzdorView(request, id):
    qarzdor = Qarzdorlar.objects.get(id=id)
    qarzlar = Qarzdor.objects.filter(qarzdorlar=qarzdor)
    list1 = []
    for i in qarzlar.all():
        list1.append(int(i.price))
    summa = sum(list1)
    return render(request, 'qarzdor.html', {
        'qarzlar': qarzlar,
        'qarzdor': qarzdor,
        'summa': summa,
    })

class QarzdorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Qarzdorlar
    template_name = 'create_qarzdor.html'
    fields = ['name', 'phone', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

class QarzCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Qarzdor
    template_name = 'create_qarz.html'
    fields = ['product', 'price', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.qarzdorlar_id = self.kwargs['id']
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

class QarzdorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Qarzdorlar
    fields = ['name', 'phone', ]
    template_name = 'qarzdor_edit.html'

    def test_func(self):
        return self.request.user.is_superuser

class QarzUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Qarzdor
    fields = ['product', 'price', ]
    template_name = 'qarz_edit.html'

    def test_func(self):
        return self.request.user.is_superuser

class QarzdorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Qarzdorlar
    template_name = 'qarzdor_delete.html'
    success_url = reverse_lazy('qarzdorlar')

    def test_func(self):
        return self.request.user.is_superuser


class QarzDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Qarzdor
    template_name = 'qarz_delete.html'
    # success_url = reverse_lazy('qarzdor')

    def get_success_url(self, **kwargs):
        return reverse('qarzdor', args=[str(self.object.qarzdorlar.pk)])

    def test_func(self):
        return self.request.user.is_superuser