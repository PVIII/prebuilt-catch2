cmake_minimum_required(VERSION 3.8)
project(prebuilt_catch2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_library(prebuilt_catch2 main.cpp)
target_link_libraries(prebuilt_catch2 PUBLIC CONAN_PKG::Catch2)
target_compile_features(prebuilt_catch2 PUBLIC cxx_std_11)

install(TARGETS prebuilt_catch2
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib)

add_subdirectory(test)

