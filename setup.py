from setuptools import setup, find_packages

# Generate distribution archives
#   python3 -m pip install --upgrade build
#   python3 -m build
# Upload to pypi: 
#   python3 -m pip install --upgrade twine
#   python3 -m twine upload --config-file .pypirc -r testpypi dist/*



setup(
    name='midasB',
    version='0.0.1',
    author='vlaghe',
    author_email='vlaghe@protonmail.com',
    description='Unnoficial Midas API library for python',
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    url='https://github.com/vlagh3/midas-bridge',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires=">=3.6",
)
