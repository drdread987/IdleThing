
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

    def event_friendly_unit_takes_damage(self, source, target, amount, dmg_type, spell_id):
        """
        Event ID 0, Happens when a friendly unit takes damage.
        :param source: Source of the damage
        :param target: The unit that took the damage
        :param amount: The amount of damage taken
        :param dmg_type: the type of damage dealt
        :param spell_id: the spell ID that created the damage
        :return: None
        """
        # TODO
        pass
