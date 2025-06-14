from django.shortcuts import render

from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.
# def store_file(file): # this is unnecessary if we use the ProfileForm as django just does this for us. 
#     with open("temp/image.png", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
class CreateProfileView(CreateView): # django is able to make this work on the back end by itself. all we need is to give it the template name, the model that its based on, and the success url. 
    template_name = "profiles/create_profile.html" #and it is able to do all the below on its own. 
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
    

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form":form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES) # request.POST contains form data, while request.FILES contains any uploaded files.
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()

#             #store_file(request.FILES['image']) # special property populated by django which gives us access to uploaded files. Files is a dictionary, and we have names within our html that is associated with the input
#             # that name, we called it "image", is how we access that file here. 
#             return HttpResponseRedirect("/profiles")
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })

        

