from conans import ConanFile, CMake, tools
import os


class HALUnixConan(ConanFile):
    name = "HALUnix"
    version = "develop"
    license = "Apache License, Version 2.0. https://www.apache.org/licenses/LICENSE-2.0"
    url = "https://github.com/Dr-QP/HALUnix"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True", "Boost:shared=True"
    generators = "cmake"
    exports_sources = "*", "!build/*", "!test_package/*"
    requires = "HAL/develop@anton-matosov/dev", "Boost/1.64.0@anton-matosov/stable"
    # remotes = "https://api.bintray.com/conan/anton-matosov/general"

    def configure(self):
        self.options["Boost"].shared = self.options.shared


    def imports(self):
        self.copy("*.dll", "", "bin")
        self.copy("*.dylib", "", "lib")

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        install = '-DCMAKE_INSTALL_PREFIX="%s"' % self.package_folder
        self.run('cmake . %s %s %s' % (cmake.command_line, install, shared))
        self.run("cmake --build . %s" % cmake.build_config)  # --target install

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*HALUnix.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
        self.cpp_info.libs = ["HALUnix"]
