from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from TestLoader import TestLoader
from TestRunner import TestRunner
from testing import TestCaseTest
from testing import TestSuiteTest
from testing import TestLoaderTest

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
    suite = TestSuite()

    suite.add_test(TestCaseTest.TestCaseTest("test_result_success_run"))
    suite.add_test(TestCaseTest.TestCaseTest("test_result_failure_run"))
    suite.add_test(TestCaseTest.TestCaseTest("test_result_error_run"))
    suite.add_test(TestCaseTest.TestCaseTest("test_result_multiple_run"))
    suite.add_test(TestCaseTest.TestCaseTest("test_was_set_up"))
    suite.add_test(TestCaseTest.TestCaseTest("test_was_run"))
    suite.add_test(TestCaseTest.TestCaseTest("test_was_tear_down"))
    suite.add_test(TestCaseTest.TestCaseTest("test_template_method"))

    suite.add_test(TestSuiteTest.TestSuiteTest("test_suite_size"))
    suite.add_test(TestSuiteTest.TestSuiteTest("test_suite_success_run"))
    suite.add_test(TestSuiteTest.TestSuiteTest("test_suite_multiple_run"))

    suite.run(result)
    print(result.summary())

def TestLoaderTest_usage(): 
    result = TestResult() 
    loader = TestLoader() 

    suite = loader.make_suite(TestLoaderTest.TestLoaderTest)
    suite.run(result)
    
    print(result.summary())

def TestRunner_usage(): 
    loader = TestLoader() 
    suite = loader.make_suite(TestLoaderTest.TestLoaderTest)
    
    runner = TestRunner() 
    runner.run(suite)

def main(): 
    loader = TestLoader() 
    test_case_suite = loader.make_suite(TestCaseTest.TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest.TestSuiteTest)
    test_loader_suite = loader.make_suite(TestLoaderTest.TestLoaderTest)

    suite = TestSuite() 
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_loader_suite)

    runner = TestRunner()
    runner.run(suite)

main()