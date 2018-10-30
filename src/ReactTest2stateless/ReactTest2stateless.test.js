import React from 'react';
import ReactDOM from 'react-dom';
import ReactTest2stateless from './ReactTest2stateless';

it('ReactTest2stateless initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactTest2stateless />, div);
  ReactDOM.unmountComponentAtNode(div);
});
