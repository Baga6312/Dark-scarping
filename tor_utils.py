# tor_utils.py
import requests
from stem.control import Controller
from stem import Signal

def get_tor_session():
    """Create a Tor session with circuit renewal"""
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    return session

def renew_tor_circuit(password="your_password"):
    """Renew Tor circuit to get a new exit node"""
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        print(f"Error renewing Tor circuit: {e}")
