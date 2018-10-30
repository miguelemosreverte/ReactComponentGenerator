import React,{ PureComponent } from 'react';
import styles from './ReactTestPure.scss';
import classNames from 'classnames/bind';
import PropTypes from 'prop-types';
const cx = classNames.bind(styles);

class ReactTestPure extends PureComponent {

    constructor(props) {
        super(props);
        this.state = { 
            
        };

    }

    componentDidMount(){

    }
    
    render() {
const { age , page } = this.props;

        return (
            <div className={cx('react-test-pure')}>

            </div>
        );
    }
}

ReactTestPure.propTypes = {
  age: PropTypes.string,
  page: PropTypes.number
};
export default ReactTestPure;
