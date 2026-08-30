# Class 3 (Student Version): Visualization in Python for R Users
# Course: Intro to Data Analysis in Python
# Background assumed: ggplot2 basics, aesthetics, geoms

# =====================================================
# HOW TO USE THIS NOTEBOOK
# =====================================================
# - Run cells top to bottom
# - Complete all TODO sections
# - Compare each plot to how you would do it in ggplot2
# - Focus on interpreting plots, not just producing them

# =====================================================
# 0. Setup
# =====================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# =====================================================
# 1. Data for Visualization
# =====================================================

# Simulated housing-style dataset

np.random.seed(42)

df = pd.DataFrame({
    "price": np.random.normal(250, 40, 100),
    "size": np.random.normal(1600, 200, 100),
    "bedrooms": np.random.choice([2, 3, 4], size=100),
    "neighborhood": np.random.choice(["A", "B", "C"], size=100)
})

df.head()

# =====================================================
# 2. First Plot: Scatterplot
# =====================================================

# In ggplot2:
# ggplot(df, aes(size, price)) + geom_point()

# TODO:
# Create a scatterplot of size vs price

# TODO:
# Label the x-axis and y-axis

# =====================================================
# 3. Adding Color (Aesthetics)
# =====================================================

# In ggplot2:
# ggplot(df, aes(size, price, color = neighborhood)) + geom_point()

# TODO:
# Recreate the plot above using seaborn

# Question:
# What does seaborn do automatically that matplotlib does not?

# =====================================================
# 4. Faceting vs Small Multiples
# =====================================================

# In ggplot2:
# ggplot(df, aes(size, price)) + geom_point() + facet_wrap(~ bedrooms)

# TODO:
# Create small multiples by bedrooms

# =====================================================
# 5. Distribution Plots
# =====================================================

# In ggplot2:
# ggplot(df, aes(price)) + geom_histogram()

# TODO:
# Create a histogram of price

# TODO:
# Create a density plot of price

# =====================================================
# 6. Summaries and Categorical Plots
# =====================================================

# In ggplot2:
# ggplot(df, aes(neighborhood, price)) + geom_boxplot()

# TODO:
# Create a boxplot of price by neighborhood

# =====================================================
# 7. Matplotlib vs Seaborn (Conceptual)
# =====================================================

# Question:
# Which library feels closer to ggplot2? Why?

# =====================================================
# 8. Plot Interpretation (Very Important)
# =====================================================

# TODO:
# Answer in text:
# 1. Is there a relationship between size and price?
# 2. Do neighborhoods differ systematically in price?
# 3. Which plot best answers each question?

# =====================================================
# 9. Common Pitfalls for R Users
# =====================================================

# - Figures do not auto-print; need plt.show()
# - Statefulness of matplotlib
# - Overplotting without transparency

# =====================================================
# 10. Active Learning Exercise (15–20 minutes)
# =====================================================

# TASK:
# Create a single figure that:
# - Shows size vs price
# - Colors by neighborhood
# - Uses transparency to reduce overplotting
# - Includes clear axis labels and a title

# Bonus:
# Add a regression line

# --- Your solution below ---

# =====================================================
# 11. Wrap-Up Reflection
# =====================================================

# In 2–3 sentences:
# - What is easier in ggplot2?
# - What is easier in Python?
# - What will you need to practice more?
