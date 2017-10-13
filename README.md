## This repository holds a conan recipe for Boost.Beast.

[Conan.io](https://conan.io) package for [Boost.Beast](https://github.com/Boostorg/Beast) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/Boost.Beast%3Abincrafters).

## For Users: Use this package

### Prerelease Status

At this time, this library is not released by the author under Boost. It is currently still under development and expected to be included in Boost 1.66.0.  Until then, this package will be built from a `git clone` of the master branch periodically and will use a datestamp as the version number.  When the library is officially released under github releases, this package will recieve proper stable and testing channels with semantic versioning.

### Basic setup

    $ conan install Boost.Beast/20171013@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Beast/20171013@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create bincrafters/stable
	
## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload Boost.Beast/20171013@bincrafters/stable --all -r bincrafters

### License
[Boost](www.boost.org/LICENSE_1_0.txt)
