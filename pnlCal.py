import requests

# Set API credentials and parameters
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
api_passphrase = 'YOUR_API_PASSPHRASE'
product_id = 'ETH-USD'
start_date = '2022-01-01T00:00:00Z'
end_date = '2022-12-31T23:59:59Z'

# Define function to calculate realized P&L
def calculate_realized_pnl(trades):
    total_cost = 0
    total_proceeds = 0
    for trade in trades:
        if trade['side'] == 'buy':
            total_cost += float(trade['executed_value'])
        elif trade['side'] == 'sell':
            total_proceeds += float(trade['executed_value'])
    realized_pnl = total_proceeds - total_cost
    return realized_pnl

# Send authenticated API request to get all ETH trades in 2022
response = requests.get(f'https://api.pro.coinbase.com/products/{product_id}/trades',
                        auth=(api_key, api_secret, api_passphrase),
                        params={'start_date': start_date, 'end_date': end_date})

# Parse trades from API response
trades = response.json()

# Calculate and print realized P&L
realized_pnl = calculate_realized_pnl(trades)
print(f'Realized P&L for {product_id} in 2022: {realized_pnl}')
