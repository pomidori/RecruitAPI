from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='RecruitAPI',
      version='0.0.1',
      description='extract data from recruit open API',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords=['API', 'open data', 'restaurant', 'csv'],
      # url='http://github.com/',
      author='Midori Kato',
      author_email='pomidori724@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires={
          'pandas=0.23.4'
          'requests=2.19.1'
          'pyhdb=0.3.4'
      }
      )
