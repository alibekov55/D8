from django.db.models.fields.related import ForeignKey
from django_filters import FilterSet
from .models import Post


class SearchFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'name': ['icontains'], # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то, что запросил пользователь
            'date': ['gt'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'category': ['exact'],
            'author': ['exact'],  # цена должна быть меньше или равна тому, что указал пользователь
        }