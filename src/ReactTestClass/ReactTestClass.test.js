import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestClass from './ReactTestClass';

it('ReactTestClass initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactTestClass />, div);
  ReactDOM.unmountComponentAtNode(div);
});
