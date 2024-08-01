from django.urls import path
from . import views

urlpatterns =[
    path("", views.ReviewView.as_view()), #as_view() makes the class act as a view.
    path("thank-you",views.thank_you.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:id>", views.SingleReviewView.as_view())
]