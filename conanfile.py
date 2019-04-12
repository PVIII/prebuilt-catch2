from conans import ConanFile, CMake, tools

class PrebuiltCatch2(ConanFile):
    name = "Catch2"
    version = "2.7.1"
    url = "https://github.com/catchorg/Catch2"
    license = "MIT"
    description = "Repackaging of Catch2 with a prebuilt main.cpp."
    settings = "os", "compiler", "arch", "build_type"
    requires = "Catch2/2.7.1@catchorg/stable"
    exports_sources = "**"
    generators = "cmake"
    build_policy = "missing"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
        self.copy("LICENSE.txt")
        self.copy("README.md")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

