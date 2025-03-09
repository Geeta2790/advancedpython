class Singleton:
    """A thread-safe singleton class implementation."""
    _instance = None
    _lock = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._get_lock():
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def _get_lock(cls):
        if cls._lock is None:
            from threading import Lock
            cls._lock = Lock()
        return cls._lock

    def some_business_logic(self):
        """Example business logic that can be executed on the singleton instance."""
        pass