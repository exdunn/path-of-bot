

class Manager():
    """
    Bot Manager class which stores search information

    Attributes
    --------------
    ladder: int
        The default ladder used when querying PoE Ladder API
    limit: int
        The default limit used when querying PoE Ladder API
    accounts
        List of account names stored for quick access when querying PoE Ladder API
    """

    def __init__(self, **kwargs):
        self.accounts = []
        self.ladder = 0
        self.limit = 5

