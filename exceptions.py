
class NoListingsFoundError(Exception):
    """Raised when no job listings are found on the page."""
    def __init__(self, message="No job listings found on the page."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"NoListingsFoundError: {self.message}\n mayb the page structure has changed or the selector is incorrect."