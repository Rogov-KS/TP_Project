#!/bin/bash
mkdir build
cd build
cmake ..
make
cp MAIN/The_age_of_conquest ../
cd ..
rm -r build
./The_age_of_conquest
rm The_age_of_conquest
