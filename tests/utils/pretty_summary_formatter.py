from tests.utils.pretty_test_result import PrettyTestResult
from unittest.runner import _WritelnDecorator


class PrettySummaryFormatter:
    """
    Formatter class for printing a summary of test results in a clean and readable format.
    """
    
    def __init__(self, stream: _WritelnDecorator) -> None:
        """Initializes the PrettySummaryFormatter with the given output stream."""
        self.stream = stream
        
    def format(self, result: PrettyTestResult, start_time: float, end_time: float) -> None:
        """
        Prints a summary of test execution, including passed, failed, and errored tests,
        along with total test count and execution duration.

        Args:
            result (PrettyTestResult): The test result object containing execution data.
            start_time (float): Timestamp when test run started.
            end_time (float): Timestamp when test run ended.
        """
        total: int = result.testsRun
        failed: int = len(result.failures)
        errors: int = len(result.errors)
        passed: int = len(result.successes)
        duration: float = end_time - start_time
        
        self.stream.writeln("\n📊 SUMMARY")
        self.stream.writeln("───────────────")
        self.stream.writeln(f"✅ Passed  : {passed}")
        self.stream.writeln(f"❌ Failed  : {failed}")
        self.stream.writeln(f"⚠️  Errors  : {errors}")
        self.stream.writeln(f"📦 Total   : {total}")
        self.stream.writeln(f"⏱️ Duration: {duration:.4f} seconds")