from unittest import TestCase, TextTestResult


class PrettyTestResult(TextTestResult):
    """
    Custom test result class that extends TextTestResult to include:
    - A list of successful test cases.
    - Pretty-printed output with icons and aligned formatting for success, failure, and error cases.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Initializes the PrettyTestResult object and sets up a list to store successful test cases."""
        super().__init__(*args, **kwargs)
        self.successes: list[TestCase] = []
    
    def addSuccess(self, test: TestCase) -> None:
        """Records a successful test and prints a formatted success message to the output stream."""
        super().addSuccess(test)
        self.successes.append(test)
        self.stream.writeln(f"✅ {test.__class__.__name__:<20} - {test._testMethodName:<50} - {test.shortDescription()}")
    
    def addFailure(self, test: TestCase, err) -> None:
        """Records a failed test and prints a formatted failure message to the output stream."""
        super().addFailure(test, err)
        self.stream.writeln(f"❌ {test.__class__.__name__:<20} - {test._testMethodName:<50} - {test.shortDescription()}")

    def addError(self, test: TestCase, err) -> None:
        """Records a test that caused an error and prints a formatted error message to the output stream."""
        super().addError(test, err)
        self.stream.writeln(f"⚠️ {test.__class__.__name__:<20} - {test._testMethodName:<50} - {test.shortDescription()}")