from abc import ABC, abstractmethod

class SocialInterface(ABC):
    @abstractmethod
    async def post(self, text, photo, filename):
        pass