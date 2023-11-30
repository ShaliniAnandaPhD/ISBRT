# analytics_insights.py
# Analyzes scenarios and personas

from collections import Counter
from textblob import TextBlob
import pandas as pd

class AnalyticsInsights:
    def analyze_scenarios(self, scenarios):
        """
        Analyze scenarios for common themes, sentiment, etc.
        :param scenarios: List of scenario descriptions
        :return: Analysis results as a dictionary
        """
        analysis_results = {
            "sentiment_analysis": self.sentiment_analysis(scenarios),
            "common_themes": self.common_themes(scenarios)
        }
        return analysis_results

    def sentiment_analysis(self, scenarios):
        """
        Perform sentiment analysis on scenarios.
        :param scenarios: List of scenario descriptions
        :return: Average sentiment score
        """
        sentiments = [TextBlob(scenario).sentiment.polarity for scenario in scenarios]
        avg_sentiment = sum(sentiments) / len(sentiments)
        return avg_sentiment

    def common_themes(self, scenarios):
        """
        Identify common themes in scenarios.
        :param scenarios: List of scenario descriptions
        :return: Most common words or themes
        """
        words = ' '.join(scenarios).split()
        most_common = Counter(words).most_common(10)
        return most_common

    def analyze_personas(self, personas):
        """
        Analyze personas for demographic distribution, interests, etc.
        :param personas: List of persona dictionaries
        :return: Analysis results as a dictionary
        """
        df = pd.DataFrame(personas)
        analysis_results = {
            "demographic_distribution": df['Demographics'].value_counts().to_dict(),
            "interests_distribution": df['Interests'].value_counts().to_dict()
            # Add more analyses as needed
        }
        return analysis_results

    # Additional analysis methods as needed

# Example usage
if __name__ == '__main__':
    analytics = AnalyticsInsights()

    # Example scenario data
    scenarios = [
        "A customer visits a new website and faces difficulty in navigation.",
        "A user tries to make a purchase but encounters a payment error."
    ]

    # Example persona data
    personas = [
        {"Name": "Alice", "Demographics": "25, Female", "Interests": "Technology, Reading"},
        {"Name": "Bob", "Demographics": "30, Male", "Interests": "Sports, Travel"}
    ]

    print("Scenario Analysis:", analytics.analyze_scenarios(scenarios))
    print("Persona Analysis:", analytics.analyze_personas(personas))
