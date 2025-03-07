from django.urls import path
from .views import add_item, delete_item, get_item, get_items,update_item

app_name = "items"

urlpatterns = [
    path('', get_items, name='get_items'),
    path('<int:item_id>', get_item, name='get_item'),
    path('add/', add_item, name='add_item'),
    path('update/<int:item_id>', update_item, name='update_item'),
    path('update/<int:item_id>', update_item, name='update_item'),
    path('delete/<int:item_id>', delete_item, name='delete_item'),
]