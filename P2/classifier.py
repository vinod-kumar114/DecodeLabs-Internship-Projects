"""
DecodeLabs - Artificial Intelligence Internship
Project 2: Data Classification Using AI

Goal:
    Build a basic classification model using a small dataset.

Key Requirements met:
    - Load and understand a dataset
    - Split data into training and testing sets
    - Apply a simple classification algorithm

Key Skills:
    Data handling, supervised learning basics, model training.

Dataset used: Iris flower dataset (built into scikit-learn).
    It has 150 samples of iris flowers, each with 4 features
    (sepal length, sepal width, petal length, petal width) and a
    target label: the species (Setosa, Versicolor, Virginica).

Author: Vinod
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def load_and_understand_data():
    """
    Step 1: Load the dataset and print basic information about it
    so we understand what we are working with before training.
    """
    iris = load_iris()

    # Convert to a pandas DataFrame for easy viewing
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = [iris.target_names[i] for i in iris.target]

    print("=" * 55)
    print(" STEP 1: LOAD & UNDERSTAND THE DATASET")
    print("=" * 55)
    print(f"Shape of dataset: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("First 5 rows:")
    print(df.head(), "\n")
    print("Class distribution (how many samples per species):")
    print(df["species"].value_counts(), "\n")

    return iris, df


def split_data(iris):
    """
    Step 2: Split the dataset into training and testing sets.
    We use 80% of the data for training and 20% for testing.
    """
    X = iris.data          # features (sepal/petal measurements)
    y = iris.target        # labels (species)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("=" * 55)
    print(" STEP 2: SPLIT DATA INTO TRAIN / TEST SETS")
    print("=" * 55)
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples:  {len(X_test)}\n")

    return X_train, X_test, y_train, y_test


def train_and_evaluate_model(X_train, X_test, y_train, y_test, iris):
    """
    Step 3: Apply a simple classification algorithm (K-Nearest
    Neighbors), train it on the training set, and evaluate it
    on the unseen testing set.
    """
    print("=" * 55)
    print(" STEP 3: TRAIN & EVALUATE THE CLASSIFICATION MODEL")
    print("=" * 55)

    # K-Nearest Neighbors is one of the simplest classification
    # algorithms: it classifies a new point based on the majority
    # label among its 'k' closest neighbors in the training data.
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # Predict on the test set (data the model has NOT seen before)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy on test data: {accuracy * 100:.2f}%\n")

    print("Detailed classification report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    print("Confusion matrix (rows = actual, columns = predicted):")
    print(confusion_matrix(y_test, y_pred))

    return model


def try_a_new_prediction(model, iris):
    """
    Bonus: show the model classifying a brand new, unseen flower
    measurement, to demonstrate the model is actually usable.
    """
    print("\n" + "=" * 55)
    print(" BONUS: PREDICT A NEW, UNSEEN SAMPLE")
    print("=" * 55)

    # Example measurements: sepal length, sepal width, petal length, petal width
    new_sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(new_sample)
    species_name = iris.target_names[prediction[0]]

    print(f"New sample measurements: {new_sample[0]}")
    print(f"Predicted species: {species_name}")


def main():
    iris, df = load_and_understand_data()
    X_train, X_test, y_train, y_test = split_data(iris)
    model = train_and_evaluate_model(X_train, X_test, y_train, y_test, iris)
    try_a_new_prediction(model, iris)


if __name__ == "__main__":
    main()
