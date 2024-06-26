import pandas as pd
from datetime import timedelta
from statsmodels.tsa.arima.model import ARIMA

def usersPredict():
    # Load data from CSV
    data = pd.read_csv("data.csv")

    # Convert 'Date' column to datetime format
    data["Date"] = pd.to_datetime(data["Date"])

    # Set 'Date' column as index
    data.set_index("Date", inplace=True)

    # Extract 'Users' column for ARIMA forecasting
    users_data = data["Users"]

    # Fit ARIMA model
    model = ARIMA(users_data, order=(1, 1, 1))  # Example (p, d, q) = (1, 1, 1)
    model_fit = model.fit()

    # Forecast next week (7 days)
    forecast = model_fit.forecast(steps=7)
    users=forecast.tolist()

    # Generate forecast dates
    forecast_dates = pd.date_range(start=data.index[-1] + timedelta(days=1), periods=7, freq='D').tolist()

    # Print or use forecast dates and user counts separately
    dataList=[]
    for i in range(len(forecast_dates)):
        data={
            "date" : str(forecast_dates[i].date()),
            "users_count": int(users[i])
        }
        dataList.append(data)
    return dataList


    
    

