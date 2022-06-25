from django.test import TestCase
from .views import AnimalView
from .views import HomeView
from .models import Animal


class AnimaViewTest(TestCase):
    
    def test_get_main_page(self):
        print(self.assertIs(HomeView.get(self, None).status_code == 200, True))
        self.assertIs(HomeView.get(self, None).status_code == 200, True)
        

    def test_get_all_animals(self):
        self.assertIs(AnimalView.get(self, request=None).status_code == 200, True)

        
        
