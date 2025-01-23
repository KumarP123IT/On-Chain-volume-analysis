import os
import requests

def fetch_on_chain_volume(asset_name):
    """Fetches the on-chain volume for a given asset using the CoinGecko API."""
    try:
        # CoinGecko API endpoint for market chart
        url = f"https://api.coingecko.com/api/v3/coins/{asset_name}/market_chart"
        params = {"vs_currency": "usd", "days": 1}  # Fetch last 1 day of data

        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        data = response.json()
        volumes = data.get("total_volumes")
        if volumes:
            # Return the last recorded volume for the asset
            return volumes[-1][1]
        else:
            print(f"Warning: Volume data not found for {asset_name}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching on-chain volume for {asset_name}: {e}")
        return None

def analyze_assets(asset_names):
    """Analyzes and reports the on-chain volume for a list of assets."""
    print("Starting analysis of assets...")
    for asset_name in asset_names:
        print(f"\nFetching on-chain volume for: {asset_name}")
        volume = fetch_on_chain_volume(asset_name)
        if volume is not None:
            print(f"On-chain volume for {asset_name}: {volume:,}")
        else:
            print(f"Failed to fetch on-chain volume for {asset_name}.")
    print("\nAnalysis complete.")

def load_asset_names(file_path):
    """Loads a list of asset names from a file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().splitlines()
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
            return []
    else:
        print(f"Error: File not found: {file_path}")
        return []

def main():
    """Main entry point for the script."""
    # File containing asset names
    file_path = "asset.txt"

    # Step 1: Load asset names
    asset_names = load_asset_names(file_path)
    if not asset_names:
        print("No assets to analyze. Exiting.")
        return

    # Step 2: Analyze each asset
    analyze_assets(asset_names)

if __name__ == "__main__":
    main()


