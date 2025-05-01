from unittest import TestCase, TextTestResult


class PrettyTestResult(TextTestResult):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.successes: list[TestCase] = []
    
    def addSuccess(self, test: TestCase) -> None:
        super().addSuccess(test)
        self.successes.append(test)
        self.stream.writeln(f"✅ {test.__class__.__name__:<20} - {test._testMethodName:<50} - {test.shortDescription()}")
    
    def addFailure(self, test: TestCase, err) -> None:
        super().addFailure(test, err)
        self.stream.writeln(f"❌ {test.__class__.__name__:<20} - {test._testMethodName:<50} - {test.shortDescription()}")

    def addError(self, test: TestCase, err) -> None:
        super().addError(test, err)
        self.stream.writeln(f"⚠️ {test.__class__.__name__:<20} - {test._testMethodName:<50} - {test.shortDescription()}")