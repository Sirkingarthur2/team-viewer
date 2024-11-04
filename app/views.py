# views.py
from django.shortcuts import render
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Team:
    name: str
    description: str
    members: List[str]

# Sample team data
teamdata: Dict[str, Team] = {
    "procurement": Team(
        name="Procurement",
        description="The Procurement team at Basecamp serves as the backbone of Basecamp's kitchen operations. They handle the acquisition of essential supplies, from toiletries to food. In addition, they play a significant role in preparing meals for the Basecamp students.",
        members=["Arthur", "Markel", "Aaron", "Jacob"]
    ),
    "management": Team(
        name="Management",
        description="The Management team is responsible for maintaining the order and cleanliness of the building. They allocate chores to the other students and ensure that these tasks are completed efficiently.",
        members=["Chris", "Kilan", "Aidan", "Tanner"]
    ),
    "documentation": Team(
        name="Documentation",
        description="In Base Camp Coding Academy, the Documentation Team's role is preserving the moments of Basecamp's daily activities and special events with pictures. This team's main objective is to portray the organic moments of Basecamp and post them on social media.",
        members=["Jason", "Patrick"]
    ),
    "community": Team(
        name="Community",
        description="The Community team organizes engaging events for Basecamp students every other week to strengthen their  sense of community. They also oversee a program at Basecamp aimed at teaching young kids the basics of coding.",
        members=["Arianna", "Peyton"]
    ),
}

def team_view(request, team_name=None):
    if team_name and team_name in teamdata:
        team = teamdata[team_name]
        return render(request, "home.html", {'team': team})
    
    return render(request, "home.html", {'teams': teamdata.keys()})
