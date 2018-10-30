#!/bin/bash

componentName=$1
className=$2
props=$3
proptypes=$4
path=$5

echo "import React,{ PureComponent } from 'react';
import styles from './$componentName.scss';
import classNames from 'classnames/bind';" >> $path/$componentName/$componentName.js

if [ ! -z "$props" ]
then
    echo "import PropTypes from 'prop-types';" >> $path/$componentName/$componentName.js
fi


echo "const cx = classNames.bind(styles);

class $componentName extends PureComponent {

    constructor(props) {
        super(props);
        this.state = { 
            
        };

    }

    componentDidMount(){

    }
    
    render() {" >> $path/$componentName/$componentName.js
if [ ! -z "$props" ]
then
    echo "      const {$props} = this.props;" >> $path/$componentName/$componentName.js
fi   
        
 echo "
        return (
            <div className={cx('$className')}>

            </div>
        );
    }
}
" >> $path/$componentName/$componentName.js

if [ ! -z "$props" ]
then
    echo "$proptypes" >> $path/$componentName/$componentName.js
fi

echo "
export default $componentName;" >> $path/$componentName/$componentName.js