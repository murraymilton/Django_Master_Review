from django.urls import path
from .views import  monthly_challenge, monthly_challenge_by_number,months_index


urlpatterns = [
    path("",months_index , name="index"),
    path("<int:month>", monthly_challenge_by_number),
    path("<str:month>", monthly_challenge, name="month-challenge"),
    # Using this slug "<str:month>" we tell django to expect only a str for path
]