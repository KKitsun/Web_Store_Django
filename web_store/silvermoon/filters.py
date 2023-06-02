import django_filters
from .models import Game
from django.forms.widgets import TextInput

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = {
            'title': ['icontains'],
            'genre': ['exact'], 
            'subgenre': ['exact'], 
            'visual': ['exact'], 
            'theme': ['exact'], 
            'feature': ['exact'], 
            'playersType': ['exact']
        }

    def __init__(self, *args, **kwargs):
        super(GameFilter, self).__init__(*args, **kwargs)
        self.filters['title__icontains'].label = "Пошук за назвою"
        self.filters['genre'].label = "Жанри"
        self.filters['subgenre'].label = "Піджанри"
        self.filters['visual'].label="Візуальний стиль і перспектива"
        self.filters['theme'].label="Тематика й атмосфера"
        self.filters['feature'].label="Особливості"
        self.filters['playersType'].label="Гравці"
        self.filters['genre'].extra.update(
            {'empty_label': 'Усі жанри'})
        self.filters['subgenre'].extra.update(
            {'empty_label': 'Усі піджанри'})
        self.filters['visual'].extra.update(
            {'empty_label': 'Усі візуальні стилі'})
        self.filters['theme'].extra.update(
            {'empty_label': 'Усі тематики'})
        self.filters['feature'].extra.update(
            {'empty_label': 'Усі особливості'})
        self.filters['playersType'].extra.update(
            {'empty_label': 'Усі типи гравців'})

