import mlflow


def train_model(model, X, y, **kwargs):
    """
    Fit the model to the training data.
    """
    mlflow.sklearn.autolog()
    mlflow.log_param("label", y.name)
    model.fit(X, y)
    return model
