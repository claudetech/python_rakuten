class RakutenApiException(Exception):
    def __init__(self, code, message):
        super(RakutenApiException, self).__init__(message)
        self.message = message
        self.code = code

