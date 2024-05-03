# README

## Overview

This README provides a detailed explanation of the code in the `main.ipynb` Jupyter notebook, which implements a movie recommendation system using Non-negative Matrix Factorization (NMF) integrated with MLflow for experiment tracking and MongoDB for data management.

## Code Explanation

### Importing Libraries

The notebook begins by importing necessary Python libraries for data manipulation, visualization, machine learning, and database interaction. This setup ensures that all tools required for executing the tasks are available.

### Dataset Split Configuration

This section allows the user to configure how the Movielens dataset is split into training and testing sets. It supports experimentation with both full datasets and smaller subsets for quicker iterations during development.

### NMF Recommender System Overview

- **Class `NMFRecommender`**: Implements a recommender system using the NMF technique, which predicts user preferences by factorizing the user-item interaction matrix into matrices representing latent features of users and items.
- **MongoDB Integration**: Initializes connections to MongoDB to fetch movie and user data.
- **MLflow Setup**: Configures MLflow for tracking experiments, storing model parameters, and versions.

### Data Preparation Workflow

- **Data Fetching and Saving**: Checks for the existence of movie and user data files; if not present, it fetches the data from MongoDB, processes it, and saves it as CSV files. This prevents repeated data fetching and speeds up future runs.
- **Data Loading**: If CSV files are available, loads data directly from them.

### Data Merging and Preprocessing

- **Combines user and movie data** into a single DataFrame and performs various preprocessing steps such as renaming columns, sorting data, and resetting indices for better data organization and access.

### Data Filtering by Ratings

This block evaluates the distribution of ratings across movies and users, applying thresholds to filter out those with insufficient interactions, ensuring the robustness and reliability of the recommendation system.

### Dataset Splitting for Training and Testing

Depending on configuration settings, divides the dataset into training and testing portions to prepare for model training and evaluation.

### Model Training

- **Sparse Matrix Creation**: Converts the training data into a sparse matrix format suitable for NMF processing.
- **NMF Model Training**: Trains the NMF model using the training data, capturing the latent features in matrices `U_train` and `M`.

### Prediction and Evaluation

- **Matrix Reconstruction**: Uses the trained NMF model to predict missing ratings.
- **Error Calculation**: Computes Mean Squared Error (MSE) for both training and test datasets to evaluate model performance.
- **MLflow Tracking**: Logs model parameters and performance metrics in MLflow for monitoring and version control.

### Correlation Analysis

- **Ranking and Correlation**: After predicting ratings, ranks items for each user and calculates correlation metrics to assess the quality of recommendations.

### Conclusion

The notebook ends with steps to normalize matrix data, showcasing an additional data manipulation technique. It uses both Pearson and Spearman correlation coefficients to evaluate the recommendation system's performance.

## Running the Notebook

Ensure you have all dependencies installed and MongoDB running with the required access permissions. Configure MLflow as per your environment setup before running the notebook to track experiments effectively.
