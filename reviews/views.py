from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
def review(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid(): # is valid is coming from the Form class we are inheriting from and it will check that user inputed data is valid. 
            print(form.cleaned_data) # cleaned_data is a field that contains all of our validated data automatically. This is a field that exists on the form class were inheriting from.
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

   

    return render(request, "reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"reviews/thank_you.html")