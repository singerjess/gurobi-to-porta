cmake_minimum_required(VERSION 3.23)
project(porta_1_4_1 C)

set(CMAKE_C_STANDARD 11)

include_directories(src)

add_executable(porta_1_4_1
        src/arith.c
        src/arith.h
        src/common.c
        src/common.h
        src/four_mot.c
        src/four_mot.h
        src/inout.c
        src/inout.h
        src/largecalc.c
        src/largecalc.h
        src/log.c
        src/log.h
        src/mp.c
        src/mp.h
        src/porta.c
        src/porta.h
        src/portsort.c
        src/portsort.h
        src/valid.c
        src/valid.h)
