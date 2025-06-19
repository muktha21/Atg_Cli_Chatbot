class ChatMemory:
    def __init__(self, max_turns=3):
        self.max_turns = max_turns
        self.history = []

    def add_turn(self, user_input, bot_reply):
        self.history.append((user_input, bot_reply))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return self.history
