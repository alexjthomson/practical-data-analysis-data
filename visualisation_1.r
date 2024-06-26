library(ggplot2)
library(dplyr)

# Load the data:
customers <- read.csv('~/Development/apprenticeship/data/synthetic_customers.csv')

# Create age groups:
customers <- customers %>%
  mutate(AgeGroup = cut(Age, breaks = c(0, 25, 35, 45, 55, 65, 100), right = FALSE,
                        labels = c("0-24", "25-34", "35-44", "45-54", "55-64", "65+")))

# Summarise total monthly billing by age group:
billing_by_age_group <- customers %>%
  group_by(AgeGroup) %>%
  summarise(TotalMonthlyBilling = mean(`Total.Monthly.Billing`))

# Plot histogram of total monthly billing amounts by age group:
ggplot(billing_by_age_group, aes(x = AgeGroup, y = TotalMonthlyBilling, fill = AgeGroup)) +
  geom_col() +
  labs(x = "AgeGroup",
       y = "Total Monthly Billing Amount",
       fill = "Age Group") +
  theme_minimal()

