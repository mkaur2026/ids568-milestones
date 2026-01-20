[![Python CI](https://github.com/mkaur2026/ids568-milestones/actions/workflows/ci.yml/badge.svg)](https://github.com/mkaur2026/ids568-milestones/actions/workflows/ci.yml)

# ids568-milestone  0


# Setup Instructions

1. In terminal (macOS)  make sure you have; 
   -Python 3.9 or higher
   -Git

2. Clone the repository
   git clone [GITHUB LINK]
   cd [repository title]

3. Create & activate  virtual environment
   python3 -m venv venv
   source venv/bin/activate

4. Instal dependencies
   pip install numpy==1.24.3 pandas==2.1.0 pytest==7.3.1
   pip freeze  >  requirements.txt

5. Create test file + run smoke test
   mkdir tests
   touch tests/test_imports.py

      import numpy
      import pandas
      
      def test_imports():
          assert numpy.__version__== "1.24.3"
          assert pandas.__version__== "2.1.0"
   
   pytest -v     #runs the smoke test locally/you should see a PASSED output#

5. Set up GitHub Actions CI
   mkdir github/workflows
   touch github/workflows/ci.yml
   insert workflow code into file

   #push to GitHub
   git add github/workflows/ci.yml
   git commit -m "title"
   git push origin main
   
   #check in GitHub repository in the actions tab for a green checkmark next to workflow

6. Add CI badge
   In GitHub repository go to actions tab then workflow and click 'create status badge'
   copy and paste that link into your README
   push to GitHub and wait for green checkmark to show it works




## Documentation

1. Environment reproducibility is critical and supports ML lifecycle reliability by using a python virtual environment and pinning the versions in 'requirements.txt', which ensures anyone who clones the repository can recreate the same results and environment without having issues due to different software versions. This eliminates common issues and ensures the same code is consistent during the whole data preparation and training process. 

2. The key reproducibility principles that were applied in my setup were dependency pinning, clear project structure, virtual environment, and a smoke test using pytest. The GitHub workflow runs in a great environment for each push, that verifies that all of the dependencies are correctly installed and working in the library.

3. Environment management supports deployment success by making sure the code runs without any errors due to differences and makes sure they match, it also makes deployment faster and more predictable by catching problems early and running without any missing errors.








































