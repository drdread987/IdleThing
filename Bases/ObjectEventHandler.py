
class ObjectEventHandler:

    def __init__(self, obj_handler):
        """
        Constructor for our Object Event Handler. Creates our dictionary of events.
        :param obj_handler: The parent obj handler that the event handler will use to check if
                            objects are alive.
        """
        self.listeners = {}  # {event-type: [[source, callback, lifespan, *args],...]}
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

    def remove_listener(self, source):

        for event_key in self.listeners:
            spots = []
            counter = 0
            for listener in self.listeners[event_key]:
                if listener[0] == source:
                    spots.insert(0, counter)
                counter += 1

            for spot in spots:
                del self.listeners[event_key][spot]

    def find_subscriber_by_event(self, event_key, source):
        """
        See if the source is a subscriber to an event.
        :param event_key: the key for the event, view the event docs for which key to use.
        :param source: The object that is the subscriber of the event.
        :return: bool return on if the source is a subscriber to the event
        """
        if event_key in self.listeners:
            for subscriber in self.listeners[event_key]:
                if subscriber[0] == source:
                    return True
        return False

    def event(self, event_key, *args):
        """
        Event Happens, let listeners know
        :param event_key: the key for the event, view the event docs for which key to use.
        :param args:
        :return:
        """

        expired_subscribers = []

        if event_key in self.listeners:
            counter = 0
            for subscriber in self.listeners[event_key]:
                subscriber[2] = subscriber[2] - 1
                if subscriber[0].dead:
                    expired_subscribers.insert(0, [counter, event_key])
                    continue
                if subscriber[2] == 0:
                    expired_subscribers.insert(0, [counter, event_key])
                if len(subscriber[3]) > 0:
                    # if the subscriber had arguments they wanted passed when the event fired we pass those too
                    subscriber[1](*args, *subscriber[3])
                else:
                    # otherwise we just pass the expected parameters
                    subscriber[1](*args)
                counter += 1

        for expired_subscriber in expired_subscribers:
            print(self.listeners, expired_subscribers, expired_subscriber)
            del self.listeners[expired_subscriber[1]][expired_subscriber[0]]

