from conans import ConanFile, CMake, tools

class PrebuiltCatch2(ConanFile):
    name = "prebuilt-catch2"
    version = "2.13.0"
    url = "https://github.com/catchorg/Catch2"
    license = "BSL-1.0"
    description = "Repackaging of Catch2 with a prebuilt main.cpp."
    settings = "os", "compiler", "arch", "build_type"
    requires = "Catch2/2.13.0@catchorg/stable"
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

