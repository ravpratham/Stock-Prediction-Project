# Stock Price Prediction using LSTM Neural Networks

## 📊 Project Overview

This project implements a Long Short-Term Memory (LSTM) neural network to predict stock prices. The model is trained on historical stock data and can forecast future stock prices based on past price patterns. The project focuses on Apple Inc. (AAPL) stock but can be adapted for other stocks.

## 🎯 Features

- **LSTM-based Stock Prediction**: Uses deep learning to predict stock prices
- **Data Preprocessing**: Comprehensive data cleaning and normalization
- **Model Training**: Complete training pipeline with hyperparameter optimization
- **Real-time Data Fetching**: Integration with Yahoo Finance API for live data
- **Visualization**: Interactive plots showing actual vs predicted prices
- **Model Persistence**: Save and load trained models for future use

## 🏗️ Project Structure

```
StockProject/
├── main_AAPL.ipynb              # Main Jupyter notebook with LSTM implementation
├── loadedModelMain.py           # Script to load and use trained model
├── jsonToCsvIBM.py             # Data fetching utility for Alpha Vantage API
├── my_model.h5                 # Saved Keras model (HDF5 format)
├── my_model.keras              # Saved Keras model (Keras format)
├── input/                      # Data directory
│   ├── prices-split-adjusted.csv
│   ├── prices.csv
│   ├── fundamentals.csv
│   └── securities.csv
├── stock_data_IBM_*.csv        # Generated stock data files
├── alphavantage.txt            # API key configuration
└── issues.txt                  # Known issues and improvements
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install tensorflow pandas numpy matplotlib scikit-learn yfinance requests
```

### Running the Project

1. **Training the Model**:
   ```bash
   jupyter notebook main_AAPL.ipynb
   ```
   Run all cells in the notebook to train the LSTM model.

2. **Using the Trained Model**:
   ```bash
   python loadedModelMain.py
   ```

3. **Fetching New Data**:
   ```bash
   python jsonToCsvIBM.py
   ```

## 📈 Model Architecture

### LSTM Network Structure
- **Input Layer**: 15 time steps (look-back period)
- **LSTM Layer**: 20 units with tanh activation
- **Dense Layer**: 1 unit for price prediction
- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Adam

### Data Preprocessing
- **Normalization**: MinMaxScaler (0-1 range)
- **Train/Test Split**: 70% training, 30% testing
- **Sequence Creation**: 15-day look-back window

## 📊 Performance Metrics

The model achieves the following performance on AAPL stock data:
- **Train RMSE**: 1.37
- **Test RMSE**: 2.17

## 🔧 Key Components

### 1. Data Processing (`main_AAPL.ipynb`)
- Loads historical stock data from CSV files
- Filters data for specific stock symbol (AAPL)
- Normalizes data using MinMaxScaler
- Creates sequences for LSTM training

### 2. Model Training
```python
model = Sequential()
model.add(LSTM(20, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
```

### 3. Prediction Pipeline (`loadedModelMain.py`)
- Loads pre-trained model
- Fetches real-time data using yfinance
- Preprocesses new data
- Makes predictions and visualizes results

### 4. Data Fetching (`jsonToCsvIBM.py`)
- Fetches stock data from Alpha Vantage API
- Converts JSON response to CSV format
- Handles API rate limiting and errors

## 📁 Data Sources

### Historical Data
- **prices-split-adjusted.csv**: Historical stock prices with split adjustments
- **prices.csv**: Raw historical stock prices
- **fundamentals.csv**: Company financial fundamentals
- **securities.csv**: Stock symbol mappings

### Real-time Data
- **Yahoo Finance API**: For live stock data
- **Alpha Vantage API**: For comprehensive market data

## 🛠️ Configuration

### API Keys
Create `alphavantage.txt` with your Alpha Vantage API key:
```
YOUR_API_KEY_HERE
```

### Model Parameters
- **Look-back period**: 15 days (configurable)
- **Training epochs**: 20
- **Batch size**: 1
- **LSTM units**: 20

## 📈 Usage Examples

### Training on Different Stocks
```python
# Modify the symbol filter in main_AAPL.ipynb
data_df = data_df[data_df.symbol == 'GOOGL']  # For Google
```

### Making Predictions
```python
# Load model and make predictions
model = tf.keras.models.load_model('my_model.keras')
predictions = model.predict(X_test)
```

## 🔍 Known Issues

1. **Date Axis**: X-axis dates may not display properly in plots
2. **Future Data**: "Actual price" graph shows even for future dates
3. **Model Generalization**: Model trained on AAPL may not generalize well to other stocks

## 🚧 Future Improvements

- [ ] Implement multi-stock training
- [ ] Add technical indicators as features
- [ ] Implement ensemble methods
- [ ] Add confidence intervals for predictions
- [ ] Create web interface for predictions
- [ ] Add real-time trading signals

## 📚 Dependencies

```
tensorflow>=2.0.0
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
scikit-learn>=1.0.0
yfinance>=0.1.70
requests>=2.25.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational purposes. Please ensure compliance with data provider terms of service.

## ⚠️ Disclaimer

This project is for educational and research purposes only. Stock predictions are inherently uncertain and should not be used as the sole basis for investment decisions. Always consult with financial advisors before making investment decisions.

---

**Note**: This project demonstrates the application of LSTM neural networks in financial time series prediction. The model's performance may vary based on market conditions and the specific stock being analyzed. 
