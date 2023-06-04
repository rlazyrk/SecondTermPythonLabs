class NegativeFlowersException(Exception):
    """
    :exception class
    """
    def __init__(self, message="Flowers cannot be negative"):
        super().__init__(self, message)
