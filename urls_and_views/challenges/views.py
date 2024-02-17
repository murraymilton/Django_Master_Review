from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



monthly_challenges = {
    "january": "Read everyday for at least 45 mins",
    "february": "Code for at least 1 hour daily",
    "march": "Exercise for 30 minutes every day",
    "april": "Learn a new programming language",
    "may": "Contribute to an open source project",
    "june": "Build a personal project",
    "july": "Improve typing speed and accuracy",
    "august": "Create a professional portfolio website",
    "september": "Attend a technology conference or webinar",
    "october": "Participate in Hacktoberfest",
    "november": "Write technical blog posts",
    "december": "Review the year's accomplishments and set next year's goals"
}

def months_index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path =  reverse("month-challenge", args=[month])
        list_items += f"<h1><li><a href=\"{month_path}\">{capitalized_month}</a></li></h1>"

        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(list_items)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>404:The month entered could not be found!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>The month cannot be found, which you've entered</h1>")

