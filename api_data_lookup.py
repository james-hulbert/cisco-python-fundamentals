import json
import urllib.request
import urllib.error

def fetch_ip_geolocation(ip_address=""):
    """
    Fetches geolocation and network details for a given IP address
    using a free REST API. If ip_address is empty, checks current IP.
    Demonstrates: Functions, Error Handling, Dictionaries, and API Parsing.
    """
    url = f"http://ip-api.com/json/{ip_address}"
    
    # Setting up the HTTP request header (Module 4 Dictionary structure)
    headers = {'User-Agent': 'Python-API-Lookup/1.0'}
    req = urllib.request.Request(url, headers=headers)
    
    try:
        # Connect to the API endpoint
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                # Read raw bytes and decode to JSON string
                raw_data = response.read().decode('utf-8')
                data = json.loads(raw_data)
                return data
            else:
                return {"status": "fail", "message": f"HTTP Error {response.status}"}
                
    except urllib.error.URLError as e:
        return {"status": "fail", "message": f"Network Connection Error: {e.reason}"}
    except json.JSONDecodeError:
        return {"status": "fail", "message": "Failed to parse JSON response"}

def format_api_report(data):
    """
    Parses the API response dictionary and prints a formatted summary.
    Demonstrates: Dictionary lookups, Conditional Logic, and String Formatting.
    """
    if data.get("status") == "fail":
        print(f"❌ Lookup Failed: {data.get('message', 'Unknown Error')}")
        return

    # Extract relevant fields using dictionary lookup (.get prevents KeyErrors)
    query_ip = data.get("query", "N/A")
    country = data.get("country", "N/A")
    region = data.get("regionName", "N/A")
    city = data.get("city", "N/A")
    isp = data.get("isp", "N/A")
    lat = data.get("lat", 0.0)
    lon = data.get("lon", 0.0)

    # Print clean formatted output report
    print("\n" + "=" * 45)
    print(f" 🌐 API DATA LOOKUP REPORT: {query_ip}")
    print("=" * 45)
    print(f" Location  : {city}, {region}, {country}")
    print(f" Provider  : {isp}")
    print(f" Coordinates: ({lat}, {lon})")
    print("=" * 45 + "\n")

# Main execution block (Module 2-3 Logic)
if __name__ == "__main__":
    print("Initializing API Lookup Tool...")
    
    # Test IPs (Google DNS and Cloudflare DNS) stored in a Module 3 List
    test_ips = ["8.8.8.8", "1.1.1.1"]
    
    # Loop through test cases
    for ip in test_ips:
        print(f"\nFetching network records for: {ip}...")
        api_response = fetch_ip_geolocation(ip)
        format_api_report(api_response)
