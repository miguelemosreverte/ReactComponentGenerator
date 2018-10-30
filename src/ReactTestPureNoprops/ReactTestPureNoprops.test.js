import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestPureNoprops from './ReactTestPureNoprops';

it('ReactTestPureNoprops initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactTestPureNoprops />, div);
  ReactDOM.unmountComponentAtNode(div);
});
