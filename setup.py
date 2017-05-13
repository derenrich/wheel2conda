from setuptools import setup, find_packages

version = open('git_version','r').read()

setup(name='wheel2conda',
      version=version+'+palantir',
      description='Python Distribution Utilities',
      author='Thomas Kluyver',
      author_email='thomas@kluyver.me.uk',
      url='https://www.github.com/takluyver/wheel2conda',
      packages=['wheel2conda'],
      entry_points={
          'console_scripts' : ['wheel2conda=wheel2conda:main']
      }      
     )

