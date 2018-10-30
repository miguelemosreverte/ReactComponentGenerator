#!/bin/bash

componentName=$1
path=$2

echo "export { default } from './$componentName'" > $path/$componentName/index.js