# StockProject — Predicting Stock Prices (Plain-English Guide)

This project teaches a computer to look at past stock prices and guess the next ones. It uses a simple LSTM (a type of neural network) and two ways to work:
- Train a model in a Jupyter Notebook
- Load that saved model to make new predictions from recent market data

---

## What’s inside (the important bits)

- `main_AAPL.ipynb`: The training notebook. It reads historical prices, prepares the data, trains a small LSTM model, checks how well it did, shows charts, and saves the model to a file.
- `loadedModelMain.py`: A small script that loads the saved model and predicts on fresh data pulled from Yahoo Finance (no retraining).
- `input/`: Historical datasets (CSV files) used for training and experiments.
- `my_model.keras` / `my_model.h5`: Saved model files (created by the notebook).
- `jsonToCsvIBM.py`: Optional tool to fetch daily data from Alpha Vantage and save as CSV.
- `alphavantage.txt`: Your Alpha Vantage API key (if you use `jsonToCsvIBM.py`).
- `issues.txt`: Known rough edges to improve later.

---

## How it works (in 3 steps)

1) Data → The notebook loads historical closing prices (e.g., Apple/AAPL) from the `input/` CSV files.
2) Learn → It scales the numbers, slices them into 15‑day windows, and trains a tiny LSTM to predict the next day’s close.
3) Use → It saves the trained brain (`my_model.keras`). The Python script then loads that file, grabs recent prices from Yahoo Finance (ticker is editable), and plots predicted vs actual.

---

## Quick start

1) Install Python deps (use your venv if you have one):

```bash
pip install tensorflow pandas numpy matplotlib scikit-learn yfinance requests
```

2) Train the model (in the notebook):

```bash
jupyter notebook main_AAPL.ipynb
```
- Run the cells top to bottom. At the end you should see a “Model Saved!” message and a file named `my_model.keras` in the folder.

3) Make predictions with the saved model:

```bash
python loadedModelMain.py
```
- By default it fetches recent data for `ADBE`. Change `ticker` and the date range in the script as you like.

Optional — fetch data to CSV via Alpha Vantage:

```bash
# Put your API key into alphavantage.txt (or directly in the script)
python jsonToCsvIBM.py
```
This saves a file like `stock_data_IBM_YYYYMMDD_HHMMSS.csv` in the project root.

---

## What you’ll see

- In the notebook: training and test error (RMSE) and charts comparing actual vs predicted prices.
- In the script: a plot of recent actual vs predicted prices—good for a quick sanity check.

---

## Change the stock

- In the notebook (training): filter another symbol in the code cell that selects `AAPL`.
- In `loadedModelMain.py` (inference): edit `ticker = "ADBE"` and the date range.

Note: The model was trained on AAPL in the sample notebook. Predicting other tickers without retraining may work but can be less accurate.

---

## Assumptions & limits (read this!)

- This is an educational demo, not trading advice.
- The model is tiny and uses only past closing prices (no volumes, no indicators). It’s meant to be simple and explainable.
- Scaling matters: the script fits its own MinMaxScaler on the fetched window so its scale may differ from training. For production, save and reuse the training scaler.
- Dates on plots can look odd (see `issues.txt`). Future points shouldn’t be treated as “known” actuals.

---

## File map (short)

- `main_AAPL.ipynb` — train, evaluate, save.
- `loadedModelMain.py` — load, fetch, predict, plot.
- `input/` — CSVs: prices, fundamentals, tickers.
- `my_model.keras` — saved model (created by the notebook).
- `jsonToCsvIBM.py` — optional: Alpha Vantage → CSV helper.

---

## Common questions

- “Why LSTM?” It’s a common neural net for time series (remembers recent steps).
- “Can I improve it?” Yes—add features (volume, indicators), tune look‑back, increase LSTM units/epochs, or try other models.
- “Do I need an API key?” Only for `jsonToCsvIBM.py` (Alpha Vantage). Yahoo Finance via `yfinance` doesn’t require keys.

---

## License & disclaimer

This is for learning/research only. Markets are risky—don’t use this as financial advice.

---

Happy experimenting!
