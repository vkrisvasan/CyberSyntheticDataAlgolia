from algoliasearch.search.client import SearchClientSync
import os

ALGOLIA_INDEX_NAME = "cybersecurity_data"

print("Initializing Algolia client...")
# Initialize the Algolia client with your application ID and API key
client = SearchClientSync(os.getenv("ALGOLIA_APP_ID"), os.getenv("ALGOLIA_API_KEY"))

# Initialize the index for cybersecurity data
print("Initializing Algolia index...")
print(ALGOLIA_INDEX_NAME)

def push_to_algolia(data):
    client.save_objects(
        index_name=ALGOLIA_INDEX_NAME, 
        body=data)
