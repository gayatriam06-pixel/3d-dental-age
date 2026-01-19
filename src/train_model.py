import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from config import PROCESSED_DATA_DIR, MODEL_DIR

def train():
    df = pd.read_csv(PROCESSED_DATA_DIR / "dataset.csv")

    X = df.drop(columns=["age", "sex"])
    y_age = df["age"]
    y_sex = df["sex"]

    age_model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    sex_model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    age_model.fit(X, y_age)
    sex_model.fit(X, y_sex)

    joblib.dump(age_model, MODEL_DIR / "age_model.pkl")
    joblib.dump(sex_model, MODEL_DIR / "sex_model.pkl")

    print("Models trained and saved.")

if __name__ == "__main__":
    train()