import React from 'react';
import styles from './ReactTestStateless.scss';
import classNames from 'classnames/bind';
import PropTypes from 'prop-types';
const cx = classNames.bind(styles);
const ReactTestStateless = ({ age , page }) => 
    (
        <div className={cx('react-test-stateless')}>

        </div>
    );

ReactTestStateless.propTypes = {
  age: PropTypes.string,
  page: PropTypes.number
};
export default ReactTestStateless;
