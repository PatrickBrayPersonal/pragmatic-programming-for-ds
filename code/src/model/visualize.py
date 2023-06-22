import matplotlib.pyplot as plt
import mlflow
import numpy as np
from sklearn.metrics import auc, precision_recall_curve, roc_curve

from src.utils import error


def pr_curve(y, y_hat):
    precisions, recalls, thresholds = precision_recall_curve(y, y_hat)
    # plot the precision recall curve
    fig = plt.figure()
    plt.plot(recalls, precisions, "b-")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision Recall Curve for Binary Classification")
    mlflow.log_figure(fig, "test_pr_curve.png")


def roc_auc_curve(y, y_hat):
    # calculate false positive rate and true positive rate for different thresholds
    fpr, tpr, thresholds = roc_curve(y, y_hat)

    # calculate the area under the curve (AUC)
    roc_auc = auc(fpr, tpr)

    # plot the ROC curve
    fig = plt.figure()
    plt.plot(fpr, tpr, "b-")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC Curve (AUC = {round(roc_auc, 3)})")
    mlflow.log_figure(fig, "test_roc_auc_curve.png")


def binary_violin(y: np.ndarray, y_hat: np.ndarray):
    """
    make a matplotlib violiplot of the binary probabilities predicted by y_hat
    """
    # make a violin plot in matplotlib using y and y_hat
    labels = y.unique()
    if len(labels) > 2:
        error(f"y must be binary {labels}")
    fig = plt.figure()
    plt.violinplot(
        (y_hat[y.values == labels[0]], y_hat[y.values == labels[1]]),
        positions=labels,
        showmeans=True,
    )
    plt.ylabel("Predicted Probability")
    plt.xlabel("True Label")
    plt.title("Binary Probability Violin Plot")
    mlflow.log_figure(fig, "test_binary_violin.png")
