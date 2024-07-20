"""Module config.py"""
import os

class Config:
    """
    Configuration
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
