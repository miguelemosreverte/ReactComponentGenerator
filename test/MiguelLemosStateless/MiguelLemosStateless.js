import React from 'react';
import styles from './MiguelLemosStateless.scss';
import classNames from 'classnames/bind';
import PropTypes from 'prop-types';
const cx = classNames.bind(styles);
const MiguelLemosStateless = ({ edad , altura }) => 
    (
        <div className={cx('miguel-lemos-stateless')}>

        </div>
    );

MiguelLemosStateless.propTypes = {
  edad: PropTypes.String,
  altura: PropTypes.Number
};
export default MiguelLemosStateless;
