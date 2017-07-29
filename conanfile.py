"""Conan.io recipe for CppRestSDK library
"""
from conans import ConanFile, tools, os


class BoostBeastConan(ConanFile):
    """Checkout CppRestSDK, build and create package
    """
    name = "Boost.Beast"
    version = "1.65.0"
    generators = "txt"
    url = "https://github.com/boostorg/process"
    description = "Boost.process is a cross-platform library for comfortable management of OS processes"
    license = "www.boost.org/users/license.html"
    folder_name = "boost_{0}".format(version.replace(".", "_"))
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git {2}"
                 .format(self.version, self.url, self.FOLDER_NAME))

    def package(self):
        release_dir = path.join(self.folder_name, "Release")
        self.copy("license.txt", dst=".", src=self.cpprestsdk_dir)
        self.copy(pattern="*.h", dst="include", src=path.join(release_dir, "include"))
        self.copy(pattern="*.hpp", dst="include", src=path.join(release_dir, "include"))


