from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='HW 7 Clean folder',
    author='Maryna Zipova',
    author_email='maryna.zipova@i.ua',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': 
    ['clean_folder=clean_folder.main:start']}
)