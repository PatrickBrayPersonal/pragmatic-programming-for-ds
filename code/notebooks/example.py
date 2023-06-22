import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.data.features import pattern_std
from src.data.read import file_to_df
from src.data.transform import drop_pattern
from src.data.write import df_to_file
from src.evaluate.evaluators import evaluate_binary_class
from src.models.train_model import train_model
from src.utils import pipeline_to_name

df = file_to_df("data/raw/PredictiveManteinanceEngineTraining.csv")
df = drop_pattern(df, "setting.*")
df["s_std"] = pattern_std(df, "s[0-9][0-9]?")
df_to_file(df, "data/processed/PredictiveManteinanceEngineTraining.csv")

print("complete")

model = Pipeline(
    [("scaler", StandardScaler()), ("classifier", LogisticRegression())]
)
with mlflow.start_run(run_name=pipeline_to_name(model)) as run:
    model = train_model(
        model, df.drop(["label1", "label2", "RUL"], axis=1), df["label1"]
    )
    evaluate_binary_class(
        model, X=df.drop(["label1", "label2", "RUL"], axis=1), y=df["label1"]
    )
mlflow.end_run()
