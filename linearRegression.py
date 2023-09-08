import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

def predict_cpu_usage(log_file_date):
    log_filename = f"{log_file_date}-pub.log"
    
    df = pd.read_csv(log_filename, names=["Timestamp", "CPU Usage", "Logical CPUs", "Memory Usage", "Disk Usage", "Host IP"])
    
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Days"] = (df["Timestamp"] - df["Timestamp"].min()).dt.days
    X = df["Days"].values.reshape(-1, 1)
    y = df["CPU Usage"].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_date = df["Timestamp"].max() + datetime.timedelta(days=1)
    future_day = (future_date - df["Timestamp"].min()).days
    predicted_cpu_usage = model.predict([[future_day]])[0]
    
    print(f"Predicted CPU Usage for {future_date}: {predicted_cpu_usage}%")

if __name__ == "__main__":
    log_file_date = "2023-09-07"  # Change this to the date you want to predict
    predict_cpu_usage(log_file_date)
