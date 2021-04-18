# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.paths = {}

    def insert(self, path):
        # Insert the node as before
        self.paths[path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path_item in path:
            if path_item not in node.paths:
                node.insert(path_item)
            node = node.paths[path_item]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path_item in path:
            if path_item == "":
                continue
            # print("D", path_item, node.paths)
            node = node.paths.get(path_item, None)
            if node is None:
                return None
            # print("D", path_item, node.paths, node.handler)
        return node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, string_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(string_path)
        self.route_trie.insert(path, handler)

    def lookup(self, string_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(string_path)
        handler = self.route_trie.find(path)
        return handler if handler else self.not_found_handler


    def split_path(self, string_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        temp = string_path.split("/")
        path = []
        for item in temp:
            if item == "":
                continue
            path.append(item)
        return path


# Test class
class Test:
    def __init__(self):
        global root_handler, about_handler, not_found_handler
        # create the router and add a route
        self.router = Router(root_handler, not_found_handler)
        self.router.add_handler("/home/about", about_handler)  # add a route

    def test_function(self, test_number, path, expected_handler, test_subject):
        if self.router.lookup(path) == expected_handler:
            result = "Pass"
        else:
            result = "Fail"
        print("{} - {} - {}".format(test_number, result, test_subject))


root_handler = "root handler"
about_handler = "about handler"
not_found_handler = "not found handler"

test = Test()
# Test 1 - empty path
test.test_function(1, "", root_handler, "empty path")

# Test 2 - "/" path
test.test_function(2, "/", root_handler, '"/" path')

# Test 3 - middle path
test.test_function(3, "/home", not_found_handler, "existing path - no handler")

# Test 4 - existing handler - no trailing slash
test.test_function(4, "/home/about", about_handler, "existing path - with handler - no trailing slash")

# Test 5 - existing handler - with trailing slas
test.test_function(5, "/home/about/", about_handler, "existing path - with handler - with trailing slash")

# Test 6 - extending non-existent route
test.test_function(6, "/home/about/me", not_found_handler, "extending non-existent path")

# Test 7 - non-existent route
test.test_function(7, "/me/", not_found_handler, "non-existent route")