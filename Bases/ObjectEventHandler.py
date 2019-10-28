
class ObjectEventHandler:

    def __init__(self):

        self.listeners = {}  # {event-type: {publisher: {caller: [function to call, *args]}}}

    def add_listener(self, event_key, func, *args):

        if event_key in self.listeners:
            self.listeners[event_key].append({})
        else:
            self.listeners[event_key] = [[func, args]]

    def call_listeners(self, event_key):

        if event_key in self.listeners:
            for event in self.listeners:
                for listener in self.listeners[event]:
                    listener[0](listener[1])

            del self.listeners[event_key]
