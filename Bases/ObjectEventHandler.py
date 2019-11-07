
class ObjectEventHandler:

    def __init__(self, obj_handler):
        """
        Constructor for our Object Event Handler. Creates our dictionary of events.
        :param obj_handler: The parent obj handler that the event handler will use to check if
                            objects are alive.
        """
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
        :return: None
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

    def event_new_friendly_unit(self, source, target, unit_id):
        """
        Event ID 0, event fires when a new friendly unit is created.
        :param source: Who created the unit, or None if it is the Object handler
        :param target: the unit that was created
        :param unit_id: the ID of the unit created, see Unit docs
        :return: None
        """
        # TODO
        pass
