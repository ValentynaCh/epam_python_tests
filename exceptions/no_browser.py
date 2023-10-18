class NoBrowser(Exception):
    def init(self, browser: str):
        message = f"Browser [{browser}] not exists."
        super().__init__(message)
