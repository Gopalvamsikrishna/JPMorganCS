from collections import OrderedDict

class RolesCache:
    def __init__(self, capacity):
        """
        Initialize the cache with a maximum capacity (k). 
        Roles and their messages will be stored in an OrderedDict to maintain the insertion order.
        """
        self.capacity = capacity  # max number of active roles
        self.cache = OrderedDict()  # store roles and their messages

    def get(self, role):
        """
        Returns the message for the given role. 
        If the role exists in the cache, return the message.
        If the role doesn't exist, return None.
        """
        if role in self.cache:
            # Move the accessed role to the end to mark it as most recently used
            self.cache.move_to_end(role)
            return self.cache[role]
        return None

    def set(self, role, message):
        """
        Adds a new role with the corresponding message to the cache.
        If the role already exists, just update the message.
        If the cache exceeds its capacity, remove the oldest role.
        """
        if role in self.cache:
            # If role exists, update the message and mark it as recently used
            self.cache.move_to_end(role)
        self.cache[role] = message

        # If the cache exceeds the capacity, pop the oldest item (first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove the least recently used role

    def _complexity(self):
        """
        Returns the time and space complexities of the `get` and `set` methods.
        """
        return {
            'get': 'O(1)',  # Accessing an item in OrderedDict is O(1)
            'set': 'O(1)',  # Inserting/removing and updating OrderedDict is O(1)
            'space': 'O(k)'  # We store up to 'k' roles in the cache
        }

# Example Usage
if __name__ == "__main__":
    # Create a cache with a capacity of 3 roles
    cache = RolesCache(3)

    # Set some roles
    cache.set("admin", "Admin role used")
    cache.set("editor", "Editor role used")
    cache.set("viewer", "Viewer role used")

    # Get a role message
    print(cache.get("admin"))  # Should return: Admin role used

    # Add a new role, causing the oldest one (admin) to be removed
    cache.set("guest", "Guest role used")
    
    # Try to get the admin role which should now be evicted
    print(cache.get("admin"))  # Should return: None

    # Get the guest role
    print(cache.get("guest"))  # Should return: Guest role used
