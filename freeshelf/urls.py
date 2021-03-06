"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from books import views as books_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books_views.book_index, name='book_list'),
    path(
        'books/<int:book_id>/favorite/',
        books_views.toggle_favorite,
        name='toggle_favorite'),
    path(
        'books/propose/',
        books_views.propose_new_book,
        name='propose_new_book'),
    path(
        'category/<slug:category_slug>/',
        books_views.category_index,
        name="category_index"),
    path('favorites/', books_views.favorites_index, name='favorites_index'),
    path('register/', users_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', books_views.AboutView.as_view(), name='about'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
