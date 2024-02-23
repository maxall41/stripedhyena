from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().split('\n')

setup(
    name='stripedhyena',
    version='0.2.0',
    description='StripedHyena',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='together.ai',
    url='http://github.com/togethercomputer/stripedhyena',
    license='Apache-2.0',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)