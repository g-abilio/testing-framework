from TestCase import TestCase
from TestResult import TestResult
from testing import TestCaseTest

class MyTest(TestCase): 
    def set_up(self): 
        print("set_up")

    def tear_down(self): 
        print("tear_down")

    def test_a(self): 
        print("test_a")

    def test_b(self): 
        print("test_b")

    def test_c(self): 
        print("test_c")

def MyTest_usage(): 
    result = TestResult()

    test = MyTest("test_a")
    test.run(result) 

    test = MyTest("test_b")
    test.run(result) 

    test = MyTest("test_c")
    test.run(result) 

    print(result.summary())

def TestCaseTest_usage(): 
    result = TestResult()

    test = TestCaseTest.TestCaseTest("test_result_success_run")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_result_failure_run")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_result_error_run")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_result_multiple_run")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_was_set_up")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_was_run")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_was_tear_down")
    test.run(result)

    test = TestCaseTest.TestCaseTest("test_template_method")
    test.run(result)

    print(result.summary())

TestCaseTest_usage()