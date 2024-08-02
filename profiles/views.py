from django.shortcuts import render

from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        print(request.FILES['image']) # special property populated by django which gives us access to uploaded files. Files is a dictionary, and we have names within our html that is associated with the input
        # that name, we called it "image", is how we access that file here. 
        return HttpResponseRedirect("/profiles")

        
        pass
