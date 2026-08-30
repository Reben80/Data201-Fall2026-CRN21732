# Class 2 (Student Version): pandas Data Wrangling for R Users
# Course: Intro to Data Analysis in Python
# Background assumed: R, dplyr pipelines, basic data.frames

# =====================================================
# HOW TO USE THIS NOTEBOOK
# =====================================================
# - Run cells top to bottom
# - Complete all TODO sections
# - When R code is shown, translate it to pandas
# - Focus on clarity and correctness, not cleverness

# =====================================================
# 0. Setup
# =====================================================

import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 20)

# =====================================================
# 1. From data.frame to DataFrame
# =====================================================

# In R:
# df <- read.csv("data.csv")

# For today, we create a small example dataset

data = {
    "price": [200, 180, 250, 300, np.nan, 220, 260],
    "size": [1400, 1200, 1600, 1800, 1500, 1550, 1700],
    "bedrooms": [3, 2, 3, 4, 3, 3, 4],
    "neighborhood": ["A", "A", "B", "B", "A", "B", "B"],
}

df = pd.DataFrame(data)
df

# TODO:
# 1. Check the dimensions of df
# 2. Inspect the structure of df
# 3. Produce summary statistics

# =====================================================
# 2. Index vs Columns (Very Important!)
# =====================================================

# TODO:
# 1. Inspect df.index
# 2. Inspect df.columns

# Question:
# Why is the index NOT the same as a regular column?

# =====================================================
# 3. Selecting Columns (dplyr::select)
# =====================================================

# In R:
# select(df, price, size)

# TODO:
# Select only price and size

# TODO:
# Select a single column (price) as a Series

# =====================================================
# 4. Filtering Rows (dplyr::filter)
# =====================================================

# In R:
# filter(df, price > 200)

# TODO:
# Filter rows where price > 200

# TODO:
# Filter rows where price > 200 AND bedrooms >= 3

# =====================================================
# 5. Creating New Variables (dplyr::mutate)
# =====================================================

# In R:
# mutate(df, price_per_sqft = price / size)

# TODO:
# Create a new column price_per_sqft

# =====================================================
# 6. Sorting Rows (dplyr::arrange)
# =====================================================

# In R:
# arrange(df, price)

# TODO:
# Sort df by price (ascending)

# TODO:
# Sort df by price (descending)

# =====================================================
# 7. Grouping and Aggregation
# =====================================================

# In R:
# df %>%
#   group_by(neighborhood) %>%
#   summarize(mean_price = mean(price, na.rm = TRUE))

# TODO:
# Reproduce the summary above in pandas

# =====================================================
# 8. Method Chaining (Pipe Mindset)
# =====================================================

# Pandas supports method chaining, similar to %>% in R

# TODO:
# Using chaining, compute:
# - Filter: price > 200
# - Mutate: price_per_sqft = price / size
# - Group by neighborhood
# - Summarize: average price_per_sqft

# =====================================================
# 9. Missing Data
# =====================================================

# TODO:
# 1. Identify which values are missing
# 2. Drop rows with missing values
# 3. Fill missing prices with the mean price

# Question:
# When is dropping missing data reasonable? When is it risky?

# =====================================================
# 10. Common Pitfalls for R Users
# =====================================================

# - Boolean filtering requires parentheses
# - groupby() does nothing until you aggregate
# - Chained assignment warnings

# =====================================================
# 11. Active Learning Exercise (15–20 minutes)
# =====================================================

# R pipeline:
# df %>%
#   filter(size > 1400) %>%
#   mutate(price_per_sqft = price / size) %>%
#   group_by(neighborhood) %>%
#   summarize(avg_ppsqft = mean(price_per_sqft, na.rm = TRUE))

# TASK:
# Translate the pipeline above into pandas using method chaining.
# Write clean, readable code.

# --- Your solution below ---

# =====================================================
# 12. Wrap-Up Reflection
# =====================================================

# In 2–3 sentences:
# - What feels most similar to dplyr?
# - What feels most different?
# - What do you find confusing so far?
