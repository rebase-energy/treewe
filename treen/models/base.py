from abc import abstractmethod
from enflow import Predictor

class BasePredictor(Predictor):
    """
    Abstract base class for all models (LightGBM, XGBoost, CatBoost).
    This class standardizes the interface for model prediction, feature importance, and SHAP values.
    """

    @abstractmethod
    def fit(self, X, y):
        """Train the model on the provided data."""
        pass

    @abstractmethod
    def predict(self, X):
        """Make predictions on the provided data."""
        pass

    @property
    @abstractmethod
    def feature_names(self):
        """Return the feature names of the trained model."""
        pass

    @property
    @abstractmethod
    def can_predict_quantiles(self):
        """Indicate if the model supports quantile prediction."""
        pass

    @property
    @abstractmethod
    def feature_importance(self):
        """Return the feature importance scores of the trained model."""
        pass

    @property
    @abstractmethod
    def shap_values(self, X):
        """Return the SHAP values for the provided data."""
        pass
