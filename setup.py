from distutils.core import setup
setup(
  name = 'real_time_flights_api',
  packages = ['real_time_flights_api'],
  version = '1.0',
  license='MIT',
  description = 'A Python package to get real time flights information from the FlightLabs API. Website https://www.goflightlabs.com/',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Zyla Labs',
  author_email = 'hello@zylalabs.com',
  url = 'https://github.com/secrojas/Zyla-Real-Time-Flights-API',
  download_url = 'https://github.com/secrojas/Zyla-Real-Time-Flights-API/archive/refs/tags/v.1.tar.gz',
  keywords = ['flights','real time flights','scraping', 'easy', 'scraper', 'website', 'download', 'links', 'images', 'videos'],
  install_requires=[
          'requests',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.11',
  ],
)