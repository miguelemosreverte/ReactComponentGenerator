#!/bin/bash

componentName=$1
className=$2
path=$3

echo ".$className {
    
}" > $path/$componentName/$componentName.sccs

