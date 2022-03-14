from django.forms import ModelForm, BooleanField, Textarea, CharField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Проверьте данные!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['name', 'author', 'date', 'category', 'text', 'rating']
        #fields = ['name', 'date', 'text', 'category', 'quantity', 'check_box'] rating