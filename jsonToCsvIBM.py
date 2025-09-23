import requests
import pandas as pd
from datetime import datetime


def fetch_stock_data(symbol, api_key):
    """
    Fetch stock data from Alpha Vantage API
    """
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'full'  # Get full data instead of compact
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def json_to_csv(data, output_filename):
    """
    Convert JSON data to CSV format
    """
    try:
        # Extract time series data
        time_series = data.get('Time Series (Daily)', {})

        # Convert to DataFrame
        df = pd.DataFrame.from_dict(time_series, orient='index')

        # Rename columns
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

        # Clean up column names (remove numbers)
        df.columns = [col.split('. ')[1] if '. ' in col else col for col in df.columns]

        # Convert index to datetime
        df.index = pd.to_datetime(df.index)

        # Sort by date
        df.sort_index(inplace=True)

        # Save to CSV
        df.to_csv(output_filename)
        print(f"Data successfully saved to {output_filename}")

        return df
    except Exception as e:
        print(f"Error converting data: {e}")
        return None


def main():
    API_KEY = 'KM0NEKE49Y5BJI52'
    # You can change the stock symbol as needed
    SYMBOL = 'IBM'  # Example stock symbol

    # Create output filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f'stock_data_{SYMBOL}_{timestamp}.csv'

    print(f"Fetching data for {SYMBOL}...")
    data = fetch_stock_data(SYMBOL, API_KEY)

    if data:
        print("Converting data to CSV...")
        df = json_to_csv(data, output_filename)
        if df is not None:
            print(f"First few rows of the data:")
            print(df[-5:])
            print(f"\nShape of the dataset: {df.shape}")


if __name__ == "__main__":
    main()
