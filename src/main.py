"""Module main.py"""
import logging
import os
import sys

import datasets


def main() -> None:
    """
    Entry point

    :return:
        None
    """

    logger: logging.Logger = logging.getLogger(__name__)

    # Set up
    src.setup.Setup().exc()

    # Explorations
    source: datasets.DatasetDict = src.data.source.Source().exc()


    # Delete Cache Points
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import src.functions.cache
    import src.data.source
    import src.setup

    main()
