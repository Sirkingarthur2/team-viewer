from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    description: str
    members: List[str]


teamdata: Dict[str, Team] = {
    "procurement": Team(
        name="Procurement",
        description="Procurement: We buy food to cook so that we can feed you guys at lunch time and we buy supplies like soap, trash bags, etc.",
        members=["Arthur", "Markel", "Aaron", "Jacob"]
    ),
    "management": Team(
        name="Management",
        description="""Management Team: As the Management team we are required to manage all of the chores for each day and who does them. This includes: Cleaning the kitchen, and taking out the trash. Sweeping the main lobby and also sweeping the backhallway/classrooms Wiping all the tables, including the kitchen tables.""",
        members=["Chris", "Kilan", "Aidan", "Tanner"]
    ),
    "documentation": Team(
        name="Documentation",
        description="Documentation team is responsible for taking photos of guest speaker, community events , and unit projects after taking the pictures depending on the event happening in the photos determines which social media we post on we are also responsible for getting all the photos for the year book.",
        members=["Jason", "Patrick"]
    ),
    "community": Team(
        name="Community",
        description="Community: Our job is to plan events that bring people together, build lasting relationships, and promote engagement.",
        members=["Arianna", "Peyton"]
    ),
}


def team_view(request: HttpRequest, team_name: str=None) -> HttpResponse:
    if team_name:
        team = teamdata.get(team_name)
        return render(request, "hello.html", {'team': team})

    return render(request, "hello.html", {'teams': teamdata.keys()})