cmake_minimum_required (VERSION 2.8.8)
project (QT_APPLICATION)

set(USE_QT 5)

set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable (app main.cpp mainwindow.cpp)
set(HEADERS mainwindow.h)

find_package(Qt5Widgets REQUIRED)
target_link_libraries(app Qt5::Widgets)

install(TARGETS app DESTINATION bin)
