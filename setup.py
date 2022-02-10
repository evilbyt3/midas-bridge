from setuptools import setup, find_packages

setup(
    name='midasB',
    version='0.1.0',
    author='vlaghe',
    author_email='vlaghe@protonmail.com',
    description='Unnoficial Midas API library for python',
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    url='https://github.com/vlagh3/midas-bridge',
    packages=find_packages()
    install_requires=['requests', 'json'],
    python_requires=">=3.6",
)
