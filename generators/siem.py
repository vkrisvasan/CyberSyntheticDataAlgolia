from faker import Faker
import uuid, random, datetime
fake = Faker()
def generate_siem_event():    
    return {
                "objectID": str(uuid.uuid4()),        
                "source_type": "SIEM",        
                "timestamp": datetime.datetime.utcnow().isoformat(),        
                "source_ip": fake.ipv4_private(),        
                "destination_ip": fake.ipv4_private(),        
                "source_port": random.randint(1024, 65535),
                "destination_port": random.randint(1024, 65535),
                "protocol": random.choice(["TCP", "UDP", "ICMP"]),
                "user": fake.user_name(),
                "message": fake.sentence(),
                "severity": random.choice(["low", "medium", "high", "critical"]),
                "event_type": random.choice(["login_attempt", 
                                             "file_access", "network_activity"]),
                "event_id": str(uuid.uuid4()),
                "event_category": random.choice(["authentication", 
                                                 "file_integrity", "network"]),
                "event_source": random.choice(["firewall",
                                             "intrusion_detection_system", 
                                             "endpoint_security"]),
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
                "alert_type": random.choice(["unauthorized_access", 
                                             "malware_detected", "port_scan"])    
                                             }