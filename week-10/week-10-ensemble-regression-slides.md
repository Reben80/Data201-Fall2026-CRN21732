<!-- .slide: data-background-color="#1F4E79" -->
# DATA 201 — Week 10
## Ensemble Methods for Regression
### Student-Friendly Slides (60-minute class)

Instructor: Dr. Rebin Abdulkader Muhammad  
Audience: Early college students  
Focus: Decision Trees · Random Forest · Gradient Boosting

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Today's Plan (60 minutes)

| Time | Focus |
|---|---|
| 0–5 min | Warm-up + vocabulary |
| 5–20 min | Decision tree foundations |
| 20–35 min | Random forest (bagging) |
| 35–48 min | Gradient boosting |
| 48–55 min | Model comparison + interpretation |
| 55–60 min | Exit ticket |

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Learning Goals

By the end of today, you should be able to:

- Explain what an **ensemble model** is
- Explain how a **decision tree** makes predictions
- Describe the difference between **bagging** and **boosting**
- Read model metrics: **MSE** and **R²**
- Compare Decision Tree, Random Forest, and Gradient Boosting in plain language

---
<!-- .slide: data-background-color="#FFF8E7" -->
# Warm-Up Question

If you wanted to estimate a house price, which would you trust more?

- **One person's guess**
- **A class average of 30 guesses**

Why?

> Keep this idea in mind. It connects directly to ensemble learning.

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Key Terms (Part 1)

- **Model**: a math tool that learns patterns from data
- **Feature**: an input variable (example: house size)
- **Target**: what we want to predict (example: house value)
- **Regression**: predicting a numeric value
- **Train/Test Split**: train on one part, test on unseen data

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Key Terms (Part 2)

- **Decision Tree**: model that asks a sequence of split questions
- **Bagging**: train many models in parallel, then average
- **Random Forest**: many decision trees trained with bagging
- **Boosting**: train models in sequence; new models fix earlier errors
- **Gradient Boosting**: a common and powerful boosting method

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Dataset Used in Class

We use the **California Housing** dataset.

**Example features**

- Median income
- House age
- Average rooms
- Population
- Latitude / longitude

**Target**

- Median house value (numeric)

---
<!-- .slide: data-background-color="#2E7D32" -->
# Section 1
## Decision Trees
### The building block of ensembles

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Why Start with Decision Trees?

Because trees are:

- Visual
- Intuitive
- A strong foundation for understanding ensembles

Also important:

- Random Forest and Gradient Boosting are both built from trees

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Decision Tree: Core Idea

A decision tree repeatedly asks yes/no questions such as:

- Is median income > 3.2?
- Is house age ≤ 25?
- Is average rooms > 5.5?

Each answer sends data down a branch.

At the end, a **leaf node** gives a prediction.

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Tree Vocabulary

| Term | Meaning |
|---|---|
| **Root node** | First split (top of tree) |
| **Internal node** | Middle decision points |
| **Leaf node** | Final output value |
| **Depth** | How many split levels from root to leaf |
| **Split** | Rule that partitions data into two groups |

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Simple Tree Walkthrough

Imagine one path:

1. Is median income > 3.5? → **Yes**
2. Is average rooms > 6? → **No**
3. Is house age > 30? → **Yes**

Leaf prediction: **2.1** (in dataset target units)

**Takeaway**

- Trees turn complex prediction into a sequence of smaller choices.

---
<!-- .slide: data-background-color="#E8F5E9" -->
# How Does a Tree Choose a Split?

For regression trees, the algorithm chooses splits that reduce error.

**Informal idea**

- Before split: group has mixed target values
- After split: each child group is more similar

The model looks for splits that make children "cleaner" (less variance).

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Decision Tree Strengths

- Easy to explain to non-technical audiences
- Captures nonlinear patterns
- Handles interactions automatically
- No feature scaling required

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Decision Tree Weaknesses

- Can **overfit** if too deep
- Sensitive to small data changes
- One tree can be unstable

> This is exactly why ensembles are useful.

---
<!-- .slide: data-background-color="#FFF3E0" -->
# Overfitting (Student-Friendly)

**Overfitting** means:

- Model memorizes training details/noise
- Looks great on training data
- Performs worse on new data

**Warning signs for trees**

- Very deep tree
- Very high training score, much lower test score

---
<!-- .slide: data-background-color="#E8F5E9" -->
# Controlling Tree Complexity

Common settings (**hyperparameters**):

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

**Goal**

- Learn enough patterns without memorizing noise

---
<!-- .slide: data-background-color="#FFF8E7" -->
# Quick Check (Think-Pair-Share)

**Question**

Why might a very deep tree perform worse on test data than a moderate-depth tree?

Discuss with a partner for **1 minute**.

---
<!-- .slide: data-background-color="#2E7D32" -->
# Transition
## From One Tree → Many Trees

One tree = understandable, but unstable  
Many trees = usually more stable and more accurate

---
<!-- .slide: data-background-color="#E3F2FD" -->
# Big Idea: What Is an Ensemble?

An **ensemble** combines multiple models to make one final prediction.

**Analogy**

- One student answer: maybe right
- Many student answers averaged: usually more reliable

---
<!-- .slide: data-background-color="#EF6C00" -->
# Section 2
## Random Forest
### Bagging many trees together

---
<!-- .slide: data-background-color="#FFF3E0" -->
# Ensemble Family #1: Bagging

**Bagging = Bootstrap Aggregating**

**Pipeline**

1. Sample training rows with replacement
2. Train one tree per sample
3. Average predictions

**Main effect**

- Reduces variance (less jumpy predictions)

---
<!-- .slide: data-background-color="#FFF3E0" -->
# Bootstrap Sampling (In Plain Language)

"With replacement" means:

- A row can appear multiple times in one sample
- Some rows may be left out of that sample

**Why useful?**

- Creates many slightly different training sets
- Encourages diversity among trees

---
<!-- .slide: data-background-color="#FFF3E0" -->
# Random Forest = Bagging + Extra Randomness

Random Forest adds another trick:

- At each split, it only considers a **random subset of features**

**Why this helps**

- Trees become less similar to each other
- Averaging works better when models are diverse

---
<!-- .slide: data-background-color="#FFF3E0" -->
# Random Forest Pros / Cons

**Pros**

- Strong baseline model
- Robust performance
- Less overfitting than a single tree

**Cons**

- Harder to interpret than one tree
- Can be slower than one tree

---
<!-- .slide: data-background-color="#C62828" -->
# Section 3
## Gradient Boosting
### Learning from mistakes, one tree at a time

---
<!-- .slide: data-background-color="#FCE4EC" -->
# Ensemble Family #2: Boosting

Boosting builds models **sequentially**.

**Idea**

- Model 1 makes predictions
- Model 2 focuses on Model 1's mistakes
- Model 3 focuses on remaining mistakes
- Continue and add them together

---
<!-- .slide: data-background-color="#FCE4EC" -->
# Gradient Boosting Intuition

Each new small tree learns from **residuals**:

> Residual = actual − predicted

- If previous model **underpredicted**, new model pushes prediction **up**
- If previous model **overpredicted**, new model pushes prediction **down**

---
<!-- .slide: data-background-color="#FCE4EC" -->
# Gradient Boosting Hyperparameters

Important knobs:

- `n_estimators` — how many trees
- `learning_rate` — how much each tree contributes
- `max_depth` — complexity per tree

**Classroom intuition**

- Small learning rate + more trees = careful learning

---
<!-- .slide: data-background-color="#FCE4EC" -->
# Boosting Pros / Cons

**Pros**

- Often excellent predictive accuracy
- Learns complex patterns gradually

**Cons**

- More sensitive to tuning choices
- Can overfit if pushed too far
- Usually less interpretable

---
<!-- .slide: data-background-color="#FFF8E7" -->
# Bagging vs Boosting (Quick Compare)

| Idea | Bagging (Random Forest) | Boosting (Gradient Boosting) |
|---|---|---|
| Training style | Parallel | Sequential |
| Main goal | Reduce variance | Reduce bias + errors |
| Typical stability | Very robust | Powerful but tuning-sensitive |
| Speed | Often faster | Can be slower |

---
<!-- .slide: data-background-color="#1565C0" -->
# Section 4
## How We Judge Models
### Metrics, plots, and fair comparison

---
<!-- .slide: data-background-color="#E3F2FD" -->
# Metrics: How We Judge Models

### MSE (Mean Squared Error)
- Average squared prediction error
- **Lower is better**

### R² (R-squared)
- How much variation in target is explained
- **Higher is better** (closer to 1.0)

---
<!-- .slide: data-background-color="#E3F2FD" -->
# Metric Interpretation Example

Suppose:

| Model | MSE | R² |
|---|---|---|
| Model A | 0.52 | 0.62 |
| Model B | 0.41 | 0.70 |

Which is better?

- Usually **Model B** (lower error + higher explained variance)

---
<!-- .slide: data-background-color="#E3F2FD" -->
# Actual vs Predicted Plot

How to read it:

- Perfect predictions lie on the **diagonal line**
- Closer points = better predictions
- Wide spread = larger errors

**Ask yourself**

- Which model's points are closest to the line?

---
<!-- .slide: data-background-color="#E3F2FD" -->
# Feature Importance (Careful Interpretation)

Feature importance tells us which features helped prediction most.

**Important caution**

- Importance does **not** prove cause-and-effect
- It only reflects predictive usefulness in this model

---
<!-- .slide: data-background-color="#E3F2FD" -->
# Model Comparison Workflow

1. Train all candidate models on same training split
2. Evaluate all on same test split
3. Compare MSE and R²
4. Inspect plots (actual vs predicted)
5. Choose model + explain tradeoffs

---
<!-- .slide: data-background-color="#FFF8E7" -->
# Classroom Discussion Prompt

If two models are close in performance, which would you choose?

Consider:

- Accuracy
- Interpretability
- Training time
- Ease of explanation to a non-technical audience

---
<!-- .slide: data-background-color="#6A1B9A" -->
# Section 5
## Practice Time
### Activity + reflection + exit ticket

---
<!-- .slide: data-background-color="#F3E5F5" -->
# In-Class Activity (12–15 min)

In groups of 2–3:

1. Compare Decision Tree, Random Forest, Gradient Boosting
2. Fill this sentence:
   - "Our best model is ___ because ___"
3. Name one risk/limitation of your chosen model
4. Share one practical use case

---
<!-- .slide: data-background-color="#F3E5F5" -->
# Guided Reflection Questions

- Why is one tree easier to explain than an ensemble?
- Why might Random Forest beat a single tree?
- Why might Gradient Boosting beat Random Forest on some datasets?
- Why should we always check test performance?

---
<!-- .slide: data-background-color="#FFF3E0" -->
# Common Student Mistakes

- Using only training score
- Forgetting MSE direction (**lower** is better)
- Assuming high R² means "perfect"
- Treating feature importance as causality
- Ignoring model tradeoffs (interpretability vs accuracy)

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Where SVM Fits (Brief Extension)

SVM is a different model family.

In your notebook, SVM is also explored, including ensemble versions:

- Bagged SVR
- AdaBoost with SVR base estimator

**Main message**

- Ensemble concepts can extend beyond trees.

---
<!-- .slide: data-background-color="#ECEFF1" -->
# Mini Glossary

| Term | Meaning |
|---|---|
| **Residual** | actual − predicted |
| **Overfitting** | memorizes noise |
| **Generalization** | performs well on new data |
| **Hyperparameter** | setting chosen before training |
| **Baseline model** | simple model used for comparison |

---
<!-- .slide: data-background-color="#FFF8E7" -->
# Exit Ticket (Last 5 min)

Write brief answers:

1. In one sentence, what is ensemble learning?
2. One difference between bagging and boosting?
3. Why can deep trees overfit?
4. Which metric should go **down**? Which should go **up**?

---
<!-- .slide: data-background-color="#1F4E79" -->
# Summary

Today we learned:

- Decision tree mechanics and vocabulary
- Why one tree can overfit
- How Random Forest stabilizes predictions
- How Gradient Boosting corrects errors step-by-step
- How to evaluate and explain model quality using MSE and R²

---
<!-- .slide: data-background-color="#E8F4F8" -->
# Optional Homework Prompt

Using your Week 9 notebook:

1. Change one hyperparameter for each model
2. Record new MSE and R²
3. Write 4–5 sentences comparing results
4. Explain one tradeoff between accuracy and interpretability

---
<!-- .slide: data-background-color="#1F4E79" -->
# Next Class Preview

Possible next topics:

- Hyperparameter tuning with simple grid search
- Cross-validation for more reliable model comparison
- Classification with ensemble methods
