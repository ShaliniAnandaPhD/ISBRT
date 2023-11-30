# model_trainer.py
# Manages the training and updating of models

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

class ModelTrainer:
    def __init__(self):
        # Initialize the model (here, using a Random Forest Classifier as an example)
        self.model = RandomForestClassifier()

    def train_model(self, X, y):
        """
        Train the model with the given features and labels.
        :param X: Feature set
        :param y: Labels
        """
        # Splitting the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Training the model
        self.model.fit(X_train, y_train)

        # Evaluating the model
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model trained with accuracy: {accuracy}")

        # Saving the trained model
        joblib.dump(self.model, 'trained_model.pkl')

    def update_model(self, X_new, y_new):
        """
        Update the model with new data.
        :param X_new: New feature set
        :param y_new: New labels
        """
        # Loading the existing model
        self.model = joblib.load('trained_model.pkl')

        # Updating the model with new data
        self.model.fit(X_new, y_new)
        print("Model updated with new data.")

        # Saving the updated model
        joblib.dump(self.model, 'trained_model.pkl')

    # Additional model training and updating methods as needed

# Example usage
if __name__ == '__main__':
    trainer = ModelTrainer()

    # Dummy data for demonstration purposes (replace with actual data)
    X, y = [[0, 0], [1, 1], [2, 2], [3, 3]], [0, 1, 1, 0]
    trainer.train_model(X, y)

    # Update model with new data
    X_new, y_new = [[4, 4], [5, 5]], [1, 0]
    trainer.update_model(X_new, y_new)
