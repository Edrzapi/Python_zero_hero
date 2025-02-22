import unittest


class TestUser(unittest.TestCase):
    """
    This is the test class for the User class. Each method in this class is a unit test
    designed to validate a specific behavior or feature of the User class.
    """

    @classmethod
    def suite(cls):
        """
        A class method that creates a test suite for the TestUser class.
        This method allows us to group all tests related to the User class into a single suite,
        which can be executed as a whole.

        Why Use a Test Suite?
        Test suites are useful for organizing related tests. Instead of running individual tests
        one by one, you can bundle them together into a suite and run them all at once. This is especially
        helpful when working with large projects, as it allows you to run tests for specific functionality or
        modules in a structured and efficient manner.

        By keeping the suite method separate from the individual test methods:
        1. You can control how tests are grouped and run.
        2. You make the testing process more flexible, allowing easy addition of new test classes in the future.

        Steps:
        1. Create a `TestSuite` instance.
        2. Add the `TestUser` test class to the suite using `addTest` and `makeSuite`.
        3. Return the suite for execution.
        """
        suite = unittest.TestSuite()  # Initialize the suite
        print("Adding TestUser to the suite...")  # Print a message to track the process
        suite.addTest(unittest.makeSuite(TestUser))  # Add all tests from the TestUser class to the suite
        return suite  # Return the suite to be run


# This is where the test suite will be executed when the script runs.
# If this file is executed directly, all the tests will run through the suite.
if __name__ == "__main__":
    """
    This block checks if the script is being run directly (rather than being imported as a module).
    If it is, the suite() method will be called to execute the test suite.
    The test runner will handle running the test cases in the suite, producing output for each test.
    """
    unittest.TextTestRunner().run(TestUser.suite())  # Run the test suite using TextTestRunner.
