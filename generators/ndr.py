from faker import Faker
import uuid, random, datetime
fake = Faker()
def generate_ndr_event():
    return {
        "objectID": str(uuid.uuid4()),
        "source_type": "NDR",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "source_ip": fake.ipv4_private(),
        "destination_ip": fake.ipv4_private(),
        "source_port": random.randint(1024, 65535),
        "destination_port": random.randint(1024, 65535),
        "protocol": random.choice(["TCP", "UDP", "ICMP"]),
        "user": fake.user_name(),
        "message": fake.sentence(),
        "severity": random.choice(["low", "medium", "high", "critical"]),
        "event_type": random.choice(["network_activity", 
                                     "protocol_violation", 
                                     "anomalous_traffic"]),
        "event_id": str(uuid.uuid4()),
        "event_category": random.choice(["network_monitoring", 
                                         "traffic_analysis"]),
        "event_source": random.choice(["network_device", 
                                       "intrusion_detection_system"]),
        "event_action": random.choice(["allowed", 
                                       "blocked", "alerted"]),
        "event_description": fake.text(max_nb_chars=200),
        "user_agent": fake.user_agent(),
        "geo_location": {
            "country": fake.country(),
            "city": fake.city(),
            "latitude": fake.latitude(),
            "longitude": fake.longitude()
        },
        "alert_type": random.choice(["suspicious_activity", 
                                     "data_exfiltration", 
                                     "malware_detected"])
    }
# This function generates a synthetic NDR (Network Detection and Response) event.
# It uses the Faker library to create realistic data for various fields.
# The generated event includes details such as source and destination IPs, ports,
# protocol, user information, event type, severity, and more.
# The event is structured as a dictionary with an `objectID` for unique identification.
# The `timestamp` is set to the current UTC time.
# The function returns the generated event as a dictionary.
# This code can be used to simulate NDR events for testing or development purposes.
# Ensure you have the Faker library installed:
# pip install faker
# Usage:
# from ndr import generate_ndr_event
# event = generate_ndr_event()
# print(event)