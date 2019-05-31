=======
cxxopts
=======

This repository contains waf build scripts for https://github.com/jarro2783/cxxopts
that are necessary for integration with other Steinwurf libraries.

.. contents:: Table of Contents:
   :local:

Quick Start
-----------

If you already installed a C++14 compiler, git and python on your system,
then you can clone this repository to a suitable folder::

    git clone git@github.com:steinwurf/cxxopts.git

Configure and build the project::

    cd cxxopts
    python waf configure
    python waf build

Run the unit tests::

    python waf --run_tests
