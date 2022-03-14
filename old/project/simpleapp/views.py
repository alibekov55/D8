#Импортируем кеширование
#from django.views.decorators.cache import cache_page
#from django.core.cache import cache

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from datetime import datetime
from .models import Product #Products, Category,
from .filters import ProductFilter
from .forms import ProductForm  # импортируем нашу форму


# из списка на главной странице уберём всё лишнее
class Products(ListView):
    model = Product
    template_name = 'simpleapp/products_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class ProductCreateView(CreateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'simpleapp/product_detail.html'
    context_object_name = 'product'


# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)

# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'simpleapp/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'






"""class Products(ListView):
    model = Products  # указываем модель, объекты которой мы будем выводить
    template_name = 'simpleapp/products_list.html'  # указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = ['-price']
    queryset = Products.objects.order_by('-id')  # настроили пораметр отображения более новый продукт
    paginate_by = 1
    form_class = ProductForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)"""


"""class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1
    form_class = ProductForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

class ProductDetail(DetailView):
    model = Product
    template_name = 'simpleapp/product_list.html'
    context_object_name = 'product'"""

"""from django.views.generic import ListView, DetailView
from .models import Product, Category
from datetime import datetime


class ProductList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'simpleapp/products_list.html'  # указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Product.objects.order_by('-id')  # настроили пораметр отображения более новый продукт

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'simpleapp/product_list.html'
    context_object_name = 'product'
"""