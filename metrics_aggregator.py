# metrics_aggregator.py
# Aggregates performance and response metrics using Pandas

import pandas as pd

class MetricsAggregator:
    def __init__(self):
        # Initialize an empty DataFrame to store metrics
        self.metrics_df = pd.DataFrame()

    def add_data(self, data):
        """
        Adds new data to the metrics DataFrame
        :param data: A dictionary or DataFrame containing new data
        """
        if isinstance(data, dict):
            # Convert dictionary to DataFrame
            data = pd.DataFrame([data])
        self.metrics_df = pd.concat([self.metrics_df, data], ignore_index=True)

    def aggregate_metrics(self):
        """
        Aggregates the metrics data and returns summary statistics
        :return: A DataFrame with summary statistics
        """
        if self.metrics_df.empty:
            return "No data to aggregate."

        # Example aggregation: mean, median, and standard deviation
        summary = self.metrics_df.agg(['mean', 'median', 'std'])
        return summary

    def filter_data(self, conditions):
        """
        Filters the data based on given conditions
        :param conditions: Conditions to filter the data
        :return: Filtered DataFrame
        """
        filtered_data = self.metrics_df.query(conditions)
        return filtered_data

    # Additional methods for more complex aggregations or statistics as needed

# Example usage
if __name__ == '__main__':
    aggregator = MetricsAggregator()

    # Example data (replace with real metric data)
    data = [
        {'metric1': 10, 'metric2': 200},
        {'metric1': 15, 'metric2': 220},
        {'metric1': 12, 'metric2': 210}
    ]

    for d in data:
        aggregator.add_data(d)

    print("Aggregated Metrics:")
    print(aggregator.aggregate_metrics())

    print("\nFiltered Data (metric1 > 10):")
    print(aggregator.filter_data("metric1 > 10"))
