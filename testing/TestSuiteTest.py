from .TestCaseTest import TestStub
from src import TestSuite
from src import TestCase
from src import TestResult

class TestSuiteTest(TestCase.TestCase): 
    
    def test_suite_size(self): 
        suite = TestSuite.TestSuite() 

        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))

        assert len(suite.tests) == 3

    def test_suite_success_run(self): 
        result = TestResult.TestResult()
        suite = TestSuite.TestSuite() 

        suite.add_test(TestStub("test_success"))

        suite.run(result)

        assert result.summary() == "1 run, 0 failed, 0 error"

    def test_suite_multiple_run(self): 
        result = TestResult.TestResult() 
        suite = TestSuite.TestSuite() 

        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))

        suite.run(result) 

        assert result.summary() == "3 run, 1 failed, 1 error"


