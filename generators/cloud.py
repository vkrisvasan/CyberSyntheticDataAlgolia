from faker import Faker
import uuid, random, datetime
fake = Faker()
def generate_cloud_event():
    return {
        "objectID": str(uuid.uuid4()),
        "source_type": "Cloud",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "source_ip": fake.ipv4_private(),
        "destination_ip": fake.ipv4_private(),
        "source_port": random.randint(1024, 65535),
        "destination_port": random.randint(1024, 65535),
        "protocol": random.choice(["TCP", "UDP", "HTTP", "HTTPS"]),
        "user": fake.user_name(),
        "message": fake.sentence(),
        "severity": random.choice(["low", "medium", "high", "critical"]),
        "event_type": random.choice(["api_call", 
                                     "data_access", 
                                     "configuration_change"]),
        "event_id": str(uuid.uuid4()),
        "event_category": random.choice(["cloud_monitoring", 
                                         "access_control", 
                                         "resource_management"]),
        "event_source": random.choice(["cloud_service_provider", 
                                       "cloud_security_service"]),
        "event_action": random.choice(["allowed", 
                                       "blocked", 
                                       "alerted"]),
        "event_description": fake.text(max_nb_chars=200),
        "user_agent": fake.user_agent(),
        "geo_location": {
            "country": fake.country(),
            "city": fake.city(),
            "latitude": fake.latitude(),
            "longitude": fake.longitude()
        },
        "alert_type": random.choice(["unauthorized_access", 
                                     "data_exfiltration", 
                                     "misconfiguration"])
    }
# This function generates a synthetic Cloud event.
# It uses the Faker library to create realistic data for various fields.
# The generated event includes details such as source and destination IPs, ports,
# protocol, user information, event type, severity, and more.
# The event is structured as a dictionary with an `objectID` for unique identification.
# The `timestamp` is set to the current UTC time.
# The function returns the generated event as a dictionary.
# This code can be used to simulate Cloud events for testing or development purposes.
# It can be integrated into a larger application to simulate cloud-related security events.
# Ensure you have the Faker library installed:
# pip install faker
# Usage:
# from cloud import generate_cloud_event
# event = generate_cloud_event()
# print(event)
