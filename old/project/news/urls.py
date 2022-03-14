from django.urls import path
from .views import NewsList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SearchListView
# импортируем наше представление

#from django.views.decorators.cache import cache_page
urlpatterns = [# path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', NewsList.as_view()), # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', (PostDetailView.as_view()), name='post_detail'), #cache_page(100) # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('search/', SearchListView.as_view(), name="search"),
]

"""from django.urls import path
from .views import ProductList, ProductDetail  # импортируем наше представление

urlpatterns = [# path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', ProductList.as_view()),# т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view()), # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]"""