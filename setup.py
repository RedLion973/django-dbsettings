from setuptools import setup, find_packages

# Dynamically calculate the version based on dbsettings.VERSION
version_tuple = (0, 1, 'alpha')
if version_tuple[2] is not None:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name = 'dbsettings',
    version = version,
    description = 'Db settings',
    author = 'RedLion973',
    author_email = 'red_lion-973@hotmail.fr',
    url = 'http://github.com/RedLion973/django-dbsettings',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers = ['Development Status :: 1 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
