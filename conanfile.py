#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostBeastConan(base.BoostBaseConan):
    name = "boost_beast"
    url = "https://github.com/bincrafters/conan-boost_beast"
    lib_short_names = ["beast"]
    header_only_libs = ["beast"]
    b2_requires = [
        "boost_align",
        "boost_asio",
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_endian",
        "boost_intrusive",
        "boost_optional",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_system",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility",
        "boost_winapi"
    ]
