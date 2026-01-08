from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Eat No meat in the entire month",
    "february": "Exercise at least 20 minutes every day",
    "march": "Read 10 pages of a book daily",
    "april": "Practice meditation for 10 minutes daily",
    "may": "Write down 3 things you’re grateful for each day",
    "june": "Drink at least 2 liters of water daily",
    "july": "Limit social media use to 30 minutes per day",
    "august": "Learn or practice a new skill for 30 minutes daily",
    "september": "Go for a walk outdoors every day",
    "october": "Declutter one item from your home daily",
    "november": "Cook at least one healthy homemade meal per day",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenges_text, "month_name": month},
        )
        # response = render_to_string("challenges/challenge.html")
        # return HttpResponse(response)
    except KeyError:
        return HttpResponseNotFound("Its not month!!")
