import React,{ Component } from 'react';
import styles from './ReactTestClassNoprops.scss';
import classNames from 'classnames/bind';
const cx = classNames.bind(styles);

class ReactTestClassNoprops extends Component {

    constructor(props) {
        super(props);
        this.state = { 
            
        };

    }

    componentDidMount(){

    }
    
    render() {

        return (
            <div className={cx('react-test-class-noprops')}>

            </div>
        );
    }
}


export default ReactTestClassNoprops;
