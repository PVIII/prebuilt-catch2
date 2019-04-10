# contracts
[![Build Status](https://travis-ci.com/PVIII/catch2.svg?branch=master)](https://travis-ci.com/PVIII/catch2)

This is a prebuilt version of the header-only unit test library Catch2. The Catch2 main file takes very long to compile compared to the actual tests.

## Getting Started

Check the [Catch2](https://github.com/catchorg/Catch2) GitHub page for information about which compilers work.

### Installing

Add the Conan remote
```
conan remote add <REMOTE> https://api.bintray.com/conan/pviii/conan
```
and reference the package `prebuilt-catch2/x.x.x@pviii/stable` as a dependency.

## Built With

* [CMake](https://cmake.org/) - Build System (Generator)
* [Conan](https://conan.io/) - Dependency Management
* [Bintray](https://bintray.com) - Package Hosting

## Versioning

This package is versioned according to the parent project [Catch2](https://github.com/catchorg/Catch2).

## License

This project is licensed under the Boost Software License 1.0 - see the [LICENSE.txt](LICENSE.txt) file for details.

