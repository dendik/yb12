cmake_minimum_required(VERSION 2.8)

find_package(PythonLibs 2 REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

python_add_module(hello hello.c++)
target_link_libraries(hello ${PYTHON_LIBRARIES})
