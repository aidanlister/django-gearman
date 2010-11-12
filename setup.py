from setuptools import setup, find_packages


setup(
    name='django-gearman',
    version='0.3',
    description='A convenience wrapper for Gearman clients and workers '
                'in Django/Python',
    long_description=open('README.md').read(),
    author='Frederic Wenzel',
    author_email='fwenzel@mozilla.com',
    url='http://github.com/aidanlister/django-gearman',
    license='MPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['gearman==2.0.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
