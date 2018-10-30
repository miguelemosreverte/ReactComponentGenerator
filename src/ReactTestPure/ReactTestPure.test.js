import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestPure from './ReactTestPure';

it('ReactTestPure initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactTestPure />, div);
  ReactDOM.unmountComponentAtNode(div);
});
