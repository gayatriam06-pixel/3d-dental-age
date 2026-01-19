import joblib
from feature_extraction import extract_features
from config import MODEL_DIR

def predict_from_stl(stl_path):
    age_model = joblib.load(MODEL_DIR / "age_model.pkl")
    sex_model = joblib.load(MODEL_DIR / "sex_model.pkl")

    features = extract_features(stl_path).reshape(1, -1)

    age_pred = age_model.predict(features)[0]
    sex_pred = sex_model.predict(features)[0]

    return {
        "Predicted Age (years)": round(age_pred, 1),
        "Predicted Sex": "Male" if sex_pred == 1 else "Female"
    }

if __name__ == "__main__":
    result = predict_from_stl("example_unlabeled.stl")
    print(result)
