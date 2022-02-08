Write a definition for a class named Kangaroo with the following methods:

An __init__ method that initializes an attribute named pouch_contents to an empty list.
A method named put_in_pouch that takes an object of any type and adds it to pouch_contents
A __str__ that returns a string representation of the Kangaroo object and the contents of the pouch.
# exercises/17.2.py

class Kangaroo:
    def __init__(self, contents=list()):
        self.pouch_contents = contents

    def put_in_pouch(self, obj):
        """appends given obj to pouch_contents"""
        self.pouch_contents.append(obj)

    def __str__(self):
        s = "Kangaroo - pouch contents:"
        for obj in self.pouch_contents:
            s += object.__str__(obj)
        return s
    
Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo, and then adding roo to the contents of kanga's pouch.

if __name__ == "__main__":
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)
Download [file], it contains a solution to the previous problem with one big, nasty bug. Find and fix the bug.

Default values for __init__ methods get evaluated when the function is defined, not on each instantiation. Because of this, both kangaroos reference the same list for their pouch contents.

To fix this, set the default value for pouch_contents to None; Within the function itself, create a list if needed.

 class Kangaroo:
-    def __init__(self, contents=list()):
+    def __init__(self, contents=None):
+		 if contents == None:
+			 contents = list()
		 self.pouch_contents = contents
