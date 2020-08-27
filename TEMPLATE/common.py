
import os


def make_sure_path_exists(path):
    """Create directory if it does not exist.

    Parameters
    ----------
    path : str
        The path to the directory which should be created.

    Returns
    -------
    bool
        True if the path exists.

    Raises
    ------
    BioLibIOException
        If an error was encountered while creating the directory.
    """
    if not path:
        # lack of a path qualifier is acceptable as this
        # simply specifies the current directory
        return True
    elif os.path.isdir(path):
        return True

    try:
        os.makedirs(path)
        return True
    except OSError:
        raise
