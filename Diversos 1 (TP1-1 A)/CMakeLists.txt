cmake_minimum_required(VERSION 3.15)
project(TP1_A C)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_FLAGS ${CMAKE_C_FLAGS} "-Wall -Wextra -std=c90 -ansi -lm")
add_executable(TP1_A mainVFinal.c)
