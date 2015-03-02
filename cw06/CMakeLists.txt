cmake_minimum_required(VERSION 2.8)
include(GenerateExportHeader)

add_library(b SHARED b.c)
set_property(TARGET b APPEND PROPERTY COMPILE_DEFINITIONS B_BUILD)

generate_export_header(b EXPORT_MACRO_NAME B_BUILD)

add_executable(hello a.c)
target_link_libraries(hello b)
