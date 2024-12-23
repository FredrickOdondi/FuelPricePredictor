import pandas as pd  
import numpy as np  
import random  
from datetime import datetime, timedelta  

# Function to generate a random date  
def random_date(start, end):  
    return start + timedelta(days=random.randint(0, (end - start).days))  

# Set the random seed for reproducibility  
np.random.seed(42)  

# Generate sample data  
data = []  
regions = ['Nairobi', 'Mombasa', 'Kisumu', 'Eldoret', 'Meru']  

start_date = datetime(2024, 1, 1)  
end_date = datetime(2024, 12, 31)  

for _ in range(2000):  
    date = random_date(start_date, end_date)  
    region = random.choice(regions)  
    
    # Prices will randomly fluctuate around a mean  
    diesel_price = round(1.0 + np.random.normal(0.1, 0.05), 2)  # mean 1.0  
    petrol_price = round(1.20 + np.random.normal(0.1, 0.05), 2)  # mean 1.20  
    paraffin_price = round(0.90 + np.random.normal(0.05, 0.02), 2)  # mean 0.90  
    
    demand_index = random.randint(100, 150)  
    supply_index = random.randint(90, 130)  

    data.append([date.strftime('%Y-%m-%d'), region, diesel_price, petrol_price, paraffin_price, demand_index, supply_index])  

# Create a DataFrame  
df = pd.DataFrame(data, columns=['Date', 'Region', 'Diesel_Price', 'Petrol_Price', 'Paraffin_Price', 'Demand_Index', 'Supply_Index'])  

# Save to CSV  
df.to_csv('fuel_price_data.csv', index=False)  
print("Dataset saved as fuel_price_data.csv")