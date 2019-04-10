cmake_minimum_required(VERSION 3.8)

add_executable(prebuilt_catch2_test
               test.cpp)
target_link_libraries(prebuilt_catch2_test PUBLIC prebuilt_catch2)

add_test(NAME test COMMAND prebuilt_catch2_test)

