from conans import ConanFile, CMake, tools
import os


class HALUnixConan(ConanFile):
    name = "HALUnix"
    version = "develop"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        install = '-DCMAKE_INSTALL_PREFIX="%s"' % self.package_folder
        self.run('cmake %s %s %s %s' % (self.conanfile_directory,
                                     cmake.command_line, install, shared))
        self.run("cmake --build . --target install %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="HALUnix")
        self.copy("*HALUnix.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["HALUnix"]
