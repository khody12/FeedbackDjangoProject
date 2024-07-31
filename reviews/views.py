from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from django.views import View

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

def thank_you(request):
    return render(request,"reviews/thank_you.html")



# review = Review(
            #     user_name=form.cleaned_data['user_name'], 
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']) # we are essentially transporting the data from the form into the model, THIS CODE NOT NECESSARY WITH MODEL FORM