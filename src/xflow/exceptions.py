class BaseXFlowException(Exception):
    """Base Exception"""


class XFlowFeatureError(BaseXFlowException):
    """Feature run error"""


class XFlowStageError(BaseXFlowException):
    """Stage run error"""


class XFlowException(BaseXFlowException):
    """XFlow run error"""


class XFlowDBException(BaseXFlowException):
    """XFlow DB error"""
