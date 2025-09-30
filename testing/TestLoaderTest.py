from src import TestCase 
from .TestCaseTest import TestStub, TestSpy
from src import TestLoader
from src import TestSuite

class TestLoaderTest(TestCase.TestCase):

    def test_create_suite(self): 
        loader = TestLoader.TestLoader() 
        suite = loader.make_suite(TestStub)
        assert len(suite.tests) == 3

    def test_create_suite_of_suites(self): 
        loader = TestLoader.TestLoader() 
        stub_suite = loader.make_suite(TestStub)
        spy_suite = loader.make_suite(TestSpy)

        suite = TestSuite.TestSuite() 
        suite.add_test(stub_suite)
        suite.add_test(spy_suite)

        assert len(suite.tests) == 2

    def test_get_multiple_test_case_names(self): 
        loader = TestLoader.TestLoader() 
        names = loader.get_test_case_names(TestStub)

        assert names == ["test_error", "test_failure", "test_success"]

    def test_get_no_test_case_names(self): 
         
        class Test(TestCase.TestCase): 
            def foobar(self): 
                pass 

        loader = TestLoader.TestLoader()
        names = loader.get_test_case_names(Test)

        assert names == []
