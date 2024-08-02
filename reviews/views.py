from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView # view that can be extended that is more specific and focused to build view classes that render templates. 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review


class ReviewView(CreateView): #create view allows us to not even have to create a form within forms.py, it will be automatically inferred by our fields variable. but it cant do custom labels or error messages
    # if we want to have custom labels, we need to set form_class and we still need to have custom forms.py. But create view will allow us not to have to right save() code. 
    model = Review 
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url ="/thank-you" # out of the book, form view doesnt know what to do with submit data, we have to add in the code to write data into the database via form_valid

    # def form_valid(self, form): # THIS CODE IS NOT NECESSARY IF WE ARE DOING CREATE VIEW INSTEAD OF FORM VIEW. FORM VIEW REQUIRES CUSTOM SAVING, WHILE CREATE VIEW WILL DO IT FOR US.
    #     form.save()
    #     return super().form_valid(form)


    # def get(self,request):
    #     form = ReviewForm()

    #     return render(request, "reviews/review.html",{
    #     "form":form
    #     })

    # def post(self,request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid(): # is valid is coming from the Form class we are inheriting from and it will check that user inputed data is valid. 
    #         form.save()
    #         #print(form.cleaned_data) # cleaned_data is a field that contains all of our validated data automatically. This is a field that exists on the form class were inheriting from.
    #         return HttpResponseRedirect("/thank-you")

class thank_you(TemplateView):
    template_name = "reviews/thank_you.html" # this is an expected property name, not some variable simply defined by me. itll automatically take this template and return and render if a get request reaches this view.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" #within our for loop in the html, by default it is object_list, but we can simply change it here so that it is more readable within html.

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1) # django will automatically supply the correct set of the data once this is returned via the get_queryset function.
        return data

    #by default, django will now take all the data that is associated with review, and pass it to that html, THATS LITERALLY IT! 

    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review # this works out of the box, despite the fact we have review in our html, django automatically takes whatever object it finds via the pk that we specified in urls.py, takes whatever we named our model,
    #make it lowercase, and then looks inside of the html and it works, despite the fact we never passed in any specific context to make that work.
    #using object within the html will also work. So object.rating will work just like review.rating. 

    



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