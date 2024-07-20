"""Module source.py"""
import logging

import datasets


class Source:
    """
    Retrieves and prepares the California Bills documents/data
    """

    def __init__(self, warehouse: str):
        """

        :param warehouse: The temporary local directory where data sets are initially placed,
                          prior to transfer to Amazon S3 (Simple Storage Service)
        """

        self.__warehouse = warehouse

        # The Data: Herein, the dictionary segments are being reset such that
        # the segments are <training>, <validate>, and <test>; initially <training>,
        # <test>, and <ca_test>, respectively.
        self.__dataset: datasets.DatasetDict = datasets.load_dataset('billsum')
        validate = self.__dataset.pop('test')
        test = self.__dataset.pop('ca_test')

        # Hence
        self.__dataset['validate'] = validate
        self.__dataset['test'] = test

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __data(self) -> datasets.DatasetDict:
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

        self.__logger.info(dataset.keys())

        return dataset

    def __persist(self, data: datasets.DatasetDict):
        """

        :param data:
        :return:
        """

        data.save_to_disk(dataset_dict_path=self.__warehouse)

    def exc(self) -> None:
        """

        :return:
        """

        # data = self.__data()

        # The data segments
        self.__logger.info('The data segments:\n%s', self.__dataset.keys())
        self.__logger.info('Training Set:\n%s', self.__dataset['train'].shape)
        self.__logger.info('Validate Set:\n%s', self.__dataset['validate'].shape)
        self.__logger.info('Test Set:\n%s', self.__dataset['test'].shape)

        # Save
        self.__persist(data=self.__dataset)
