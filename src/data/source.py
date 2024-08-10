"""Module source.py"""
import logging

import datasets

import src.data.dictionary
import src.elements.s3_parameters as s3p


class Source:
    """
    Retrieves and prepares the California Bills documents/data
    """

    def __init__(self, warehouse: str, s3_parameters: s3p):
        """

        :param warehouse: The temporary local directory where data sets are initially placed,
                          prior to transfer to Amazon S3 (Simple Storage Service)
        """

        self.__warehouse = warehouse
        self.__s3_parameters = s3_parameters

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    @staticmethod
    def __data() -> datasets.DatasetDict:
        """

        :return:
        """

        # The Data: Herein, the dictionary segments are being reset such that
        # the segments are <training>, <validate>, and <test>; initially <training>,
        # <test>, and <ca_test>, respectively.
        dataset: datasets.DatasetDict = datasets.load_dataset('billsum')

        # Let the test node data be the validate data
        validate = dataset.pop('test')

        # Let the <ca_test> node data be the test data
        test = dataset.pop('ca_test')

        # Hence
        dataset['validate'] = validate
        dataset['test'] = test

        return dataset

    def __persist(self, data: datasets.DatasetDict):
        """

        :param data: The data set being saved.
        :return:
        """

        data.save_to_disk(dataset_dict_path=self.__warehouse)

    def __transfer(self):

        dictionary = src.data.dictionary.Dictionary()
        dictionary.exc(path=self.__warehouse, extension='*', prefix=self.__s3_parameters.path_internal_splits)

    def exc(self) -> None:
        """

        :return:
        """

        data = self.__data()

        # The data segments
        self.__logger.info('The data segments:\n%s', data.keys())
        self.__logger.info('Training Set:\n%s', data['train'].shape)
        self.__logger.info('Validate Set:\n%s', data['validate'].shape)
        self.__logger.info('Test Set:\n%s', data['test'].shape)

        # Save
        self.__persist(data=data)
