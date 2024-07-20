"""Module setup.py"""
import src.functions.directories


class Setup:
    """
    Description
    -----------

    Sets up local & cloud environments
    """

    def __init__(self, warehouse: str):
        """

        :param warehouse: The temporary local directory where data sets are initially placed,
                          prior to transfer to Amazon S3 (Simple Storage Service)
        """

        self.__warehouse = warehouse

    def __local(self):
        """

        :return:
        """

        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__warehouse)
        directories.create(path=self.__warehouse)

    def exc(self):
        """

        :return:
        """

        self.__local()
