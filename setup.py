from setuptools import setup, find_packages

setup(
    name='my_ansible_lookup_plugin',
    version='0.1.0',
    description='Custom Ansible lookup plugin for AWX',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Volodymyr Mazur',
    author_email='vmazur@ukrtelecom.ua',
    url='https://github.com/vmazurukrtelecom/my_ansible_lookup_plugin',
    packages=find_packages(),
    package_data={
        '': ['lookup_plugins/*.py'],  # Включаємо всі .py файли з lookup_plugins
    },
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
