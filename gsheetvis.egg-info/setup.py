from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'Programming Language :: Python :: 3'
]
setup(
  name='gsheetvis',
  version='0.0.3',
  description='A Visualizing program which can visualize you data from google sheets ',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rahul Rathore',
  author_email='rathodrahul873@gmail.com',
  license='NA', 
  classifiers=classifiers,
  keywords='GSHEET VISUALIZER', 
  packages=find_packages(),
  install_requires=[['gsheets==0.5.1'],['pandas==1.1.3'],['matplotlib==3.3.2'] ],
  python_requires='>=3.6'
)