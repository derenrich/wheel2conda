from setuptools import setup, find_packages

setup(name='wheel2conda',
      version='0.1.palantir',
      description='Python Distribution Utilities',
      author='Thomas Kluyver',
      author_email='thomas@kluyver.me.uk',
      url='https://www.github.com/takluyver/wheel2conda',
      packages=['wheel2conda'],
      entry_points={
          'console_scripts' : ['wheel2conda=wheel2conda:main']
      },
      install_requires = ['win_cli_launchers']
      
     )

