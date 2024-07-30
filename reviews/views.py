from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
def review(request):
    # if request.method =='POST': # .method gives access to what the method for sending the data. whether its a get, post, or something else. 
    #     entered_username = request.POST['username'] # gives us access to the actual data sent in the form of a dictionary. itll hold keys with the names of the inputs in the forms, and the values are whatever the user enters. 

    #     if entered_username =="":
    #         return render(request,"reviews/review.html", {"has_error": True})
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
        

    # return render(request, "reviews/review.html")

    form = ReviewForm()

    return render(request, "reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"reviews/thank_you.html")