cmake_minimum_required(VERSION 3.5)

set(PROJECT_NAME HALUnix)
project(${PROJECT_NAME})

if(NOT EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    # message(ERROR "The file conanbuildinfo.cmake doesn't exist.\nPlease run 'conan install' first")
    execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}" WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE ALL_CODE_HDRS ${CMAKE_CURRENT_SOURCE_DIR}/*.h)
file(GLOB_RECURSE ALL_CODE_SRCS ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

add_library(${PROJECT_NAME} ${ALL_CODE_HDRS} ${ALL_CODE_SRCS} ${SOURCE_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)

find_package(Boost 1.63 REQUIRED thread system)
target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
