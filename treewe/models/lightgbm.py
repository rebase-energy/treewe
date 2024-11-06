from .base import BasePredictor
import lightgbm as lgb
import shap

class LightGBMPredictor(BasePredictor):
    def __init__(self, params=None):
        self.model = None
        self.params = params if params else {}
        self._can_predict_quantiles = 'quantile' in self.params.get('objective', '')

    def fit(self, X, y):
        train_data = lgb.Dataset(X, label=y)
        self.model = lgb.train(self.params, train_data)
        self._feature_names = X.columns.tolist()

    def predict(self, X):
        return self.model.predict(X)

    @property
    def feature_names(self):
        return self._feature_names

    @property
    def can_predict_quantiles(self):
        return self._can_predict_quantiles

    @property
    def feature_importance(self):
        return self.model.feature_importance()

    def shap_values(self, X):
        explainer = shap.TreeExplainer(self.model)
        return explainer.shap_values(X)
