


class Conversation:

    def __init__(self) -> None:
        self.conversation = []
    

    def add(self, message: str) -> None:
        if (len(self.conversation) < 51):
            self.conversation.append(message)
        else:
            self.conversation.pop(0)
            self.conversation.append(message)

    def get(self) -> str:
        return self.conversation