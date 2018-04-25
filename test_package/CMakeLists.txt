project(test_package CXX)
cmake_minimum_required(VERSION 3.1.2)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(MPI)

file(GLOB SOURCE_FILES *.cpp)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} 
  CONAN_PKG::boost_asio
  CONAN_PKG::boost_assert
  CONAN_PKG::boost_beast
  CONAN_PKG::boost_bind
  CONAN_PKG::boost_config
  CONAN_PKG::boost_container
  CONAN_PKG::boost_core
  CONAN_PKG::boost_endian
  CONAN_PKG::boost_intrusive
  CONAN_PKG::boost_optional
  CONAN_PKG::boost_smart_ptr
  CONAN_PKG::boost_static_assert
  CONAN_PKG::boost_system
  CONAN_PKG::boost_throw_exception
  CONAN_PKG::boost_type_traits
  CONAN_PKG::boost_utility
  CONAN_PKG::boost_winapi)
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 11)

if(MPI_CXX_FOUND)
  target_link_libraries(${CMAKE_PROJECT_NAME} CONAN_PKG::openmpi)
endif(MPI_CXX_FOUND)
