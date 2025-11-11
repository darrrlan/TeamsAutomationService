#Teams Automation Microservice
=============================

This microservice automates Microsoft Teams management by creating Teams, adding users, and logging operations in MongoDB.

Features:
---------
- Authenticate with Azure AD and obtain access tokens
- Create Microsoft Teams via Microsoft Graph API
- Add members to Teams by email
- Log all actions and errors into MongoDB for monitoring and auditing

Prerequisites:
--------------
- Microsoft Azure AD app registration with permissions:
  - Group.ReadWrite.All
  - User.Read.All
  - Team.Create
  - TeamMember.ReadWrite.All
- MongoDB instance accessible for logging
- Python 3.7+
- Required Python packages (see requirements.txt)

Setup:
------
1. Clone the repository:
   git clone https://github.com/yourusername/teams-automation-service.git
   
   cd teams-automation-service

3. Create and activate a Python virtual environment:
   python -m venv venv
   
   source venv/bin/activate   (On Windows: venv\Scripts\activate)

4. Install dependencies:
   pip install -r requirements.txt

5. Create a `.env` file with your configuration variables:
   TENANT_ID=your-tenant-id
   
   CLIENT_ID=your-client-id
   
   CLIENT_SECRET=your-client-secret
   
   MONGO_URI=your-mongodb-connection-string
   
   GRAPH_API_URL=https://graph.microsoft.com/v1.0

Usage:
------
Run the main script to create a team and add members:
   python main.py

Logging:
--------
All operations are saved to MongoDB in the collection `teams_microservice.logs` with timestamps and details.

Diagram:
--------
See the sequence diagram illustrating the microservice workflow:

<p align="center">
  <img width="705" height="530" alt="Sequence Diagram" src="https://github.com/user-attachments/assets/a74acd85-6f80-4191-9343-173ff8909a4a" />
</p>

This diagram shows:
- Request token from Azure AD
- Create team via Microsoft Graph API
- Add users to the team
- Log actions and errors to MongoDB

Troubleshooting:
----------------
- Verify Azure AD app permissions and admin consent
- Confirm MongoDB connection string and accessibility
- Make sure the users exist in Azure AD before adding to teams

License:
--------
MIT License

