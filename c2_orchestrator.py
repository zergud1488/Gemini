import requests
import time
import sys

# --- Configuration ---
BOT_TOKEN = "6110538923:AAEikXV9EoTzOBiGkh3jwSEOrSRbfdmQ2zk"
CHAT_ID = "669861467"
MESSAGE = "C2 ONLINE"
INTERVAL_SECONDS = 60
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_beacon():
    """Sends the C2 status message to Telegram."""
    payload = {
        'chat_id': CHAT_ID,
        'text': MESSAGE
    }
    
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Send the POST request with a timeout
        response = requests.post(TELEGRAM_URL, data=payload, timeout=15)
        
        if response.status_code == 200 and response.json().get('ok'):
            print(f"[{current_time}] C2 ONLINE beacon successful.")
        else:
            # Log API level errors
            print(f"[{current_time}] Failed to send beacon. HTTP Status: {response.status_code}. Response: {response.text.strip()}")
            
    except requests.exceptions.RequestException as e:
        # Log network/connection errors
        print(f"[{current_time}] Network error during beacon transmission: {e}")
    except Exception as e:
        # Log unexpected errors
        print(f"[{current_time}] Unexpected error: {e}")

def orchestrate():
    """Main loop for the C2 status beacon."""
    print(f"[INFO] C2 Orchestrator starting. Beaconing to {CHAT_ID} every {INTERVAL_SECONDS}s...")
    while True:
        send_beacon()
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    # Basic check for required library
    try:
        import requests
    except ImportError:
        print("Error: The 'requests' library is required. Install with 'pip install requests'")
        sys.exit(1)
        
    orchestrate()