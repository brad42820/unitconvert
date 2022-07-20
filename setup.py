try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='unitconvert',
      version='0.1',
      description='Convert between units for MD simulations',
      author='Dr Bradley Treece',
      author_email='btreece@mercyhurst.edu',
      url = "https://github.com/brad42820/unitconvert.git",
      license='MIT',
      packages=['unitconvert',
                'unitconvert.acceleration',
                'unitconvert.area',
                'unitconvert.constants',
                'unitconvert.dictionaries',
                'unitconvert.energy',
                'unitconvert.force',
                'unitconvert.length',
                'unitconvert.mass',
                'unitconvert.pressure',
                'unitconvert.speed',
                'unitconvert.time',
                'unitconvert.volume'],
      install_requires=[
          'numpy'
          ],
      zip_safe=False,
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Other Audience",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ]
)