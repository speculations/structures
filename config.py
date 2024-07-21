"""Module config.py"""
import os
import subprocess
import src.functions.serial


class Config:
    """
    Configuration
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        # A S3 parameters template
        # https://raw.githubusercontent.com/speculations/.github/master/profile/s3_parameters_text.yaml
        self.s3_parameters_template = 'https://raw.githubusercontent.com/speculations/.github/master/profile/s3_parameters_text.yaml'
