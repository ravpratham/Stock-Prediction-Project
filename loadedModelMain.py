import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

# Load the pre-trained TensorFlow model
model = tf.keras.models.load_model("my_model.keras")
print(model.input_shape)

# tickerSymbol = 'ADBE'
# data =  pd.read_csv("./input/prices-split-adjusted.csv", index_col = 0)
# data = data[data.symbol == tickerSymbol]
# data.head()

ticker = "ADBE"
data = yf.download(ticker, start="2025-08-20", end="2025-09-20")
data.head()


# Preprocess data
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data["Close"].values.reshape(-1, 1))

# Prepare input for prediction
look_back = 15
# Number of previous days to consider
X_test = []
for i in range(look_back, len(data_scaled)):
    X_test.append(data_scaled[i-look_back:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

# Predict stock prices
predicted_stock_price = model.predict(X_test)
predicted_stock_price = scaler.inverse_transform(predicted_stock_price)

# Plot results
plt.figure(figsize=(12,6))
plt.plot(data.index[look_back:], data["Close"].values[look_back:], label="Actual Price")
plt.plot(data.index[look_back:], predicted_stock_price, label="Predicted Price")
plt.legend()
plt.title(ticker + " Stock Price Prediction")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.show()