library(ggplot2)
library(dplyr)
library(tidyr)

# Load the data:
calls <- read.csv('~/Development/apprenticeship/data/synthetic_calls.csv')

# Create a summary data-frame for customer monthly billing by call type:
billing_by_call_type <- calls %>%
  group_by(Customer.ID, Call.Type) %>%
  summarise(TotalBilling = sum(Charges)) %>%
  ungroup()

# Plot a box-plot of monthly billing amounts by call type:
ggplot(billing_by_call_type, aes(x = Call.Type, y = TotalBilling, fill = Call.Type)) +
  geom_boxplot() +
  labs(x = "Call Type",
       y = "Total Monthly Billing Amount",
       fill = "Call Type") +
  theme_minimal()

