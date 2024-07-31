from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100,error_messages={
#         "required":"Your name must not be empty!",
#         "max_length":"Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your feedback",widget=forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label="Your rating",min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review # review form is now connected with review model. 
        # we need to specify which fields should be included, because sometimes we might have some fields that shouldnt be public to the user
        fields = "__all__" # this is just saying all fields should be included, if we need to do specific ones, use a list [1,2,3,4]
        # we can also exclude fields if we want to have all except a few. exclude = ['somefield']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name":{
                "required":"Your name must not be empty!",
                "max_length":"Please enter a shorter name!"
            }
        }
    
