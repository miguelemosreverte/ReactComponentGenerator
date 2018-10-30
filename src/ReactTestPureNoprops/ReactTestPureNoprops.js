import React,{ PureComponent } from 'react';
import styles from './ReactTestPureNoprops.scss';
import classNames from 'classnames/bind';
const cx = classNames.bind(styles);

class ReactTestPureNoprops extends PureComponent {

    constructor(props) {
        super(props);
        this.state = { 
            
        };

    }

    componentDidMount(){

    }
    
    render() {

        return (
            <div className={cx('react-test-pure-noprops')}>

            </div>
        );
    }
}

export default ReactTestPureNoprops;
