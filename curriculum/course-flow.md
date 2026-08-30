# DATA 201 — Fall 2026 (CRN 21732)

## Course Flow: Topics and Learning Objectives

> For the official meeting schedule, grading, and due dates, see the [Fall 2026 syllabus](../DATA%20201%20Fall%202026%20Syllabus%20CRN21732.pdf) and [README](../README.md).

**Course format:** 14-week semester, 2 × 75-minute classes per week\
**Audience:** Students with prior R experience, transitioning to Python
and modern data science / machine learning

------------------------------------------------------------------------

# Weeks 1--3: Python for R Users

## Foundational Skills Block

### Topics

-   Python syntax and control flow\
-   NumPy arrays vs. R vectors\
-   pandas DataFrames vs. `data.frame`\
-   Plotting and visualization in Python\
-   Jupyter notebooks and reproducible workflows

### Learning Objectives

-   Translate common R workflows into Python\
-   Manipulate and summarize tabular data using pandas\
-   Create basic visualizations in Python\
-   Write clean, reproducible Jupyter notebooks

------------------------------------------------------------------------

# Week 4: Linear Regression & Diagnostics

## Beginning Model Form Reasoning

### Topics

-   Linear regression refresher\
-   Exploratory Data Analysis (EDA) for regression\
-   Residual plots\
-   Detecting nonlinearity and interactions\
-   Distinguishing model form from noise

### Learning Objectives

-   Use EDA to hypothesize relationships between predictors and
    outcomes\
-   Diagnose violations of linear regression assumptions\
-   Distinguish random noise from systematic model misfit\
-   Explain the difference between model form and feature inclusion

**Associated Assessment:** Lab 1 -- EDA and baseline linear regression

------------------------------------------------------------------------

# Week 5: Model Form & Feature Selection (Linear Regression)

### Topics

-   Transformations, polynomial terms, and interactions\
-   Feature selection for linear regression\
-   Multicollinearity and VIF\
-   Adjusted R², AIC/BIC, partial F-tests\
-   Interpretability and stability tradeoffs

### Learning Objectives

-   Use diagnostics to justify changes to model form\
-   Apply feature selection criteria specific to OLS regression\
-   Explain tradeoffs between complexity and interpretability\
-   Distinguish model selection from feature selection

**Associated Assessment:** Lab 2 -- Model form and linear feature
selection

------------------------------------------------------------------------

# Week 6: Logistic Regression & Feature Selection

## Classification with Linear Models

### Topics

-   Logistic regression refresher\
-   Linear vs. logistic modeling goals\
-   Feature selection for logistic regression\
-   Rare predictors and risk framing\
-   Conceptual L1 regularization\
-   Side-by-side comparison of linear and logistic regression

### Learning Objectives

-   Fit and interpret logistic regression models\
-   Explain how feature selection priorities differ for classification\
-   Reason about rare but important predictors\
-   Compare inference-oriented and prediction-oriented modeling goals

**Associated Assessment:** Lab 3 -- EDA, logistic regression, and
feature selection

------------------------------------------------------------------------

# Week 7: Generalized Linear Models (GLMs)

## Unification of Classical Statistical Models

### Topics

-   GLMs as a family of models\
-   Linear predictor, link function, and loss function\
-   Polynomial functions as feature engineering\
-   Logistic regression reframed as a GLM\
-   Poisson regression for counts\
-   Gamma regression for positive, skewed outcomes\
-   Deviance and overdispersion\
-   Likelihood-based feature selection (AIC/BIC, likelihood ratio tests)

### Learning Objectives

-   Explain how linear, logistic, Poisson, and Gamma regression are
    unified\
-   Distinguish feature engineering from loss engineering\
-   Select appropriate GLMs based on outcome type\
-   Apply likelihood-based reasoning for model and feature selection

------------------------------------------------------------------------

# Week 8: Resampling & Model Evaluation

## How Do We Trust Models?

### Topics

-   Train/test split\
-   Cross-validation\
-   Bootstrap (conceptual)\
-   Bias--variance tradeoff\
-   Honest performance estimation

### Learning Objectives

-   Explain why training error is misleading\
-   Use resampling methods to estimate generalization performance\
-   Relate model complexity to bias and variance\
-   Apply evaluation ideas consistently across model families

------------------------------------------------------------------------

# Week 9: Regularization & Optimization

## Automated Complexity Control

### Topics

-   Ridge, Lasso, and Elastic Net\
-   Loss functions plus penalties\
-   Hyperparameter tuning with cross-validation\
-   Stability vs. sparsity\
-   Manual feature selection vs. regularization

### Learning Objectives

-   Explain how regularization controls model complexity\
-   Compare shrinkage-based and selection-based approaches\
-   Interpret regularized coefficients conceptually\
-   Connect regularization to earlier feature-selection decisions

------------------------------------------------------------------------

# Week 10: Neural Networks

## Gradient-Based Flexible Models

### Topics

-   Linear and logistic regression as one-layer neural networks\
-   Hidden layers as learned feature transformations\
-   Activation functions (ReLU, sigmoid)\
-   Loss functions in neural networks\
-   Overfitting and regularization in neural networks\
-   Role of resampling

### Learning Objectives

-   Explain neural networks as extensions of linear models\
-   Identify tradeoffs between flexibility and interpretability\
-   Relate neural networks to feature engineering and loss functions\
-   Understand when neural networks are appropriate (and when they are
    not)

------------------------------------------------------------------------

# Week 11: Support Vector Machines (SVMs)

## Margin-Based Learning

### Topics

-   Linear SVM classification\
-   Maximum margin intuition\
-   Hinge loss vs. log loss\
-   Soft margin and the regularization parameter C\
-   Support Vector Regression (SVR)\
-   Geometric interpretation of SVMs

### Learning Objectives

-   Contrast SVMs with logistic and linear regression\
-   Explain margin-based vs. probability-based modeling\
-   Interpret the role of support vectors\
-   Understand the bias--variance implications of the parameter C

------------------------------------------------------------------------

# Week 12: Trees & Ensembles

## Rule-Based Nonparametric Models

### Topics

-   Decision trees and recursive partitioning\
-   Automatic interactions\
-   Interpretability vs. instability\
-   Bagging and variance reduction\
-   Random forests\
-   Boosting (conceptual)

### Learning Objectives

-   Explain how trees model interactions automatically\
-   Identify sources of overfitting in trees\
-   Describe how ensembles improve stability\
-   Compare trees to linear models, SVMs, and neural networks

------------------------------------------------------------------------

# Week 13: Distance-Based Methods & Clustering

## Geometry of Data

### Topics

-   k-nearest neighbors (regression and classification)\
-   Distance metrics\
-   Feature scaling\
-   Curse of dimensionality\
-   k-means clustering\
-   Interpreting clusters

### Learning Objectives

-   Explain similarity-based learning\
-   Recognize the importance of scaling and representation\
-   Apply k-NN appropriately\
-   Perform and interpret basic clustering

------------------------------------------------------------------------

# Week 14: PCA, NLP Mini-Module & Synthesis

## Representation and Integration

### Topics

-   Principal Component Analysis (PCA) as structure discovery\
-   Variance explained and dimensionality reduction\
-   PCA vs. feature selection

### NLP Mini-Module

-   Text as high-dimensional data\
-   Bag-of-words and TF--IDF representations\
-   Logistic regression and linear SVMs for text\
-   PCA and clustering for documents

### Learning Objectives

-   Use PCA to understand structure in high-dimensional data\
-   Explain how representation affects modeling\
-   Apply familiar models to text data\
-   Synthesize modeling choices across paradigms\
-   Articulate tradeoffs between interpretability, performance, and
    responsibility

------------------------------------------------------------------------

# Unifying Course Learning Outcomes

-   Distinguish inference vs. prediction\
-   Reason about interpretability tradeoffs\
-   Separate model selection from feature selection\
-   Separate feature engineering from loss engineering\
-   Choose models responsibly based on data, goals, and constraints\
-   Evaluate models honestly using resampling\
-   Transfer modeling ideas across domains, including numeric,
    categorical, and text data
