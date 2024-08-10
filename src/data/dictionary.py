"""Module dictionary.py"""
import glob
import logging
import os
import pathlib

import pandas as pd

import src.functions.objects


class Dictionary:
    """
    Class KeyStrings
    """

    def __init__(self):
        """
        Constructor
        """

        self.__objects = src.functions.objects.Objects()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __local(self, path: str, extension: str) -> pd.DataFrame:
        """

        :param path: The path wherein the files of interest lie
        :param extension: The extension type of the files of interest
        :return:
        """

        splitter = os.path.basename(path) + os.path.sep
        self.__logger.info(splitter)

        # The list of files within the path directory, including its child directories.
        files: list[str] = glob.glob(pathname=os.path.join(path, '**',  f'*.{extension}'),
                                     recursive=True)

        details: list[dict] = [
            {'file': file,
             'vertex': file.rsplit(splitter, maxsplit=1)[1]}
            for file in files]

        return pd.DataFrame.from_records(details)

    def __metadata(self) -> dict:
        """

        :return:
        """

        return {'description': 'Part of the Bills Summary corpus for the automatic summarisation of legislation.',
         'details': 'https://arxiv.org/abs/1910.00523'}

    def exc(self, path: str, extension: str, prefix: str) -> pd.DataFrame:
        """

        :param path: The path wherein the files of interest lie
        :param extension: The extension type of the files of interest
        :param prefix: The Amazon S3 (Simple Storage Service) where the files of path are heading
        :return:
        """

        local: pd.DataFrame = self.__local(path=path, extension=extension)
        # metadata: pd.DataFrame = self.__metadata(path=path, vertices=local['vertex'].tolist())
        # frame = local.copy().merge(metadata, how='left', on='vertex')

        # Building the Amazon S3 strings

        frame = local.assign(key=prefix + local["vertex"])
        # frame[['file', 'key', 'metadata']]

        return frame