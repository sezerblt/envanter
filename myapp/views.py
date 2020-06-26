from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Room,Apartment,Building,Furniture


def home(request):
    context = {
        'posts': Apartment.objects.all()
    }
    return render(request, 'myapp/home.html', context)


class ApartmentListView(ListView):
    model = Apartment
    template_name = 'myapp/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


class ApartmentDetailView(DetailView):
    model = Apartment


class ApartmentCreateView(LoginRequiredMixin, CreateView):
    model = Apartment
    fields = ['apartmentName', 'building','rooms']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BuildingCreateView(CreateView):
    model = Building
    fields = ['buildingName']

class FurnitureCreateView(CreateView):
    model = Furniture
    fields = ['furnitureName', 'furniturePrice']

class RoomCreateView(CreateView):
    model = Room
    fields = ['roomName', 'furnitures']

"""
    apartmentName = models.CharField(max_length=40, verbose_name="Daire Ad")
    address = models.TextField(max_length=150, verbose_name="Adres", blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Bina")
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Odalar")
    apartmentImage = models.ImageField(default='apartment.png', upload_to='apartment_img')
  """
class ApartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Apartment
    fields = ['apartmentName','address' ,'building','rooms']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ApartmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Room
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BuildingDeleteView(CreateView):
    model = Building
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class FurnitureDeleteView(CreateView):
    model = Furniture
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class RoomDeleteView(CreateView):
    model = Room
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'myapp/about.html',{'title':'Detaylar'})

