from pandas import DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.base import ClassifierMixin
from joblib import dump, load
from datetime import datetime


class Machine:
    def __init__(self, df: DataFrame):
        """
        Initialize the ML model.
        Args:
            df: DataFrame containing features and target "Rarity"
        """
        self.name = "Logistic Regression Classifier"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Explicit numeric feature columns (matches notebook)
        self.feature_cols = ["Level", "Health", "Energy", "Sanity"]

        # Split features and target
        self.features = df[self.feature_cols]
        self.target = df["Rarity"]

        # Train the model
        self.model: ClassifierMixin = LogisticRegression(max_iter=1000)
        self.model.fit(self.features, self.target)

    def __call__(self, pred_basis: DataFrame):
        """
        Predict using the trained model.
        Args:
            pred_basis: DataFrame with feature columns
        Returns:
            prediction, probability of prediction
        """
        pred_basis = pred_basis[self.feature_cols]

        prediction = self.model.predict(pred_basis)[0]
        prob = self.model.predict_proba(pred_basis).max()

        return prediction, prob

    def save(self, filepath: str):
        """Save the trained model to a file."""
        dump(self, filepath)

    @classmethod
    def open(cls, filepath: str):
        """Load a saved model from a file."""
        return load(filepath)

    def info(self) -> str:
        """Return model name and initialization timestamp."""
        return f"{self.name} initialized at {self.timestamp}"


