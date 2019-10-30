
class ObjectEventHandler:

    def __init__(self, obj_handler):

        self.listeners = {}  # {event-type: {publisher: {caller: [function to call, *args]}}}
        self.parent = obj_handler

    def add_listener(self, event_key, source, callback, lifespan, *args):
        """
        :param event_key: the key for the event, view the event docs for which key to use.
        :param source: The object that is the subscriber of the event.
        :param callback: The function called upon this events activation.
        :param lifespan: How many times this event is called before the subscriber is removed
                          from the list. 0 is infinite or until the subscriber object is dead.
        :param args: Any arguments the subscriber wants passed to the callback function.
        :return: None
        :return:
        """
        if event_key in self.listeners:
            self.listeners[event_key].append([source, callback, lifespan, args])
        else:
            self.listeners[event_key] = [[source, callback, lifespan, args]]

    def find_subscriber_by_event(self, event_key, source):

        if event_key in self.listeners:
            for subscriber in self.listeners[event_key]:
                if subscriber[0] == source:
                    return subscriber

    def call_listeners(self, event_key):

        if event_key in self.listeners:
            for event in self.listeners:
                for listener in self.listeners[event]:
                    listener[0](listener[1])

            del self.listeners[event_key]

    def listen_friendly_unit_takes_damage(self, source, callback, lifespan, *args):
        """
        :param source: The object that is the subscriber of the event.
        :param callback: The function called upon this events activation.
        :param lifespan: How many times this event is called before the subscriber is removed
                          from the list. 0 is infinite or until the subscriber object is dead.
        :param args: Any arguments the subscriber wants passed to the callback function.
        :return: None
        """
        pass
