import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestStateless from './ReactTestStateless';

it('ReactTestStateless initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactTestStateless />, div);
  ReactDOM.unmountComponentAtNode(div);
});
