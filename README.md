## Package Status

| Bintray | Windows | Linux & Mac | 
|:--------:|:---------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/bincrafters/public-conan/boost_base%3Abincrafters/images/download.svg)](https://bintray.com/bincrafters/public-conan/boost_base%3Abincrafters/_latestVersion)|[![Build status](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-boost_base?svg=true)](https://ci.appveyor.com/project/bincrafters/conan-boost-base)|NA|

## Conan.io Information

Bincrafters packages can be found in the following public Conan repository:

[Bincrafters Public Conan Repository on Bintray](https://bintray.com/bincrafters/public-conan)

*Note: You can click the "Set Me Up" button on the Bintray page above for instructions on using packages from this repository.*

## Issues

If you wish to report an issue or make a request for a Bincrafters package, please do so here:  

[Bincrafters Community Issues](https://github.com/bincrafters/community/issues)

## General Information

This GIT repository is managed by the Bincrafters team and holds files related to Conan.io.  For detailed information about Bincrafters and Conan.io, please visit the following resources: 

[Bincrafters Wiki - Common README](https://github.com/bincrafters/community/wiki/Common-README.md)

[Bincrafters Technical Documentation](http://bincrafters.readthedocs.io/en/latest/)

[Bincrafters Blog](https://bincrafters.github.io)

## License Information

The license for all files contained in this GIT repository are defined in the [LICENSE.md](LICENSE.md) file in this repository.  The licenses included with all Conan packages published by Bincrafters can be found in the Conan package directories in the following locations, relative to the Conan Cache root (`~/.conan` by default): 

### License(s) for packaged software: 

    ~/.conan/data/<pkg_name>/<pkg_version>/bincrafters/package/<random_package_id>/license/<LICENSE_FILES_HERE>

*Note :   The most common filenames for OSS licenses are `LICENSE` AND `COPYING` without file extensions.*
	
### License for Bincrafters recipe: 

    ~/.conan/data/<pkg_name>/<pkg_version>/bincrafters/export/LICENSE.md 

## Boost Modular Packages

This is the base class, as a python requires package, for the Boost modular packages. It contains almost all the packaging logic for all supported versions of Boost.

### Contents

* `src/data` -- Contains the generated information for the Boost packages as
    JSON data for each version.
* `script` -- Contains generation and build scripts for creating and
    maintaining the packages as one development unit.
    * `package_data_gen.py` -- Generates the
        `package-data-boost-<version>.json` data.
    * `create_all.py` -- Invokes `conan create ...` for each package in
        dependency order.
    * `clone_conan_boost.py` -- Git clones the needed for a given version.

### Release

Generating the packages for a modular Boost release is complex. But hopefully
the scripts here make it as simple as possible. But be warned; this is a
continuing work in progress.

#### Base Package

First step is to clone this package locally. It contains scripts to automate
the Boost libraries data and other utilities to deal with the numerous,
and growing, Boost modular packages.

```
git clone https://github.com/bincrafters/conan-boost_base
cd conan-boost_base
```

#### Release Data

Next we need to generate the package data that specifies the setup and
dependencies for the particular Boost release. For that we need to a few
source pieces and scripts. Before we proceed with this there are two
dependencies we need to account for:

1. Python 3
2. Boost Library Statistics, aka `bls`, utility Python package.

All the scripts here and in `bls` use Python version 3. Hence you will
need to install that to continue. The `bls` package can be installed
directly from the GitHub repo with `pip`:

```
pip3 install --upgrade https://github.com/grafikrobot/boost_lib_stats/archive/master.zip
```

We can now use the `package_data_gen.py` script to do all the heavy work needed
to obtain Boost libraries and to inspect them to generate the package
dependency information.

```
./src/script/package_data_gen.py ++version=1.70.0
```
