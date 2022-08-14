from django.urls import path, include
from .views import goods, newGoodesView, newGoodesInfo, GoodesCats, RecreateNewGoodes, DeleteNewGoodes, OrderOfGoods

urlpatterns = [
    path('', goods, name="orders"),
    path('newGoodes/', newGoodesView, name="goodesNew"),
    path('<str:cat>/', GoodesCats, name="goodesCat"),
    path('goods/<str:cat>/<str:artic>', newGoodesInfo, name="goodesinfo"),
    path('repull/<int:id>/', RecreateNewGoodes, name="goodesRepul"),
    path('goodesdelete/<int:id>/', DeleteNewGoodes, name="goodesdelete"),
    path('create/Orders/', OrderOfGoods, name="OrderOfGoods")
]
