<h1 align="center">ForexFix</h1>

<p align="center">
  <a href="https://waveassist.io/templates/ForexFix">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <a href="https://waveassist.io/templates/forexfix-template">
  <img src="https://img.shields.io/badge/ForexFix-Daily%20Forex%20Rate%20Updates-blue" alt="ForexFix Badge" />
    </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

Looks up today’s currency exchange rate (e.g. USD to INR) from a free API and emails an HTML table of rates. Uses exchangerate.host (free, no key). Keeps you updated on forex movements for budgeting or travel.  
This automation runs on [WaveAssist](https://waveassist.io) and keeps you informed about the latest forex rates for your financial needs.

---

## One-Click Deploy on WaveAssist (Recommended)

<p>
  <a href="https://waveassist.io/templates/forexfix-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy ForexFix instantly on [WaveAssist](https://waveassist.io) — WaveAssist handles scheduling, variable storage, and orchestration for you.

> 🔐 You may be prompted to log in or create a free WaveAssist account before continuing.

#### How to Use:

1. Click the button above or go to [waveassist.io/templates/forexfix-template](https://waveassist.io/templates/forexfix-template)
2. Paste your values under the **Variables tab**:
   * `base_currency` (e.g. `USD`)
   * `target_currencies` (comma-separated list, e.g. `EUR,GBP`)
3. Run the starting node:
   - **exchange_rate_fetcher**: Fetches the latest exchange rates from the API.
4. Finally, click **Deploy** to schedule this automation and run it daily.

✅ You’re now running ForexFix on autopilot.

---

## Manual Deployment

Clone this repository and run the following scripts in order:

* `exchange_rate_fetcher.py`
* `currency_exchange_rates_email.py`

<details>
<summary>Python Requirements</summary>
  
_No additional Python requirements specified._
</details>

---

## Features

* **exchange_rate_fetcher** Fetches current exchange rates from the exchangerate.host API.
* **currency_exchange_rates_email** Formats the fetched exchange rates into an HTML table and sends them via email.
* **Processing Variables:**  Manage core data using variables like:`base_currency`, `target_currencies`, `formatted_rates_html`, `exchange_rates`, `rates_date`

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).