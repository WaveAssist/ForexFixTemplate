import waveassist

waveassist.init()

# Fetch exchange rate data from Node 1
exchange_rates = waveassist.fetch_data("exchange_rates")  # {"data": {...}, "data_type": "json"}

# Fetch base currency and date
base_currency = waveassist.fetch_data("base_currency")
fetch_date = waveassist.fetch_data("rates_date")

# Create HTML table
html_content = f"""
<html>
<head>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
            max-width: 600px;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .rate {{
            text-align: right;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <h2>Daily Currency Exchange Rates</h2>
    <p>Base Currency: <strong>{base_currency}</strong></p>
    <p>Date: {fetch_date}</p>

    <table>
        <thead>
            <tr>
                <th>Currency</th>
                <th>Rate (1 {base_currency} =)</th>
            </tr>
        </thead>
        <tbody>
"""

# Add rows for each currency rate
for currency, rate in exchange_rates.items():
    html_content += f"""
        <tr>
            <td>{currency}</td>
            <td class="rate">{rate:.4f}</td>
        </tr>
    """


html_content += """
        </tbody>
    </table>
</body>
</html>
"""


# Store the formatted HTML table
waveassist.store_data("formatted_rates_html", html_content)

# Send email with the exchange rates table
waveassist.send_email(
    subject=f"Daily Exchange Rates - {fetch_date}",
    html_content=html_content
)
