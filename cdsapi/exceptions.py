
class CDSAPIException(Exception):
    """Base class for all CDS API exceptions."""
    pass


class MissingSettings(IOError, CDSAPIException):
    """Raised when settings are missing or incomplete."""
    pass


class APIError(CDSAPIException):
    """Raised when the CDS API returns a well-formed error."""
    pass


class FailedTask(CDSAPIException):
    """Raised when a request sent failed to be processed in the Server."""
    pass


class DownloadFailed(CDSAPIException):
    """Raised when a download size is less than the remote file size."""
    pass


class UnknownState(CDSAPIException):
    """Raised when the state of a task is unknown."""
    pass


class MaxRetriesExceeded(CDSAPIException):
    """Raised when the maximum number of retries is exceeded."""
    pass
