"""
This is data type S3Parameters
"""
import typing


class S3Parameters(typing.NamedTuple):
    """
    The data type class ⇾ S3Parameters

    Attributes
    ----------
    region_name : str
      The Amazon Web Services region code.

    location_constraint : str
      The region code of the region that the data is limited to.

    internal : str
      The Amazon S3 (Simple Storage Service) bucket that hosts this project's data.

    path_internal_splits : str
      The bucket path of data splits.

    path_internal_artefacts : str
      The bucket path of the model development artefacts.

    external: str
      The name of the bucket that the project's calculations will be delivered to.

    """

    region_name: str
    location_constraint: str
    internal: str
    path_internal_splits: str
    path_internal_artefacts: str
    external: str
