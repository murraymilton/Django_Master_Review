from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None
}

def months_index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

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
        # If you use render --> your must pass in the request argument.
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404("404.html")
        

