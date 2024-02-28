from django.conf.urls.static import static
from django.urls import path
from bookstore import settings
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('book/<int:pk>/update/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
