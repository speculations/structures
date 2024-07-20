"""Module setup.py"""
import config
import src.functions.directories


class Setup:
    """

    Description
    -----------

    Sets up local & cloud environments
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

    def __local(self):

        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__configurations.warehouse)
        directories.create(path=self.__configurations.warehouse)

    def exc(self):

        self.__local()
