from faker import Faker
import uuid, random, datetime
fake = Faker()
def generate_cve_event():
    return {
        "objectID": str(uuid.uuid4()),
        "source_type": "CVE",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "source_ip": fake.ipv4_private(),
        "destination_ip": fake.ipv4_private(),
        "source_port": random.randint(1024, 65535),
        "destination_port": random.randint(1024, 65535),
        "protocol": random.choice(["TCP", "UDP", "ICMP"]),
        "user": fake.user_name(),
        "message": fake.sentence(),
        "severity": random.choice(["low", "medium", "high", "critical"]),
        "event_type": random.choice(["vulnerability_reported", 
                                     "exploit_attempt", 
                                     "patch_released"]),
        "event_id": str(uuid.uuid4()),
        "event_category": random.choice(["vulnerability_management", 
                                         "security_patch"]),
        "event_source": random.choice(["cve_database", 
                                       "security_research"]),
        "event_action": random.choice(["reported", 
                                       "updated", 
                                       "patched"]),
        "event_description": fake.text(max_nb_chars=200),
        "user_agent": fake.user_agent(),
        "geo_location": {
            "country": fake.country(),
            "city": fake.city(),
            "latitude": fake.latitude(),
            "longitude": fake.longitude()
        },
        "alert_type": random.choice(["new_vulnerability_detected", 
                                     "exploit_attempt_detected", 
                                     "patch_available"])
    }
# This function generates a synthetic CVE (Common Vulnerabilities and Exposures) event.
# It uses the Faker library to create realistic data for various fields.
# The generated event includes details such as source and destination IPs, ports,
# protocol, user information, event type, severity, and more.
# The event is structured as a dictionary with an `objectID` for unique identification.
# The `timestamp` is set to the current UTC time.
# The function returns the generated event as a dictionary.
# This code can be used to simulate CVE events for testing or development purposes.
# Ensure you have the Faker library installed:
# pip install faker
# Usage:
# from cve import generate_cve_event
# event = generate_cve_event()
# print(event)