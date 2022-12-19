from django.urls import path

from .views import CharacterList, CharacterDetail

urlpatterns = [
    path('<int:pk>/', CharacterDetail.as_view()),
    path('', CharacterList.as_view())
]