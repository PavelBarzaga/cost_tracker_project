from django.urls import path
from .views import CostListCreateView, CostRetrieveUpdateDestroyView

urlpatterns = [
    path("costs/", CostListCreateView.as_view(), name="cost-list-create"),
    path(
        "costs/<int:pk>/",
        CostRetrieveUpdateDestroyView.as_view(),
        name="cost-retrieve-update-destroy",
    ),
]
