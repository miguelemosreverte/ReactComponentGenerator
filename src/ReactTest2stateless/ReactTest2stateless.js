import React from 'react';
import styles from './ReactTest2stateless.scss';
import classNames from 'classnames/bind';
import PropTypes from 'prop-types';
const cx = classNames.bind(styles);
const ReactTest2stateless = ({ age }) => 
    (
        <div className={cx('react-test-2stateless')}>

        </div>
    );

ReactTest2stateless.propTypes = { age: PropTypes.string };
export default ReactTest2stateless;
