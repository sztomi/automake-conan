from __future__ import print_function
from conans import ConanFile, CMake, tools
from glob import glob
from time import sleep

import os
import subprocess

class AutoMakeConan(ConanFile):
    name = 'automake'
    version = '1.15'
    license = 'MIT'
    url = 'https://github.com/sztomi/automake-conan'
    description = 'This is a tooling package for GNU automake'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake', 'virtualenv'
    requires = 'autoconf/2.69@sztomi/testing'

    def source(self):
        tarball_url = 'https://gnu.cu.be/automake/automake-{}.tar.gz'.format(self.version)
        tgz = tarball_url.split('/')[-1]
        tools.download(tarball_url, tgz)
        tools.untargz(tgz)
        os.unlink(tgz)


    def build(self):
        self.dirname = glob('automake-*')[0]
        os.chdir(self.dirname)    
        def run_in_env(cmd):
            activate = '. ../activate.sh &&'
            self.run(activate + cmd)    
        run_in_env('./configure --prefix={}'.format(self.package_folder))
        self.run('make')
        self.run('make install')

    def package(self):
        pass

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))
        
