import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the random seed for reproducibility:
np.random.seed(42)

# Parameters:
num_customers = 500
num_calls = 10000

# Generate customer data:
customer_ids = np.arange(1, num_customers + 1)
ages = np.random.normal(35, 10, num_customers).astype(int)
genders = np.random.choice(['Male', 'Female', 'Other'], num_customers, p=[0.495, 0.495, 0.01])
subscription_plans = np.random.choice(['Standard', 'Premium'], num_customers, p=[0.7, 0.3])

# Create a customer data-frame:
customers = pd.DataFrame({
    'Customer ID': customer_ids,
    'Age': ages,
    'Gender': genders,
    'Subscription Plan': subscription_plans
})

# Generate call data:
call_durations = np.random.exponential(3, num_calls).astype(int) + 1
call_types = np.random.choice(['Domestic', 'International'], num_calls, p=[0.8, 0.2])
timestamps = [datetime.now() - timedelta(days=np.random.randint(0, 30), hours=np.random.randint(0, 24), minutes=np.random.randint(0, 60)) for _ in range(num_calls)]
customer_ids_calls = np.random.choice(customer_ids, num_calls)

# Define rate based on call type and subscription plan:
def get_rate(call_type, subscription_plan):
    if call_type == 'Domestic':
        return 0.06 if subscription_plan == 'Premium' else 0.05
    else:
        return 0.18 if subscription_plan == 'Premium' else 0.15

# Calculate charges:
charges = []
for i in range(num_calls):
    rate = get_rate(call_types[i], customers.loc[customers['Customer ID'] == customer_ids_calls[i], 'Subscription Plan'].values[0])
    charges.append(call_durations[i] * rate)

# Create a calls data-frame:
calls = pd.DataFrame({
    'Customer ID': customer_ids_calls,
    'Call Duration': call_durations,
    'Call Type': call_types,
    'Timestamp': timestamps,
    'Rate Applied': [get_rate(call_types[i], customers.loc[customers['Customer ID'] == customer_ids_calls[i], 'Subscription Plan'].values[0]) for i in range(num_calls)],
    'Charges': charges
})

# Aggregate total monthly billing:
total_monthly_billing = calls.groupby('Customer ID')['Charges'].sum().reset_index()
total_monthly_billing.columns = ['Customer ID', 'Total Monthly Billing']

# Merge customer data with total monthly billing:
customers = customers.merge(total_monthly_billing, on='Customer ID', how='left')

# Print sample data to be included in the assignment:
print(customers.head())
print(calls.head())

# Save to CSV:
customers.to_csv('synthetic_customers.csv', index=False)
calls.to_csv('synthetic_calls.csv', index=False)