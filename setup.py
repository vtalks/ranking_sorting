from setuptools import setup, find_packages

with open('README.md') as readme_file:
    long_description = readme_file.read()

with open('VERSION') as version_file:
    version = version_file.read()

setup(
    name='ranking_sorting',
    version=version,
    description='Ranking and Sorting algorithms for vtalks.net',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Raül Pérez',
    author_email='hellol@vtalks.net',
    url='https://github.com/vtalks/ranking_sorting',
    packages=find_packages(),
    install_requires=[
    ],
    license='Apache 2',
    test_suite='tests',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
