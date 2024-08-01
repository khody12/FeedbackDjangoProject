from django.urls import path
from . import views

urlpatterns =[
    path("", views.ReviewView.as_view()), #as_view() makes the class act as a view.
    path("thank-you",views.thank_you.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()) # we change id to pk to allow us to use detail view. It tells django we should be using a primary key value of which django should find a single piece of data
    # django will go to the database and find an entry that matches the pk that is stated. 
]