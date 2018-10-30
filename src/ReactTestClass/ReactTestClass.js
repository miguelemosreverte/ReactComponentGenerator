import React,{ Component } from 'react';
import styles from './ReactTestClass.scss';
import classNames from 'classnames/bind';
import PropTypes from 'prop-types';
const cx = classNames.bind(styles);

class ReactTestClass extends Component {

    constructor(props) {
        super(props);
        this.state = { 
            
        };

    }

    componentDidMount(){

    }
    
    render() {
      const { age } = this.props;

        return (
            <div className={cx('react-test-class')}>

            </div>
        );
    }
}

ReactTestClass.propTypes = {
  age: PropTypes.string
};

export default ReactTestClass;
