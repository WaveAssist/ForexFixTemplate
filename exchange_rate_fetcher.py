import waveassist
import requests

waveassist.init()

# Get base currency (default to USD if not specified)
try:
    base_currency = waveassist.fetch_data('base_currency')
except:
    base_currency = 'USD'

target_currencies = waveassist.fetch_data('target_currencies')
target_currencies = [c.strip() for c in target_currencies.split(',') if c.strip()]

# Get exchange rates from Frankfurter (base currency to all others)
api_url = f"https://api.frankfurter.app/latest?from={base_currency}&to={','.join(target_currencies)}"
response = requests.get(api_url)
response.raise_for_status()

data = response.json()
# Frankfurter doesn't return a 'success' flag, but if status is 200, it's good
if 'rates' not in data:
    raise Exception("API response missing 'rates' key")

exchange_rates = data['rates']
fetch_date = data['date']

# Store the exchange rates data
waveassist.store_data('exchange_rates', exchange_rates)
waveassist.store_data('rates_date', fetch_date)
