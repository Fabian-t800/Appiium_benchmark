# Appium_benchmark
### Introduction:
This repo was created with the purpose of benchmarking Appium with winappdriver.exe The runner that's being used is Robotframework.
#### Technology stack used:
- <a href="https://www.python.org/downloads/release/python-376/">Python 3.7.4</a>
- <a href="https://github.com/robotframework/robotframework#id8">Robot Framework v3.1.2 </a>
- <a href="https://github.com/microsoft/WinAppDriver/releases/tag/v1.1.1">Winappdriver 1.1.1 </a>

#### Files in this repo:
- appium_tests
  - HelperClass.py
- proj_lib
  - BaseLayer.py
  - Element.py
  - SetupTeardown.py
- rf_appium_tests
  - Calculator_Tests.robot
  - helper_kw.robot
  - keywords.robot
- argfile_appium.txt
- requirements.txt

#### System settings and particularities:
- Operating system: Windows 10 Pro with Developer Mode turned on
- winappdriver.exe was added to the system variables

#### Dependencies and libraries:
- To install all used libraries, please run -r requirements.txt in from the command line

### Notes:
- All tests suites will only run if winappdriver.exe is active at runtime
- This is of course already in the Suite Setup, however it is not functioning properly, so currently if the tests need to be run, winappdriver.exe needs to be manually run.
