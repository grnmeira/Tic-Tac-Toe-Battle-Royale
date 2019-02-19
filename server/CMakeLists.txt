cmake_minimum_required(VERSION 2.8)

project(server)

add_executable("unit-tests" "unit-tests.cpp")

target_link_libraries("unit-tests"
                      "gtest"
                      "pthread")
enable_testing()
add_test(UnitTests "unit-tests")

add_executable(${PROJECT_NAME} "main.cpp")
