import xml.etree.ElementTree as ET
from ...models.test_artifacts import TestSuites, TestCase, TestSuite, Failure, TestError

def parse(filepath):
    """ returns a list of testsuites from the file """
    xml = ET.parse(filepath)
    root = xml.getroot()  # May be a testsuite or a testsuites

    testsuites = make_testsuites(root)
    return testsuites


def make_testsuites(root_xml):

    if root_xml.tag == 'testsuites':

        name = root_xml.get('name')
        tests = int(root_xml.get('tests'))
        failures = int(root_xml.get('failures'))
        errors = int(root_xml.get('errors'), 0)
        skipped = int(root_xml.get('skipped'), 0)

        testsuites = TestSuites(name, tests, failures, errors=errors, skipped=skipped)

        for testsuite in root_xml:
            ts = parse_testsuite(testsuite)
            testsuites.add_testsuite(ts)

    elif root_xml.tag == 'testsuite':

        testsuites = TestSuites()

        ts = parse_testsuite(root_xml)
        testsuites.add_testsuite(ts)

    else:
        raise JUnitParseException(f'The root element of the file {filepath} is expected to be either "testsuite" or "testsuites"')

    return testsuites



def parse_testsuite(xml_testsuite):
    """ Extract testcases """
    name = xml_testsuite.get('name')
    tests = int(xml_testsuite.get('tests', 0))
    failures = int(xml_testsuite.get('failures'))
    errors = int(xml_testsuite.get('errors', 0))
    skipped = int(xml_testsuite.get('skipped', 0))
    filename = xml_testsuite.get('file', None)

    testsuite = TestSuite(name, tests, failures, errors=errors, skipped=skipped, filename=filename)

    print(testsuite)

    for testcase in xml_testsuite:
        if testcase.tag == 'testcase':
            tc = make_testcase(testcase)
            testsuite.add_testcase(tc)

    return testsuite


def make_testcase(xml_testcase):
    name = xml_testcase.get('name')
    classname = xml_testcase.get('classname')
    xml_failure = xml_testcase.find('failure')
    failure = make_failure(xml_failure)

    xml_error = xml_testcase.find('error')
    error = make_error(xml_error)


    testcase = TestCase(name, classname, failure, error)
    return testcase


def make_failure(xml_failure):
    if xml_failure is None:
        return None
    message = xml_failure.get('message')
    text = xml_failure.text
    return Failure(message, text)


def make_error(xml_error):
    if xml_error is None:
        return None
    message = xml_error.get('message')
    text = xml_error.text
    return TestError(message, text)




def parsedir(dirpath):
    # parse all the files found, treat each as a testsuite
    pass
