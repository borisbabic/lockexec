from distutils.core import setup

setup(
    name='LockExec',
    version='0.1.0',
    author='Boris Babic',
    author_email='boris.ivan.babic@gmail.com',
    packages=['lockexec'],
    py_modules=['lockexec'],
    include_package_data=True,
    url='template url',
    entry_points={
            'console_scripts': [
                #'lockexec = lockexec/__main__:main',
                'lockexec = lockexec:main',
            ],
        },
    description='do stuff on screen lock/unlock',
    long_description=open('README.txt').read(),
)
