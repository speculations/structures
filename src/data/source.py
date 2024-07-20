"""Module source.py"""
import logging

import datasets


class Source:
    """
    Retrieves and prepares the California Bills documents/data
    """

    def __init__(self):
        """
        Constructor
        """

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

    def exc(self) -> datasets.DatasetDict:
        """

        :return:
        """

        data = self.__data()

        # The data segments
        self.__logger.info('The data segments:\n%s', data.keys())
        self.__logger.info('Training Set:\n%s', data['train'].shape)
        self.__logger.info('Validate Set:\n%s', data['validate'].shape)
        self.__logger.info('Test Set:\n%s', data['test'].shape)

        return data
