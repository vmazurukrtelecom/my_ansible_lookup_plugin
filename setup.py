from setuptools import setup, find_packages

setup(
    name='my_ansible_lookup_plugin',
    version='0.1.0',
    description='Custom Ansible lookup plugin for AWX',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_ansible_lookup_plugin',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Додайте залежності, якщо є (наприклад, з requirements.txt)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
