from abc import ABC, abstractmethod

class SocialModuleInterface(ABC):
    @abstractmethod
    async def post(self, text, photo, filename):
        pass