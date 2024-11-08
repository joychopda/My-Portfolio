import random
from datetime import datetime
import json

# Simulated user database
users = [
    {"id": 1, "name": "Steve Jobs", "clicked": False, "reported": False},
    {"id": 2, "name": "Steve Wozniak", "clicked": False, "reported": False},
    {"id": 3, "name": "Jon Ive", "clicked": False, "reported": False},
    {"id": 4, "name": "Tim Cook", "clicked": False, "reported": False}
]

def simulate_phishing_campaign():
    """Simulate a phishing campaign by determining random user actions."""
    for user in users:
        # Randomly assign actions for 'clicking' or 'reporting'
        user["clicked"] = random.choice([True, False])
        user["reported"] = not user["clicked"] and random.choice([True, False])

def generate_report():
    """Generate a summary report of the phishing campaign with user-specific data."""
    total_users = len(users)
    click_count = sum(user["clicked"] for user in users)
    report_count = sum(user["reported"] for user in users)
    click_rate = (click_count / total_users) * 100
    report_rate = (report_count / total_users) * 100

    # Collect user IDs and names for those who clicked and those who reported
    clicked_users = [{"id": user["id"], "name": user["name"]} for user in users if user["clicked"]]
    reported_users = [{"id": user["id"], "name": user["name"]} for user in users if user["reported"]]

    report_data = {
        "total_users": total_users,
        "click_count": click_count,
        "report_count": report_count,
        "click_rate": click_rate,
        "report_rate": report_rate,
        "campaign_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "clicked_users": clicked_users,
        "reported_users": reported_users
    }

    print("\n=== Phishing Campaign Report ===")
    print(f"Date: {report_data['campaign_date']}")
    print(f"Total Users: {report_data['total_users']}")
    print(f"Click Count: {report_data['click_count']} ({click_rate:.2f}%)")
    print(f"Report Count: {report_data['report_count']} ({report_rate:.2f}%)")
    print("\nUsers who clicked the link:")
    for user in clicked_users:
        print(f"  - ID: {user['id']}, Name: {user['name']}")
    print("\nUsers who reported the phishing email:")
    for user in reported_users:
        print(f"  - ID: {user['id']}, Name: {user['name']}")

    # Save report as JSON
    with open("phishing_campaign_report.json", "w") as file:
        json.dump(report_data, file, indent=4)

    return report_data

def generate_incident_response_template(report_data):
    """Generate an incident response report based on campaign data."""
    clicked_user_details = "\n".join([f"  - ID: {user['id']}, Name: {user['name']}" for user in report_data["clicked_users"]])
    reported_user_details = "\n".join([f"  - ID: {user['id']}, Name: {user['name']}" for user in report_data["reported_users"]])

    incident_report = f"""
    === Incident Response Report ===
    Campaign Date: {report_data['campaign_date']}
    Total Users Targeted: {report_data['total_users']}
    
    - Clicked Link: {report_data['click_count']} ({report_data['click_rate']:.2f}%)
    - Reported Phishing Email: {report_data['report_count']} ({report_data['report_rate']:.2f}%)

    Users who clicked the link:
    {clicked_user_details}

    Users who reported the phishing email:
    {reported_user_details}

    Incident Analysis:
    - High click rate indicates a need for additional training.
    - Employees who reported promptly demonstrated strong awareness.
    
    Next Steps:
    - Conduct follow-up training for users who clicked.
    - Share best practices and provide resources for reporting suspicious emails.
    - Monitor these users in future campaigns to assess improvement.
    
    Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    """

    # Print to console and save to file
    print(incident_report)
    with open("incident_response_report.txt", "w") as file:
        file.write(incident_report)

# Run the simulation, generate the report, and create the incident response report
simulate_phishing_campaign()
campaign_report = generate_report()
generate_incident_response_template(campaign_report)