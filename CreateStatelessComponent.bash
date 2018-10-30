#!/bin/bash

componentName=$1
className=$2
props=$3
proptypes=$4
path=$5

echo "proptypes $proptypes"
echo "props $props"

echo "import React from 'react';
import styles from './$componentName.sccs';
import classNames from 'classnames/bind';" >> $path/$componentName/$componentName.js
if [ ! -z "$props" ]
then
    echo "import PropTypes from 'prop-types';" >> $path/$componentName/$componentName.js
fi
echo "const cx = classNames.bind(styles);" >> $path/$componentName/$componentName.js

if [ ! -z "$props" ]
    then
        echo "const $componentName = ({$props}) => " >> $path/$componentName/$componentName.js
    else
        echo "const $componentName = () => " >> $path/$componentName/$componentName.js
fi
echo "    (
        <div className={cx('$className')}>

        </div>
    );
" >> $path/$componentName/$componentName.js

if [ ! -z "$props" ]
then
    echo "$proptypes" >> $path/$componentName/$componentName.js
fi

echo "export default $componentName;" >> $path/$componentName/$componentName.js