"""Module source.py"""
import logging

import datasets

import src.data.dictionary
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.ingress


class Source:
    """
    Retrieves and prepares the California Bills documents/data
    """

    def __init__(self, service: sr.Service,  s3_parameters: s3p, warehouse: str):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.
        :param warehouse: The temporary local directory where data sets are initially placed,
                          prior to transfer to Amazon S3 (Simple Storage Service)
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters
        self.__warehouse: str = warehouse

        # Instances
        self.__dictionary = src.data.dictionary.Dictionary()

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

    def exc(self) -> list[str]:
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

        # Inventory of data files
        strings = self.__dictionary.exc(
            path=self.__warehouse, extension='*', prefix=self.__s3_parameters.path_internal_splits)

        # Transfer
        messages = src.s3.ingress.Ingress(
            service=self.__service, bucket_name=self.__s3_parameters.internal).exc(strings=strings)

        return messages
