"""Module main.py"""
import logging
import os
import sys


def main() -> None:
    """
    Entry point

    :return:
        None
    """

    logger: logging.Logger = logging.getLogger(__name__)

    # Set up
    src.setup.Setup(
        warehouse=configurations.warehouse).exc()

    # Explorations
    src.data.source.Source(
        warehouse=configurations.warehouse).exc()

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
    import config
    import src.functions.cache
    import src.data.source
    import src.setup

    configurations = config.Config()

    main()
