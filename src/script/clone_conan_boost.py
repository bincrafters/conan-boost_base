#!/usr/bin/env python3
"""
    Copyright (C) 2019 Rene Rivera.
    Use, modification and distribution are subject to the
    Boost Software License, Version 1.0. (See accompanying file
    LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""
import os.path
import sys
from pprint import pprint
from bls.util import PushDir
from foreach import ForEach


script_dir = os.path.dirname(os.path.realpath(__file__))


class CloneConanBoost(ForEach):
    '''
    Clones all the available Conan Boost packages.
    '''

    def __init_parser__(self, parser):
        super(CloneConanBoost, self).__init_parser__(parser)

    def groups_pre(self, groups):
        self.__check_call__(['git', 'init'])

    def package_do(self, package):
        super(CloneConanBoost, self).package_do(package)
        if package != 'base':
            self.__call__([
                'git', 'submodule', 'add',
                'https://github.com/bincrafters/conan-boost_%s.git' % (
                    package),
                package
            ])


if __name__ == "__main__":
    CloneConanBoost()
