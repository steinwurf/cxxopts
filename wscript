#! /usr/bin/env python
# encoding: utf-8

import os

APPNAME = 'cxxopts'
VERSION = '1.1.0'


def build(bld):

    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_CXXOPTS_VERSION="{}"'.format(VERSION))

    # Path to the source repo
    sources = bld.dependency_node("cxxopts-source")
    includes = sources.find_dir('include')

    bld(name='cxxopts_includes',
        export_includes=[includes])

    if bld.is_toplevel():

        # The actual sources are stored outside this repo - so we manually
        # add them for the solution generator
        bld.msvs_extend_sources = [sources]

        # Only build tests when executed from the top-level wscript,
        # i.e. not when included as a dependency
        bld.program(
            features='cxx test',
            source=sources.ant_glob('test/*.cpp', excl=['**/link_*.cpp']),
            target='cxxopts_tests',
            use=['cxxopts_includes'])
