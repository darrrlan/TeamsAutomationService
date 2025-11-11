import requests
from auth import get_access_token
from config import GRAPH_API_URL
from logService import log_event

def createTeam(display_name, description):
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    team_data = {
        "template@odata.bind": "https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
        "displayName": display_name,
        "description": description
    }

    response = requests.post(f"{GRAPH_API_URL}/teams", headers=headers, json=team_data)

    if response.status_code in [200, 201, 202]:
        log_event("create_team", "success", {"team_name": display_name})
        return response.json()
    else:
        log_event("create_team", "error", {"status_code": response.status_code, "response": response.text})
        print(f"❌ Failed to create team: {response.status_code}\n{response.text}")
        return None

def addMemberTeam(team_id, user_email, role="member"):
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # 1️⃣ Find the user by email
    user_response = requests.get(
        f"{GRAPH_API_URL}/users/{user_email}",
        headers=headers
    )

    if user_response.status_code != 200:
        log_event("add_member", "error", {"user_email": user_email, "error": f"User not found: {user_response.text}"})
        print(f"❌ Could not find user: {user_email}")
        return None

    user_id = user_response.json().get("id")

    # 2️⃣ Add user to the team
    member_data = {
        "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{user_id}"
    }

    add_response = requests.post(
        f"{GRAPH_API_URL}/groups/{team_id}/members/$ref",
        headers=headers,
        json=member_data
    )

    if add_response.status_code in [200, 204]:
        log_event("add_member", "success", {"team_id": team_id, "user_email": user_email, "role": role})
        print(f"✅ User {user_email} added to team successfully!")
    else:
        log_event("add_member", "error", {"team_id": team_id, "user_email": user_email, "response": add_response.text})
        print(f"❌ Failed to add {user_email}: {add_response.text}")
