from teamsService import createTeam, addMemberTeam

if __name__ == "__main__":
    print("🚀 Starting the microservice...")

    new_team = createTeam("Support Squad", "Internal technical support team")

    if new_team:
        team_id = new_team.get("id")
        if team_id:
            addMemberTeam(team_id, "analyst@company.com", role="owner")
            addMemberTeam(team_id, "collaborator@company.com", role="member")
        else:
            print("❌ Team ID not found in response.")
    else:
        print("❌ Failed to create the team.")
