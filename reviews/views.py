from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView # view that can be extended that is more specific and focused to build view classes that render templates. 
from .models import Review

class ReviewView(View): #
    def get(self,request):
        form = ReviewForm()

        return render(request, "reviews/review.html",{
        "form":form
        })

    def post(self,request):
        form = ReviewForm(request.POST)

        if form.is_valid(): # is valid is coming from the Form class we are inheriting from and it will check that user inputed data is valid. 
            form.save()
            #print(form.cleaned_data) # cleaned_data is a field that contains all of our validated data automatically. This is a field that exists on the form class were inheriting from.
            return HttpResponseRedirect("/thank-you")

class thank_you(TemplateView):
    template_name = "reviews/thank_you.html" # this is an expected property name, not some variable simply defined by me. itll automatically take this template and return and render if a get request reaches this view.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context

class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context
class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"] # this id is coming from urls.py where we have  <> indicating a dynamic url. This id is in kwargs because we have it there as a parameter in our urls.py
        SelectedReview = Review.objects.get(pk=review_id) # pk is primary key, and its the unique identifier for each record that is in our SQL database. it is automatically assigned and we are retrieving it here by taking 
        # in the variable number in our url, that is put into kwargs, review_id accesses kwargs id value, and then finally we use that to get the specific review object from our database and then pass to that our template. 
        context['review'] = SelectedReview

        return context



# def review(request):

#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         #if we wanted to update an existing data set in our data base.
#         #existing_data = Review.objects.get(pk=1) # pk is an identifier
#         #form = ReviewForm(request.POST,instance=existing_data)
#         form = ReviewForm(request.POST)

#         if form.is_valid(): # is valid is coming from the Form class we are inheriting from and it will check that user inputed data is valid. 
#             form.save()
#             #print(form.cleaned_data) # cleaned_data is a field that contains all of our validated data automatically. This is a field that exists on the form class were inheriting from.
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

   

#     return render(request, "reviews/review.html",{
#         "form":form
#     })






# review = Review(
            #     user_name=form.cleaned_data['user_name'], 
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']) # we are essentially transporting the data from the form into the model, THIS CODE NOT NECESSARY WITH MODEL FORM