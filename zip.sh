#!/bin/bash
rm function.zip
cd package
zip -r9 ../function.zip .
cd ..
zip -r -g function.zip social_modules
zip -g function.zip lambda_function.py
