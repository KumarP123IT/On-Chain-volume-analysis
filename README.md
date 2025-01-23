# On-Chain Volume Analysis Script
 This Python script retrieves and analyzes the on-chain volume for a list of cryptocurrency assets using the CoinGecko API. It fetches the market chart data for each asset and reports the volume for the last 24 hours, providing valuable insights for data analysis or cryptocurrency research.

## Features
 - API Integration: Uses CoinGecko's public API to fetch market chart data for various assets.
 - Error Handling: Includes robust error handling for API request issues and missing data.
 - Batch Asset Analysis: Loads asset names from a file and analyzes each asset sequentially.
 - Formatted Output: Displays the on-chain volume in a user-friendly format with thousands separators for readability.

## Setup
 - Clone the repository or download the script.
     Install the required dependencies:
     ```bash
       pip install requests
     ```
 - Prepare a file (e.g., assets.txt) containing a list of asset names (one per line).
 - Run the script:
     ```bash
       python on_chain_volume_analysis.py
     ```

## Usage
  The script loads asset names from a file and fetches their on-chain volume for the past 24 hours. It will print the volume for each asset, and if no data is found or if an error occurs, it will notify the user.

## Example Output:
  ```graphql
    Starting analysis of assets...

    Fetching on-chain volume for: bitcoin
    On-chain volume for bitcoin: 1,234,567,890

    Fetching on-chain volume for: ethereum
    On-chain volume for ethereum: 987,654,321
    ...
  ```

## Contributing
  Feel free to fork this repository, submit issues, or contribute pull requests. Let's collaborate and improve this tool for better crypto analysis!
  
