import pickle

class ModeloOrange:
    def __init__(self):
        with open('logistic_regression_model.pkcls', 'rb') as model_file:
            self.model = pickle.load(model_file)

    def predict(self, features):
        # Asumiendo que el modelo espera un array de características ya preprocesadas
        return self.model.predict([features])[0]