class DataSourceInterface:
    """
    Interface for data source classes.
    """

    def get_data(self):
        """
        Retrieve data from the data source.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def save_data(self, data):
        """
        Save data to the data source.
        """
        raise NotImplementedError("Subclasses must implement this method.")